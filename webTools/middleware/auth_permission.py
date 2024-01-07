import logging

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from webTools import models


class AuthPermissionMiddleware(MiddlewareMixin):
    """
    用户权限中间件
    """
    def process_request(self, request):
        logger = logging.getLogger("django")
        try:
            mock_interfacedfa_url = (
                models.Mock_Service_Interface.objects.all().values_list()
            )

            url_lsit = [
                mock_interfacedfa_url[i][3] for i in range(len(mock_interfacedfa_url))
            ]
            print(url_lsit)
            url_lsit2 = [
                "/user/login/",
                "/image/code/",
                "/test/",
                "/permission/info/",
                "/favicon.ico",
                "/mock/",
                "/swagger/management/auto/",
                "/swagger/authentication/",
                "/test/report/list/",
                "/test/report/view/",
                "/story/test/report/list/",
                "/story/test/report/view/",
            ]
            for i in url_lsit2:
                url_lsit.append(i)
            nbu=0
            for i in url_lsit:
                if i in request.path_info:
                    nbu += 1
            if request.path_info in url_lsit:
                return
            elif nbu>=1:
                return
            else:
                # # 直接通过url
                # path_list = ['/image/code/', '/test/', '/favicon.ico/', '/mock/', '/swagger/management/auto/']
                print(request.path_info)
                info_dict = request.session.get("info")
                user_mobile_phone = info_dict["mobile_phone"]
                sds = models.UserAppInfo.objects.get(mobile_phone=user_mobile_phone)

                # 用户角色列表
                role_list = sds.role.all()

                sign = 0
                for i in role_list:
                    role_capabilities = models.PermissionPath.objects.filter(
                        role__role_name=i
                    ).values("permission_path")

                    # 查询角色 包含开放功能

                    for ii in range(len(role_capabilities)):
                        # 是否在直接通过url

                        if role_capabilities[ii]["permission_path"] in role_list:
                            print(role_capabilities[ii])
                            print(url_lsit)
                            # 直接通过返回
                            return
                        elif (
                            role_capabilities[ii]["permission_path"]
                            in request.path_info
                        ):

                            sign = sign + 1
                        else:

                            continue
                if sign >= 1:
                    return
                else:
                    return redirect("/permission/info/")
        except Exception as e:
            logger.error(e)
