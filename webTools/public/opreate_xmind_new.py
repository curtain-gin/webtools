#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @@ScriptName:
# @@Author:
# @@Create Date:
# @@Modify Date:
# @@Description:


"""
case_directory  用例目录
case_title  用例名称
require_id  需求id
precondition  前置条件
case_step 用例步骤
case_expect 预期结果
case_type 用例类型
case_status 用例状态
case_level 用例等级
creator 创建人
"""
import os
import copy
import logging
from xmindparser import xmind_to_dict
from collections import Counter

class ReadXmind(object):


    def __init__(self, file, path):
        self.cases = []
        self.file = file
        self.path = path
        self.case_list = []
        self.case_title_list = []
        self.end_case = ''
        self.titles = []
        self.title_max = ''
        self.master_dire = ''

    def check_xmind_title(self):
        logger = logging.getLogger('django')
        """获取指定文件夹下的xmind文件，校验标题是否规范"""
        try:
            xm_base = xmind_to_dict(self.path)[0]['topic']
            return xm_base
        except Exception as e:
            logger.error("校验用例失败：{}".format(e))

    def get_case_new(self, json_data, cur=''):
        logger = logging.getLogger('django')
        """
        新处理方法
        """
        try:
            single_case = {}
            if 'makers' not in json_data:
                cur += '~~~' + json_data['title']
            else:
                cur += '~~~' + json_data['title'] + json_data['makers'][0]

            for k, v in json_data.items():
                if isinstance(v, list):
                    for i in v:
                        if isinstance(i, dict):
                            self.get_case_new(i, cur)
                else:
                    if ('topics' not in json_data) and (k == 'title'):
                        cur_all = cur[3:]
                        if 'flag-red' in cur_all:
                            # 获取优先级
                            if 'priority-1' in cur_all:
                                single_case['case_level'] = '高'
                                cur_all = cur_all.replace("priority-1", "")
                            else:
                                single_case['case_level'] = '低'
                            all = cur_all.split('~~~')
                            self.titles.append(cur_all.split('flag-red')[0])
                            # 获取打标的位置
                            title_address = 0
                            for a in all:
                                if 'flag-red' in a:
                                    break
                                title_address += 1
                            # 处理子目录
                            dire_str = ''
                            for dire_num in range(1, title_address):
                                dire_str += '-' + all[dire_num]
                            # 处理目录、创建人、需求id
                            if '#' in all[0]:
                                case_directory = all[0].split('#')[0]
                                creator = all[0].split('#')[1]
                                require_id = all[0].split('#')[-1]
                            else:
                                case_directory, creator, require_id = all[0], '', ''
                            self.master_dire = case_directory
                            case_directory = case_directory + dire_str
                            single_case['case_directory'] = case_directory
                            # 处理用例名称
                            title = all[title_address].split('flag-red')[0]
                            single_case['case_title'] = title
                            if len(title) > 200:
                                self.title_max = '用例[{}]字数超过200，请更正后重新上传'.format(case_directory + '-' +title)
                            single_case['require_id'] = require_id
                            single_case['precondition'] = ''
                            # 处理用例步骤(注意标题后无步骤的情况)
                            if len(all) - title_address == 1:
                                single_case['case_step'] = ''
                            else:
                                single_case['case_step'] = all[title_address + 1]
                            # 处理用例期望
                            expect_count = len(all) - (title_address + 2)
                            if expect_count in [0, -1]:
                                single_case['case_expect'] = ''
                            elif expect_count == 1:
                                single_case['case_expect'] = all[title_address + 2]
                            elif expect_count > 1:
                                expect_all = ''
                                for expect in range(title_address + 2, len(all)):
                                    expect_all += all[expect] + '；'
                                expect_all = expect_all[:-1]
                                single_case['case_expect'] = expect_all
                            single_case['case_type'] = '功能测试'
                            single_case['case_status'] = '正常'
                            single_case['creator'] = creator
                            self.cases.append(single_case)
        except Exception as e:
            logger.error('处理xmind出错：{}'.format(e))


    def add_case_dict(self):
        """
        添加到用例集合里
        """

    def get_case(self, json_data, cur=''):
        logger = logging.getLogger('django')
        """
        :param json_data: 被解析的json
        :param cur:
        :return:
        """
        cur += '##' + json_data['title']
        single_case = {}
        # 前置条件是否存在
        if 'callout' in json_data:
            single_case['precondition'] = json_data['callout'][0]
        elif 'callout' not in json_data:
            single_case['precondition'] = ''
        # 判断标记存在
        if 'makers' in json_data:
            if 'flag-red' in json_data['makers']:
                # 用例等级校验
                if 'priority-1' in json_data['makers']:
                    single_case['case_level'] = '高'
                elif 'priority-2'in json_data['makers']:
                    single_case['case_level'] = '中'
                else:
                    single_case['case_level'] = '低'
                d = ''
                for k, v in json_data.items():
                    if 'title' in v[0]:
                        num = 0
                        for c in v:
                            # 处理期望值后面的内容
                            if 'topics' in c:
                                self.deal_end_content(c['topics'])
                                self.end_case = '({})'.format(self.end_case[:-1])
                            num += 1
                            d += str(num) + '、' + c['title'] + self.end_case + '\n'
                            self.end_case = ''
                d = d[:-1]
                cur += '##' + d
                case = cur[2:]
                all = case.split('##')
                if '#' in all[0]:
                    case_directory = all[0].split('#')[0]
                    creator = all[0].split('#')[1]
                    require_id = all[0].split('#')[-1]
                else:
                    case_directory, creator, require_id = all[0], '', ''
                single_case['case_directory'] = case_directory
                single_case['case_expect'] = all[-1]
                del all[0]
                del all[-1]
                del all[-1]
                title = ''
                for e in all:
                    title += '-' + e
                title = title[1:]
                if len(title) > 200:
                    self.title_max = '用例[{}]字数超过200，请更正后重新上传'.format(title)
                single_case['case_title'] = title
                self.titles.append(title)
                single_case['case_step'] = json_data['title']
                single_case['require_id'] = ''

                single_case['case_type'] = '功能测试'
                single_case['case_status'] = '正常'
                single_case['creator'] = creator
                single_case['require_id'] = require_id

                self.cases.append(single_case)
        for k, v in json_data.items():
            if isinstance(v, list):
                for i in v:
                    if isinstance(i, dict):
                        self.get_case(i, cur)
            else:
                if ('topics' not in json_data) and (k == 'title'):
                    cur = cur[1:]

    def deal_end_content(self, json_data):
        """
        取出case
        """

        if isinstance(json_data, list):
            for i in json_data:
                self.end_case += i['title'] + '、'
                if 'topics' in i:
                    self.deal_end_content(i['topics'])


