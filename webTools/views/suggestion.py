from io import BytesIO
import os
import logging
from urllib.parse import quote
from urllib import parse


from django.shortcuts import render, redirect
from django.http import  FileResponse
from webTools.public.logger import get_logger

import webTools.models
from webTools.forms.suggestion_form import SuggestionAddFrom, SuggestionEditFrom
from webTools.public.logger import decorator_log
import xlsxwriter
from datetime import datetime

def suggestion_list(request):
    try:
        queryset = webTools.models.Suggestions.objects.all()
        tille = '建议列表'
        return render(request, 'web/suggestion_list.html', {'fro': queryset, 'tille': tille})
    except Exception as e:
        logger = logging.getLogger('django')
        logger.error(e)


def suggestion_add(request):
    logger = logging.getLogger('django')
    try:
        if request.method == "GET":
            forms = SuggestionAddFrom()
            tille = "新建建议"
            return render(request, 'web/chenge.html', {'form': forms, 'tille': tille, })
    except Exception as e:
        logger.error(e)
    try:
        form = SuggestionAddFrom(data=request.POST)
        if form.is_valid():
            # title = form.data["title"]
            form.save()
            return redirect('/suggestion/list/')
        else:
            # 校验失败显示错误信息
            print(form.errors)
            return render(request, 'web/chenge.html', {'form': form})
    except Exception as e:
        logger.error(e)


def suggestion_edit(request, nid):
    logger = logging.getLogger('django')
    try:
        # 根据suggestion_id 查询 所有字段
        row_object = webTools.models.Suggestions.objects.filter(suggest_id=nid).first()
        tille = '修改建议'
        if request.method == "GET":
            # 根据ID去数据库获取要编辑的那一行数据（对象）

            form = SuggestionEditFrom(instance=row_object)
            return render(request, 'web/chenge.html', {'form': form, 'tille': tille})
        else:
            form = SuggestionEditFrom(data=request.POST, instance=row_object)

            if form.is_valid():
                form.save()
                return redirect('/suggestion/list/')
            else:
                return render(request, 'web/chenge.html', {'form': form, 'tille': tille})
    except Exception as e:
        logger.error(e)


def suggestion_delet(request, nid):
    logger = logging.getLogger('django')
    try:
        row_object = webTools.models.Suggestions.objects.filter(suggest_id=nid).first()
        if not row_object:
            return render(request, 'web/suggestion_list.html')
        else:
            webTools.models.Suggestions.objects.filter(suggest_id=nid).delete()
            return redirect("/suggestion/list/")
    except Exception as e:
        logger.error(e)
@decorator_log
def suggestion_download(request):

    if request.method =='GET':

        queryset = webTools.models.Suggestions.objects.all()
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        #设置存储位置
        storage_path = parse.unquote(os.path.join(os.path.dirname(BASE_DIR),
                                                  "webTools/data/up_excl/建议列表.xlsx"))

        workbook = xlsxwriter.Workbook(storage_path)
        worksheet = workbook.add_worksheet()
        #查询数据库数据
        queryset_list=queryset.values_list()
        #写入xlsx第一行
        tilel=['序号','建议ID','所属工具模块','建议描述','提出人','提出时间','状态','处理人','备注']
        tilel_row=0
        tilel_col=0
        for ima in tilel:
            worksheet.write(tilel_row, tilel_col, ima)
            tilel_col =tilel_col+1
        row=1
        col=0
        #写入数据
        for i  in range(len(queryset_list)):
            for ii in queryset_list[i]:
                if col == 0:
                    worksheet.write(row, col, i+1)
                    col = col+1
                elif isinstance(ii    ,datetime) :
                    ii=str(ii)
                worksheet.write(row, col,ii)
                col +=1
            row +=1
            col=0
        workbook.close()
        response = FileResponse(open(storage_path, 'rb'))
        response['content_type'] = "application/octet-stream"
        response['Content-Disposition'] = 'attachment; filename={0}.xlsx'.format(quote("建议优化"))
        return response
    else:
        return redirect('/suggestion/list/')
