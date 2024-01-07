import logging
from django.shortcuts import render, redirect, HttpResponse

from webTools.forms.user_permission_path import *


def permission_path_list(request):
    logger = logging.getLogger("django")
    try:
        """权限路径列表"""
        permission_path = models.PermissionPath.objects.all()
        return render(
            request, "web/user_permission_path.html", {"fro": permission_path}
        )
    except Exception as e:
        logger.error(e)


def permission_path_add(request):
    logger = logging.getLogger("dango")
    try:
        """权限路径添加"""
        if request.method == "GET":
            forms = PermissionPathAdd()
            tille = "功能添加"

            return render(
                request,
                "web/chenge.html",
                {
                    "form": forms,
                    "tille": tille,
                },
            )
        else:
            form = PermissionPathAdd(data=request.POST)

            if form.is_valid():

                form.save()
                return redirect("/permission/path/list/")

            else:
                # 校验失败显示错误信息
                # print(form.errors)

                return render(request, "web/chenge.html", {"form": form})
    except Exception as e:
        logger.error(e)


def permission_path_edit(request, nid):
    """编辑权限路径"""
    logger = logging.getLogger("django")
    try:
        # 根据user_id 查询
        row_object = models.PermissionPath.objects.filter(
            permission_path_id=nid
        ).first()

        if request.method == "GET":
            tille = "修改个人信息"
            # 根据ID去数据库获取要编辑的那一行数据（对象）
            form = PermissionPathAdd(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        else:

            form = PermissionPathedit(data=request.POST, instance=row_object)
            # 校验输入数据
            if form.is_valid():
                form.save()
                return redirect("/permission/path/list/")
            else:
                tille = "修改个人信息"

                return render(
                    request, "web/chenge.html", {"form": form, "tille": tille}
                )
    except Exception as e:
        logger.error(e)


def user_permission_path_delet(request, nid):
    """功能权限路径删除"""
    logger = logging.getLogger("django")
    try:
        row_object = models.PermissionPath.objects.filter(
            permission_path_id=nid
        ).first()
        if not row_object:
            return render(request, "web/user_permission_path.html")
        models.PermissionPath.objects.filter(permission_path_id=nid).delete()
        return redirect("/permission/path/list/")
    except Exception as e:
        logger.error(e)


def user_permission_path_info(request):
    """权限路径页面"""
    return render(request, "web/permission_info.html")
