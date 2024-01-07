import os
from urllib import parse
from urllib.parse import quote

import xlsxwriter
from datetime import datetime
from django.http import FileResponse
import logging
from django.shortcuts import render, redirect

from webTools.forms.demand_form import DemandAddFrom, DemandEditFrom
import webTools.models
from webTools.public.logger import decorator_log


def demand_list(request):

    try:

        queryset = webTools.models.Demands.objects.all()
        tille = "需求列表"

        return render(
            request, "web/demand_list.html", {"fro": queryset, "tille": tille}
        )
    except Exception as e:
        logger = logging.getLogger("django")
        logger.error(e)


def demand_add(request):
    logger = logging.getLogger("django")
    try:
        if request.method == "GET":
            forms = DemandAddFrom()
            tille = "添加需求"
            return render(
                request,
                "web/chenge.html",
                {
                    "form": forms,
                    "tille": tille,
                },
            )
    except Exception as e:
        logger.error(e)
    try:
        form = DemandAddFrom(data=request.POST)
        if form.is_valid():
            # title = form.data["title"]
            form.save()
            return redirect("/demand/list/")
        else:
            # 校验失败显示错误信息
            print(form.errors)
            return render(request, "web/chenge.html", {"form": form})
    except Exception as e:
        logger.error(e)


def demand_edit(request, nid):
    logger = logging.getLogger("django")
    try:
        # 根据demand_id 查询 所有字段
        row_object = webTools.models.Demands.objects.filter(demand_id=nid).first()
        tille = "更新需求"
        if request.method == "GET":
            # 根据ID去数据库获取要编辑的那一行数据（对象）

            form = DemandEditFrom(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        else:
            form = DemandEditFrom(data=request.POST, instance=row_object)

            if form.is_valid():
                form.save()
                return redirect("/demand/list/")
            else:
                return render(
                    request, "web/chenge.html", {"form": form, "tille": tille}
                )
    except Exception as e:
        logger.error(e)


def demand_delet(request, nid):
    logger = logging.getLogger("django")
    try:
        row_object = webTools.models.Demands.objects.filter(demand_id=nid).first()
        if not row_object:
            return render(request, "web/demand_list.html")
        else:
            webTools.models.Demands.objects.filter(demand_id=nid).delete()
            return redirect("/demand/list/")
    except Exception as e:
        logger.error(e)


@decorator_log
def demand_download(request):

    if request.method == "GET":

        queryset = webTools.models.Demands.objects.all()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # 设置存储位置
        storage_path = parse.unquote(
            os.path.join(os.path.dirname(BASE_DIR), "webTools/data/up_excl/需求列表.xlsx")
        )

        workbook = xlsxwriter.Workbook(storage_path)
        worksheet = workbook.add_worksheet()
        # 查询数据库数据
        queryset_list = queryset.values_list()
        # 写入xlsx第一行
        tilel = [
            "序号",
            "需求ID",
            "需求描述",
            "详细说明",
            "提出人",
            "提出时间",
            "状态",
            "处理人",
            "备注",
        ]
        tilel_row = 0
        tilel_col = 0
        for ima in tilel:
            worksheet.write(tilel_row, tilel_col, ima)
            tilel_col = tilel_col + 1
        row = 1
        col = 0
        # 写入数据
        for i in range(len(queryset_list)):
            for ii in queryset_list[i]:
                if col == 0:
                    worksheet.write(row, col, i + 1)
                    col = col + 1
                elif isinstance(ii, datetime):
                    ii = str(ii)
                worksheet.write(row, col, ii)
                col += 1
            row += 1
            col = 0
        workbook.close()
        response = FileResponse(open(storage_path, "rb"))
        response["content_type"] = "application/octet-stream"
        response["Content-Disposition"] = "attachment; filename={0}.xlsx".format(
            quote("需求汇总")
        )
        return response
    else:
        return redirect("/demand/list/")
