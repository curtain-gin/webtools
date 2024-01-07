from django.shortcuts import render, redirect, HttpResponse

from webTools.forms.user_permission import *


def user_permission_role_list(request):
    user_role = models.Role.objects.all()

    return render(request, "web/user_permission_role.html", {"fro": user_role})


def user_permission_role_add(request):

    if request.method == "GET":
        forms = PermissionAdd()
        tille = "角色添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )

    form = PermissionAdd(data=request.POST)

    if form.is_valid():

        form.save()
        return redirect("/permission/list/")

    else:
        # 校验失败显示错误信息
        # print(form.errors)

        return render(request, "web/chenge.html", {"form": form})


def user_permission_role_edit(request, nid):
    row_object = models.Role.objects.filter(role_id=nid).first()

    if request.method == "GET":
        # 根据ID去数据库获取要编辑的那一行数据（对象）
        form = PermissionEdit(instance=row_object)
        return render(request, "web/chenge.html", {"form": form})

    form = PermissionEdit(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/permission/list/")
    else:

        return render(request, "web/chenge.html", {"form": form})


def user_permission_role_delet(request, nid):
    row_object = models.Role.objects.filter(role_id=nid).first()
    if not row_object:
        return render(request, "web/user_permission_role.html")
    models.Role.objects.filter(role_id=nid).delete()
    return redirect("/permission/list/")
