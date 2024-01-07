#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @@ScriptName:
# @@Author:
# @@Create Date:
# @@Modify Date:
# @@Description:

import xlsxwriter as xw
import os
import logging
def xw_toExcel(data, fileName,xmind_path,xmindname):  # xlsxwriter库储存数据到excel
    logger=logging.getLogger('django')
    try:
        if '字数超过200' in data:
            return 'false'
        else:
            logger.error("########################################")
            # dir = os.path.abspath(__file__)
            # a = dir.split("up_xmind")[0]
            # dirr = '{}xmind_import_excel/excel_file/{}'.format(a, fileName)
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            storage_path = os.path.join(os.path.dirname(BASE_DIR), "webTools/data/up_excl/",fileName)
            workbook = xw.Workbook(storage_path)  # 创建工作簿
            bold_title = workbook.add_format({
                'bold': True,  # 字体加粗
                'border': 1,  # 单元格边框宽度
                'align': 'left',  # 水平对齐方式
                'valign': 'vcenter',  # 垂直对齐方式
                'fg_color': '#C4BC97',  # 单元格背景颜色
                'text_wrap': False,  # 是否自动换行
            })
            bold = workbook.add_format({
                'text_wrap': True,  # 是否自动换行
                'valign': 'vcenter',
            })
            worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
            worksheet1.activate()  # 激活表
            title = ['用例目录', '用例名称', '需求ID', '前置条件', '用例步骤', '预期结果', '用例类型', '用例状态', '用例等级', '创建人']  # 设置表头
            worksheet1.write_row('A1', title, bold_title)  # 从A1单元格开始写入表头
            worksheet1.set_column('A:J', 25)
            i = 2  # 从第二行开始写入数据
            for j in range(len(data)):
                insertData = [data[j]["case_directory"], data[j]["case_title"], data[j]["require_id"], data[j]["precondition"], data[j]["case_step"],
                              data[j]["case_expect"], data[j]["case_type"], data[j]["case_status"], data[j]["case_level"], data[j]["creator"]]
                row = 'A' + str(i)
                worksheet1.write_row(row, insertData, bold)
                i += 1
            workbook.close()  # 关闭表
            # xmind_remove_path=os.path.join(xmind_path,xmindname)
            xmindname=xmindname+".xmind"

            xmind_storage_path = os.path.join(os.path.dirname(BASE_DIR), "webTools/data/up_xmind",xmindname )
            os.remove(xmind_storage_path)


            return 'true'
    except Exception as e:
        logger.error("导出excel失败：{}".format(e))


# if __name__ == "__main__":
#     dir=os.path.abspath(__file__)
#     a = dir.split("up_xmind")[0]
#     dirr = '{}xmind_import_excel/excel_file'.format(a)
#     print(dirr)
