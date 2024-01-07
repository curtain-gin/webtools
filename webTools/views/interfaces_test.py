from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.interface_info_form import *
from webTools.public.daba_tuple_to_dict import execute_query
from django.http import QueryDict
import json
from webTools.public.logger import decorator_log
from webTools.public.logger import get_logger


def interfaces_test_list(request):
    forms = models.InterfaceInfo.objects.all()

    tille = "接口列表"
    return render(
        request, "web/interfaces_test_list.html", {"ff": forms, "tille": tille}
    )


@decorator_log
def interfaces_test_add(request):
    get_logger().info("接口添加")
    # 接口添加
    if request.method == "GET":
        forms = InterfaceInfoAddForm()

        tille = "接口添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    else:

        form = InterfaceInfoAddForm(data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("/list/of/interfaces/")
        else:
            return render(request, "web/chenge.html", {"form": form})


def dict_to_querset(asdf):
    ppp2 = []
    iiiii2 = {}
    for i in asdf:
        iiiii2["name"] = i
        iiiii2["aa"] = asdf[i]
        ppp2.append(iiiii2)
        iiiii2 = {}

    return ppp2


@decorator_log
def interfaces_test_info(request, nid):
    if request.method == "GET":
        data=models.InterfaceInfo.objects.filter(interface_id=nid).first()

        tille = "接口信息"
        return render(
            request,
            "web/interfaces_test_info.html",
            {
                "data": data,
                "tille": tille,

            },
        )


def interfaces_test_edit(request, nid):
    row_object = models.InterfaceInfo.objects.filter(interface_id=nid).first()
    tille = "版本编辑"
    if request.method == "GET":
        form = InterfaceInfoAddForm(instance=row_object)
        return render(request, "web/chenge.html", {"form": form, "tille": tille})
    else:
        form = InterfaceInfoAddForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/list/of/interfaces/")
        else:
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
