from django.shortcuts import redirect, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from webTools import models


class AuthMiddleware(MiddlewareMixin):
    """
    用户登陆认证中间件
    """

    def process_request(self, request):

        mock_interfacedfa_url = (
            models.Mock_Service_Interface.objects.all().values_list()
        )

        url_lsit = [
            mock_interfacedfa_url[i][3] for i in range(len(mock_interfacedfa_url))
        ]
        url_lsit2 = [
            "/user/login/",
            "/image/code/",
            "/test/",
            "/favicon.ico",
            "/swagger/management/auto/",
            "/swagger/authentication/",
            "/test/report/list/",
            "/test/report/view/",
            "/story/test/report/list/",
            "/story/test/report/view/"
        ]
        for i in url_lsit2:
            url_lsit.append(i)
        print(request.path_info)
        nbu = 0
        for i in url_lsit:
            if i in request.path_info:
                nbu += 1
        if request.path_info in url_lsit2:
            return
        elif nbu>=1:
            return
        else:
            info_dict = request.session.get("info")
            if info_dict:
                return
            return redirect("/user/login/")
