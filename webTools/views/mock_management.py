# encoding:utf-8
import json
from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from webTools.forms.mock_serice_interfaces_from import *



@csrf_exempt
def mock_server(request):
    request_path = request.path_info
    if request.method == "GET":
        if  models.Mock_Service_Interface.objects.filter(request_url=request_path, request_method=0,interface_add_type=1):
            response_parameters = json.loads(
                models.Mock_Service_Interface.objects.get(
                    request_url=request_path, request_method=0,interface_add_type=1
                )
                .response_parameters.replace("\n", "")
                .replace("\r", "")
            )

            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        elif models.Mock_Service_Interface.objects.filter(request_url=request_path,request_method=0,interface_add_type=0):
                response_parameters = json.loads(
                    models.Mock_Service_Interface.objects.get(
                        request_url=request_path, request_method=0, interface_add_type=0
                    )
                    .response_parameters.replace("\n", "")
                    .replace("\r", "")
                )

                return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        else:
            response_parameters = {
                "errcode": 404,
                "errmsg": "不存在的api, 当前请求path为 %s， 请求方法为 GET ，请确认是否定义此请求。"
                          % request.path_info,
                "data": None,
            }
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
    else:
        if  models.Mock_Service_Interface.objects.filter(request_url=request_path, request_method=1,interface_add_type =1):
            response_parameters = json.loads(
                models.Mock_Service_Interface.objects.get(
                    request_url=request_path, request_method=1,interface_add_type=1
                )
                .response_parameters.replace("\n", "")
                .replace("\r", "")
            )
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        elif models.Mock_Service_Interface.objects.filter(request_url=request_path,
                                                      request_method=1,
                                                       interface_add_type=0):
                response_parameters = json.loads(
                    models.Mock_Service_Interface.objects.get(
                        request_url=request_path, request_method=1, interface_add_type=0
                    ) .response_parameters.replace("\n", "")
                    .replace("\r", "")
                )
                return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))
        else:
            response_parameters = {
                "errcode": 404,
                "errmsg": "不存在的api, 当前请求path为 %s， 请求方法为 POST ，请确认是否定义此请求。"
                          % request.path_info,
                "data": None,
            }
            return HttpResponse(json.dumps(response_parameters, ensure_ascii=False))

def mock_serice_interfaces_list(request):

    data = models.Mock_Service_Interface.objects.all().order_by("-mock_service_id")
    tille = "mock接口服务列表"
    return render(
        request, "web/mock_serice_interfaces_list.html", {"ff": data, "tille": tille}
    )



def mock_serice_interfaces_add(request):

    # 接口添加
    if request.method == "GET":
        forms = MockServiceInterfaceAdd()

        tille = "MOCK接口添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    else:
        print(request.POST)
        form = MockServiceInterfaceAdd(data=request.POST)
        form.instance.interface_add_type = 0

        if form.is_valid():
            form.save()
            return redirect("/mockserice/interfaces/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})
def mock_serice_interfaces_info(request,nid):
    data=models.Mock_Service_Interface.objects.filter(mock_service_id=nid).first()
    return render(request,"web/mock_serice_interfaces_info.html",{"data":data})

def mock_serice_interfaces_edit(request,nid):
    row_object=models.Mock_Service_Interface.objects.filter(mock_service_id=nid).first()
    if request.method == "GET":

        tille = "MOCK服务修改"
        form = MockServiceInterfaceEdit(instance=row_object)
        return render(request, "web/chenge.html", {"form": form, "tille": tille})
    else:
        form = MockServiceInterfaceEdit(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/mockserice/interfaces/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})
