import time
import re
import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import QueryDict
from webTools.models import OpLogs, AccessTimeOutLogs
from webTools.forms.user_form import *
from webTools import models


class LogMiddleware(MiddlewareMixin):
    """日志中间件"""

    mock_interfacedfa = models.Mock_Service_Interface.objects.all().values_list()

    lll_urls = [
        "/image/code/",
        "/test/",
        "/favicon.ico",
        "mock",
        "/",
        "/swagger/management/auto/",
        "/swagger/authentication/",
        "/test/report/view/",
        "/test/report/list/",
        "/story/test/report/list/",
        "/story/test/report/view/"
    ]  # 定义不需要记录日志的url名单

    def __init__(self, *args):
        super(LogMiddleware, self).__init__(*args)
        self.start_time = None  # 开始时间
        self.end_time = None  # 响应时间
        self.data = {}  # dict数据

    def process_request(self, request):
        """
        请求进入
        :param request: 请求对象
        :return:
        """
        logger = logging.getLogger("django")
        try:
            lpp = [
                self.mock_interfacedfa[i][3] for i in range(len(self.mock_interfacedfa))
            ]
            nbu=0
            for i in self.lll_urls:
                print("isadfa%s"%i)
                if i in request.path_info and i !='/':
                    print(request.path_info)
                    nbu += 1
            for i in self.lll_urls:
                lpp.append(i)
            print("shuzi%s"%nbu)
            if request.path_info in lpp:
                print(request.path_info)
                return None

            elif nbu>=1:
                return None
            else:
                if request.path_info == "/user/login/" and request.method == "GET":
                    # /user/login/ get 请求直接通过
                    return None

                elif request.path_info == "/user/login/" and request.method == "POST":
                    print("开始存入数据库")

                    self.start_time = time.time()  # 开始时间

                    re_time = time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime()
                    )  # 请求时间（上海时区）
                    # 请求IP
                    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
                    if x_forwarded_for:
                        # 如果有代理，获取真实IP
                        re_ip = x_forwarded_for.split(",")[0]
                    else:
                        re_ip = request.META.get("REMOTE_ADDR")

                    # 请求方法
                    re_method = request.method

                    # 请求参数
                    re_content = request.GET if re_method == "GET" else request.POST
                    if re_content:
                        # 筛选空参数
                        re_content = QueryDict.dict(re_content)
                    else:
                        re_content = None

                    form = LoginModelFrom(data=request.POST)
                    mobile_phone = form.data["mobile_phone"]
                    request_path = request.path_info
                    request_path = re.sub(r"[0-9]/", "", request_path)
                    # 查询PermissionPath id
                    path_id = (
                        models.PermissionPath.objects.filter(
                            permission_path=request_path
                        )
                        .get()
                        .permission_path_id
                    )
                    print("进入啊定时发多发")
                    self.data.update(
                        {
                            "re_time": re_time,  # 请求时间
                            "permission_path_id_id": path_id,  # 请求url
                            "re_method": re_method,  # 请求方法
                            "re_ip": re_ip,  # 请求IP
                            "re_content": re_content,  # 请求参数
                            "re_user": mobile_phone,  # 手机号
                            # 're_user': 'AnonymousUser'  # 匿名操作用户测试
                        }
                    )

                else:
                    print("开始存入数据库2")
                    self.start_time = time.time()  # 开始时间

                    re_time = time.strftime(
                        "%Y-%m-%d %H:%M:%S", time.localtime()
                    )  # 请求时间（上海时区）
                    # 请求IP
                    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
                    if x_forwarded_for:
                        # 如果有代理，获取真实IP
                        re_ip = x_forwarded_for.split(",")[0]
                    else:
                        re_ip = request.META.get("REMOTE_ADDR")

                    # 请求方法
                    re_method = request.method

                    # 请求参数
                    re_content = request.GET if re_method == "GET" else request.POST
                    if re_content:
                        # 筛选空参数
                        re_content = QueryDict.dict(re_content)

                    else:
                        re_content = None
                    # sesion存储

                    info_dict = request.session.get("info")
                    user_mobile_phone = info_dict["mobile_phone"]
                    # 查询PermissionPath id
                    request_path = request.path_info
                    request_path = re.sub(r"[0-9]+/", "", request_path)

                    path_id = (
                        models.PermissionPath.objects.filter(
                            permission_path=request_path
                        )
                        .get()
                        .permission_path_id
                    )
                    self.data.update(
                        {
                            "re_time": re_time,  # 请求时间
                            "permission_path_id_id": path_id,  # 请求url
                            "re_method": re_method,  # 请求方法
                            "re_ip": re_ip,  # 请求IP
                            "re_content": re_content,  # 请求参数
                            "re_user": user_mobile_phone,  # 操作人(需修改)，网站登录用户
                            # 're_user': 'AnonymousUser'  # 匿名操作用户测试
                        }
                    )
        except Exception as e:
            logger.error(e)

    def process_response(self, request, response):
        """
        响应返回
        :param request: 请求对象
        :param response: 响应对象
        :return: response
        """
        logger = logging.getLogger("django")
        try:
            # 请求url在 exclude_urls中，不保存操作日志记录
            lpp = [
                self.mock_interfacedfa[i][3] for i in range(len(self.mock_interfacedfa))
            ]
            nbu = 0
            for i in self.lll_urls:
                if i in request.path_info and  i !="/":
                    nbu += 1
            for i in self.lll_urls:
                lpp.append(i)
            print(lpp)
            if request.path_info in lpp:
                return response
            elif nbu>=1:
                return response

            else:
                # /user/login/ get 请求直接通过
                if request.path_info == "/user/login/" and request.method == "GET":

                    return response
                elif request.path_info == "/user/login/" and request.method == "POST":
                    self.end_time = time.time()  # 响应时间
                    access_time = self.end_time - self.start_time
                    self.data["access_time"] = round(access_time * 1000)  # 耗时毫秒/ms

                    # 耗时大于3s的请求,单独记录 (可将时间阈值设置在settings中,实现可配置化)
                    if self.data.get("access_time") > 3 * 1000:

                        AccessTimeOutLogs.objects.create(**self.data)  # 超时操作日志入库db

                    OpLogs.objects.create(**self.data)  # 操作日志入库db
                    return response
                else:
                    self.end_time = time.time()  # 响应时间
                    access_time = self.end_time - self.start_time
                    self.data["access_time"] = round(access_time * 1000)  # 耗时毫秒/ms
                    # 耗时大于3s的请求,单独记录 (可将时间阈值设置在settings中,实现可配置化)
                    if self.data.get("access_time") > 3 * 1000:
                        AccessTimeOutLogs.objects.create(**self.data)  # 超时操作日志入库db
                    OpLogs.objects.create(**self.data)  # 操作日志入库db

                    return response
        except Exception as e:
            logger.error(e)