def main_cases():
    logger = logging.getLogger('django')
    """
    批量执行校验xmind文件
    :return:
    """
    try:
        path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/' + 'data/up_xmind'
        name=[]
        all_cases=[]
        for path_base, j, files in os.walk(path):
            for file in files:
                if file == '__init__.py' :
                    continue
                elif file == '.DS_Store':
                    continue
                xmind_path = path_base + '/' + file

                logger.info('开始校验执行文件【{}】'.format(xmind_path))
                xmindname = file.rsplit(".", 1)[0]
                name.append(xmindname)
                bb = ReadXmind(file, xmind_path)
                bb.get_case_new(bb.check_xmind_title())
                first_title = bb.master_dire
                # print(bb.cases)
                if bb.title_max != '':
                    return bb.title_max
                title = bb.titles
                # 在重复的标题后面加上序号
                dict_json = dict(Counter(title))
                json_dict = {key: value for key, value in dict_json.items() if value > 0}  #统计重复个数
                titles_new = []
                for key, value in json_dict.items():
                    # 标题无重复的情况
                    if value == 1:
                        titles_new.append(key)
                    # 标题重复的情况
                    else:
                        for num in range(1, value + 1):
                            titles_new.append(key + '-' + str(num))
                cases = bb.cases
                # 处理后的标题替换原始重复标题
                for num in range(len(titles_new)):
                    title = titles_new[num]
                    cases[num]['case_title'] = title.split('~~~')[-1]
                cases_smoke = []
                # 筛选出优先级高的冒烟用例
                for case in cases:
                    for key, value in case.items():
                        if key == 'case_level' and value == '高':
                            case_a = copy.copy(case)
                            cases_smoke.append(case_a)
                # 处理冒烟用例的case_directory，加上路径
                for smoke_single in cases_smoke:
                    old_directory = smoke_single['case_directory']
                    new_directory = old_directory.replace(first_title, first_title + '-冒烟用例')
                    smoke_single['case_directory'] = new_directory
                all_cases1 = cases + cases_smoke
                all_cases.append(all_cases1)



            return all_cases,name,xmind_path
    except Exception as e:
        logger.error("批量执行xmind用例失败：{}".format(e))


