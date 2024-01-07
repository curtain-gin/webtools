import os
from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.version_management_form import *
from django.http import Http404, FileResponse
from urllib import parse
from urllib.parse import quote
# from webTools.public.logger import get_logger
from webTools.public.logger import decorator_log
import logging

@decorator_log
def version_management_list(request):
    if request.method == "GET":
        tille = "版本列表"
        form_data = models.VersionManagement.objects.all().order_by("-version_id")
        return render(
            request,
            "web/version_management_list.html",
            {"tille": tille, "ff": form_data},
        )


def version_management_add(request):
    if request.method == "GET":
        forms = VersionManagementAdd()
        tille = "版本添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    elif request.method == "POST":
        print(request.POST)
        form = VersionManagementAdd(data=request.POST)

        if form.is_valid():

            form.save()
            return redirect("/version/management/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})
    else:
        forms = models.SystemEnvironment.objects.all()
        return render(request, "web/version_management_list.html", {"fro": forms})


def version_management_edit(request, nid):
    row_object = models.VersionManagement.objects.filter(version_id=nid).first()
    tille = "版本编辑"
    if request.method == "GET":
        form = VersionManagementAdd(instance=row_object)
        return render(request, "web/chenge.html", {"form": form, "tille": tille})
    else:
        form = VersionManagementAdd(data=request.POST, instance=row_object)

        if form.is_valid():
            form.save()
            return redirect("/version/management/list/")
        else:
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
def version_ts_dow(request,nid):
    if request.method == "GET":
        if models.VersionManagement.objects.filter(version_id=nid).first():
            addrs=models.VersionManagement.objects.get(version_id=nid).download_address
            logger = logging.getLogger("django")
            try:
                BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                storage_path = parse.unquote(
                    os.path.join(
                        os.path.dirname(BASE_DIR),
                        "webTools/data/TS_file/%s"%addrs,
                    )
                )

                logger.info(storage_path)
                response = FileResponse(open(storage_path, "rb"))
                response["content_type"] = "application/octet-stream"
                response["Content-Disposition"] = "attachment; filename={0}".format(
                    quote(addrs)
                )
                return response
            except Exception as e:
                logger.info(e)
                return redirect("/version/management/list/")
        else:
            return redirect("/version/management/list/")


    else:
        return redirect("/request/environment/list/")
