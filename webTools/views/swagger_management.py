import requests
import json
import os
import time
import logging
import pandas
from urllib import parse
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.swagger_management_form import *
from webTools.forms.interface_info_form import *
from webTools.forms.version_management_form import *
from django.http.request import QueryDict
from django.http import Http404, FileResponse
from webTools.public.swagger_data_processing import DataProcessing

from webTools.public.logger import get_logger
from webTools.public.encrypt import md5


# from webTools.public.swagger_data_processing import


def swagger_management_list(request):
    tille = "swagger列表"
    forff = models.SwaggerTasks.objects.all()
    return render(
        request, "web/swagger_management_list.html", {"data": forff, "tille": tille}
    )


@csrf_exempt
def swagger_authentication(request):
    if request.method == "POST":
        request_data = eval(request.body.decode("UTF-8").replace("\\", ""))
        sdp_user = request_data["user"]
        sdp_data = request_data["data"]
        ssd_pwd = models.UserAppInfo.objects.get(username=sdp_user).password
        if ssd_pwd == md5(sdp_data):
            response_parameters = {"code": "200", "msg": "%s" % ssd_pwd}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        else:
            response_parameters = {"code": "201", "msg": "认证失败"}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))


def swagger_management_add(request):
    if request.method == "GET":
        forms = SwaggerMangementAdd()
        tille = "swagger任务添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    elif request.method == "POST":
        form = SwaggerMangementAdd(data=request.POST)
        if form.is_valid():

            form.save()
            return redirect("/swagger/management/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})

    else:
        forms = models.SystemEnvironment.objects.all()
        return render(request, "web/swagger_management_list.html", {"fro": forms})


def swagger_interfaceInfo_list(request):
    ff = models.Swagger_InterfaceInfo.objects.all().order_by("-interface_id")[0:4000]
    tille = "swagger同步接口列表"
    return render(
        request, "web/swagger_interfaceInfo_list.html", {"ff": ff, "tille": tille}
    )


def swagger_management_run(request, nid):
    swagger_url = models.SystemEnvironment.objects.get(environment_id=nid).swagger_url
    token = models.UserAppInfo.objects.get(username='SDP').password
    reponse = DataProcessing.first_data(token, swagger_url)
    print(reponse)
    return redirect('/request/environment/list/')


@csrf_exempt
def     swagger_management_auto_run(request):
    if request.method == "GET":
        response_parameters = {"code": "404"}
        return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))

    else:
        response_dict = json.loads(request.body.decode())
        ssd_pwd = models.UserAppInfo.objects.get(username="SDP").password
        get_logger().info(response_dict)

        old_swagger_url = response_dict["env"]

        # https://api-dev.ennejb.cn/api/sms/swagger-ui.html
        # /v2/api-docs
        swagger_toekn = response_dict["token"]
        if swagger_toekn != ssd_pwd:
            response_parameters = {"code": "201", "errmsg": "认证失败"}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        swagger_url_list = models.SystemEnvironment.objects.filter(
            swagger_url=old_swagger_url
        ).count()
        get_logger().info(swagger_url_list)
        if (
                models.SystemEnvironment.objects.filter(swagger_url=old_swagger_url).count()
                < 1
        ):
            response_parameters = {"code": "202", "errmsg": "环境不存在"}
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        swagger_url = str(response_dict["env"]).replace(
            "/swagger-ui.html", "/v2/api-docs"
            # "/swagger-ui.html",
            # "/v2/apidocs",  # 测试使用
        )
        get_logger().info(swagger_url)

        ssagger_json = requests.get(swagger_url).json()

        # swagger_paths = dict(ssagger_json["paths"])
        swagger_version = dict(ssagger_json)["info"]["version"]
        print(swagger_version)
        # swagger_definitions = dict(ssagger_json["definitions"])
        env_id = str(
            models.SystemEnvironment.objects.get(
                swagger_url=old_swagger_url
            ).environment_id
        )

        version_swagger = models.VersionManagement.objects.filter(
            version_number=swagger_version, environment_id=env_id
        ).count()

        if version_swagger < 1:
            local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            version_name = swagger_version
            creat_time = local_time
            creat_user = "系统"
            version_number = swagger_version

            dddd = (
                f"version_name={version_name}&version_number={version_number}"
                f"&creat_time={creat_time}&creat_user={creat_user}"
                f"&environment_id={env_id}"
            )
            pp = QueryDict(dddd, encoding="utf-8")
            form = VersionManagementAdd(data=pp)

            if form.is_valid():
                form.save()

            else:
                response_parameters = {"code": "203", "errmsg": "生成版本失败"}
                return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        versionmanagement = models.VersionManagement.objects.get(
            version_number=swagger_version, environment_id=env_id
        ).version_id

        ts_or_test = 3
        iii = DataProcessing(swagger_url, env_id, versionmanagement, ts_or_test)
        iii.initial_data_processing()
        # 生成ts列表
        ts = [
            "https://swagger.ennejb.cn/swagger/opcs/v2/api-docs	",
            'http://0.0.0.0:7777/mock/ooo/v2/apidocs',
            'http://0.0.0.0:7777/mock/oooo/v2/apidocs',
            'https://swagger.ennejb.cn/swagger/api/sms/v2/api-docs',
            'https://swagger.ennejb.cn/swagger/api/file/v2/api-docs',
            'https://swagger.ennejb.cn/swagger/api/es/v2/api-docs'
        ]
        ts_or_test = 1
        if swagger_url in str(ts):
            iii = DataProcessing(swagger_url, env_id, versionmanagement, ts_or_test)
            iii.ts_data()
        ts_or_test = 0
        ts2 = [
            "https://swagger.ennejb.cn/swagger/opcs/v2/api-docs",
            'http://0.0.0.0:7777/mock/ooo/v2/apidocs',
            'https://swagger.ennejb.cn/swagger/api/sms/v2/api-docs',
            'https://swagger.ennejb.cn/swagger/api/file/v2/api-docs',
            'https://swagger.ennejb.cn/swagger/api/es/v2/api-docs'
        ]
        print(old_swagger_url)

        if swagger_url in str(ts2):
            iii = DataProcessing(swagger_url, env_id, versionmanagement, ts_or_test)
            iii.ts_data()

        interface_results = {"code": 200, "msg": "数据存储成功，TS生成完毕，MOCK服务更新启动成功"}
        return HttpResponse(json.dumps(interface_results, ensure_ascii=False))


