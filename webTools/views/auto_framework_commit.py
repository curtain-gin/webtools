#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *********************************************************
# @@ScriptName:
# @@Author: 周雅
# @@Create Date: 
# @@Modify Date: 
# @@Description: 汇总自动化脚本提交信息，包括提交分支，路径，文件等
# *********************************************************
import logging
from django.shortcuts import render, redirect
from webTools.forms.case_form import CaseAddFrom, CaseEditFrom
import webTools.models


def case_list(request):
    try:

        queryset = webTools.models.Cases.objects.all()
        tille = '提交列表'

        return render(request, 'web/case_list.html', {'fro': queryset, 'tille': tille})
    except Exception as e:
        logger = logging.getLogger('django')
        logger.error(e)


def case_add(request):
    logger = logging.getLogger('django')
    try:
        if request.method == "GET":
            forms = CaseAddFrom()
            tille = "添加脚本提交记录"
            return render(request, 'web/chenge.html', {'form': forms, 'tille': tille, })
    except Exception as e:
        logger.error(e)
    try:
        form = CaseAddFrom(data=request.POST)
        if form.is_valid():
            # title = form.data["title"]
            form.save()
            return redirect('/case/list/')
        else:
            # 校验失败显示错误信息
            print(form.errors)
            return render(request, 'web/chenge.html', {'form': form})
    except Exception as e:
        logger.error(e)


def case_edit(request, nid):
    logger = logging.getLogger('django')
    try:
        # 根据demand_id 查询 所有字段
        row_object = webTools.models.Cases.objects.filter(case_id=nid).first()
        tille = '更新'
        if request.method == "GET":
            # 根据ID去数据库获取要编辑的那一行数据（对象）

            form = CaseEditFrom(instance=row_object)
            return render(request, 'web/chenge.html', {'form': form, 'tille': tille})
        else:
            form = CaseEditFrom(data=request.POST, instance=row_object)

            if form.is_valid():
                form.save()
                return redirect('/case/list/')
            else:
                return render(request, 'web/chenge.html', {'form': form, 'tille': tille})
    except Exception as e:
        logger.error(e)


def case_delet(request, nid):
    logger = logging.getLogger('django')
    try:
        row_object = webTools.models.Cases.objects.filter(case_id=nid).first()
        if not row_object:
            return render(request, 'web/case_list.html')
        else:
            webTools.models.Cases.objects.filter(case_id=nid).delete()
            return redirect("/case/list/")
    except Exception as e:
        logger.error(e)