# if __name__ == "__main__":
#     aa = {'title': '保鱼通v1.2#张砚程#5475655', 'topics': [{'title': '需求文档：xxxxxxxxxx'}, {'title': '涉及库：res_user'}, {'title': '制作方案', 'topics': [{'title': '配置产品', 'topics': [{'title': '选择产品弹窗', 'topics': [{'title': '搜索框', 'makers': ['priority-1'], 'topics': [{'title': '暗提示', 'topics': [{'title': '根据当前险种展示，选择xx主险', 'topics': [{'title': 'customercore.xls', 'link': 'xap:resources/357317e7eaeede81ff1ae6d68abbf54b70ecc0ffd5573cd3e575e63fbd1c0964.xls'}]}]}, {'title': '点击搜索框动作', 'topics': [{'title': '点击搜索框，光标定位于输入框，并弹出键盘', 'topics': [{'title': '注意：输入关键字后暗提示消失', 'note': '非常棒。。。。。'}]}]}, {'title': '搜索结果', 'topics': [{'title': '中英文筛选、特殊符号筛选'}, {'title': '符合筛选条件'}, {'title': '对应的关键字全部高亮展示'}, {'title': '表user_basic存在'}]}, {'title': '清空筛选再次搜索', 'topics': [{'title': '搜索结果展示后，清空筛选项，点击搜索，不影响搜索结果的展示'}]}, {'title': '点击搜索结果', 'topics': [{'title': '关闭操作栏并将产品名称填入到页面中，展示各配置项和附加险'}]}]}, {'title': '热门推荐', 'topics': [{'title': '展示该险种下，顾问可见范围内的三款产品，支持点击选中'}, {'title': '无热门推荐的产品', 'topics': [{'title': '展示为空'}]}, {'title': '新增的年金险类产品推荐逻辑', 'makers': ['priority-2'], 'topics': [{'title': '每个产品的推荐权重系数=所有佣金比例累加值/佣金条数；', 'topics': [{'title': '111111'}, {'title': '222222'}]}, {'title': '每个险种默认选中权重系数最大的产品；'}, {'title': '权重系数每日更新一次；'}]}]}]}, {'title': '配置产品页面', 'topics': [{'title': '返回按钮', 'makers': ['priority-3'], 'topics': [{'title': '点击返回按钮', 'topics': [{'title': '返回至制作方案页面'}]}]}, {'title': '产品名称', 'makers': ['priority-1'], 'topics': [{'title': '查看选中的产品名', 'topics': [{'title': '显示为【主险】或【附加险】+产品名称'}]}, {'title': '产品名称较长时', 'topics': [{'title': '分行展示，最多展示2行，超过用…表示'}]}]}]}]}]}, {'title': '去掉产品海报的banner入口', 'topics': [{'title': '入口', 'topics': [{'title': '首页--banner', 'topics': [{'title': '产品海报不显示，仅展示保险方案讲解；（取消切换banner的交互）'}]}, {'title': '之前保存的海报可以正常扫描--打开产品', 'topics': [{'title': '测试环境的，合作产品ID：718'}, {'title': '预发环境的，合作产品ID：793'}]}, {'title': '客户扫描二维码打开产品', 'topics': [{'title': 'res_order.page_share_record.model==产品海报分享'}, {'title': 'res_customercore.customer_follow_up '}]}]}]}]}
#     main_cases()