def swagger_info(request, nid):
    data = models.Swagger_InterfaceInfo.objects.filter(interface_id=nid).first()
    return render(request, "web/swagger_interface_info.html", {"data": data})


def swagger_ts_down(request, nid):
    if request.method == "GET":
        ts_dow_ddress = models.SystemEnvironment.objects.get(environment_id=nid).download_address
        logger = logging.getLogger("django")
        try:
            if request.method == "GET":
                logger = logging.getLogger("django")

                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                storage_path = parse.unquote(
                    os.path.join(
                        os.path.dirname(BASE_DIR),
                        "webTools/data/TS_file/%s" % ts_dow_ddress,
                    )
                )

                logger.info(storage_path)
                response = FileResponse(open(storage_path, "rb"))
                response["content_type"] = "application/octet-stream"
                response["Content-Disposition"] = "attachment; filename={0}".format(
                    quote(ts_dow_ddress)
                )

                return response
            else:
                return redirect("/request/environment/list/")
        except Exception as e:
            logger.error(e)
            return redirect("/request/environment/list/")
    else:
        return redirect("/request/environment/list/")


def swagger_interfaceInfo_add(request):
    get_logger().info("swagger接口添加")
    # 接口添加
    if request.method == "GET":
        forms = SwaggerInterfaceInfoAdd()

        tille = "swagger接口添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    else:

        form = SwaggerInterfaceInfoAdd(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("/swagger/InterfaceInfo/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})


def swagger_template_down(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    storage_path = parse.unquote(
        os.path.join(
            os.path.dirname(BASE_DIR),
            "webTools/data/up_excl/swagger_template/swagger接口模版.xlsx",
        )
    )

    response = FileResponse(open(storage_path, "rb"))
    response["content_type"] = "application/octet-stream"
    response["Content-Disposition"] = "attachment; filename={0}".format(
        quote("swagger接口模版.xlsx")
    )
    return response


def swagger_upload(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if request.FILES.getlist("file") == []:
        XMIND_ERROR = "请上传xlsx文件"
        tille = "swagger同步接口列表"
        forff = models.Swagger_InterfaceInfo.objects.all().order_by("-interface_id")[0:4000]
        return render(
            request, "web/swagger_interfaceInfo_list.html", {"ff": forff, "tille": tille, "error": XMIND_ERROR}
        )
    files_name = request.FILES.getlist("file")[0]

    if str(files_name).endswith(".xlsx") != True:
        XMIND_ERROR = "请上传xlsx文件"
        tille = "swagger同步接口列表"
        forff = models.Swagger_InterfaceInfo.objects.all().order_by("-interface_id")[0:4000]
        return render(
            request, "web/swagger_interfaceInfo_list.html", {"ff": forff, "tille": tille, "error": XMIND_ERROR}
        )

    file_obj = request.FILES.get("file")
    storage_path = os.path.join(
        os.path.dirname(BASE_DIR), "webTools/data/up_excl/swagger_excl/"
    )
    destination = open(os.path.join(storage_path, str(files_name)), "wb+")

    for chunk in file_obj.chunks():
        destination.write(chunk)
    destination.close()
    file_data = pandas.read_excel('webTools/data/up_excl/swagger_excl/%s' % str(files_name), sheet_name='Sheet1')

    for i in file_data.index:
        interface_name = file_data.loc[i].values[1]
        request_url = file_data.loc[i].values[2]
        request_method = file_data.loc[i].values[3]
        request_parameters = file_data.loc[i].values[4]
        response_parameters = file_data.loc[i].values[5]
        creat_user = file_data.loc[i].values[6]
        environment_id_id = file_data.loc[i].values[7]
        version_id_id = file_data.loc[i].values[8]
        interface_add_type = file_data.loc[i].values[9]
        print(version_id_id)
        try:
            version_id = models.VersionManagement.objects.get(version_number=version_id_id).version_id
        except Exception as e:
            XMIND_ERROR = "版本不存在"
            tille = "swagger同步接口列表"
            forff = models.Swagger_InterfaceInfo.objects.all().order_by("-interface_id")[0:4000]
            return render(
                request, "web/swagger_interfaceInfo_list.html", {"ff": forff, "tille": tille, "error": XMIND_ERROR}
            )
        data = {
            "interface_name": interface_name,
            "request_url": request_url,
            "request_method": request_method,
            "request_parameters": request_parameters,
            "response_parameters": response_parameters,
            "creat_user": creat_user,
            "environment_id_id": environment_id_id,
            "version_id_id": version_id,
            "interface_add_type": interface_add_type,
        }
        if models.Swagger_InterfaceInfo.objects.filter(
                request_url=request_url, request_method=request_method).count() < 1:
            models.Swagger_InterfaceInfo.objects.create(**data)
        else:

            XMIND_ERROR = "请检查文件是否存在和之前接口重复数据"
            tille = "swagger同步接口列表"
            forff = models.Swagger_InterfaceInfo.objects.all().order_by("-interface_id")[0:4000]
            return render(
                request, "web/swagger_interfaceInfo_list.html", {"ff": forff, "tille": tille, "error": XMIND_ERROR}
            )
    return redirect("/swagger/InterfaceInfo/list/")


