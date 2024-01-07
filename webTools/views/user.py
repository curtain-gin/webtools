from io import BytesIO

import logging
from django.shortcuts import render, redirect, HttpResponse

from webTools.forms.user_form import *
from webTools.public.encrypt import md5
from webTools.public.code import check_code


def user_login(request):
    "用户登录"
    logger = logging.getLogger("django")
    try:
        if request.method == ("GET"):
            fro = LoginModelFrom()
            return render(request, "web/user_login.html", {"fro": fro})
        else:
            form = LoginModelFrom(data=request.POST)

            # 进行校验
            if form.is_valid():

                # user_input_code=form.data["code"]
                mobile_phone = form.data["mobile_phone"]
                password = md5(form.data["password"])

                sdf = models.UserAppInfo.objects.filter(
                    mobile_phone=mobile_phone, password=password
                ).first()

                # session验证码校验
                # session_image_code = request.session.get('image_code', '')
                # if not session_image_code :
                #     form.add_error('code', '请重新刷新页面获得验证码')
                # else:
                # session
                #
                # if user_input_code.upper()=='123456':
                #     # print(user_input_code)
                #     pass
                # session
                # elif session_image_code.upper() != user_input_code.upper():
                #         form.add_error('code', '验证码错误')
                #         return render(request, 'web/user_login.html', {'fro': form})

                # 手机号密码校验

                if not sdf:
                    print(2)
                    form.add_error("mobile_phone", "手机号错误")
                    form.add_error("password", "密码错误")
                    return render(request, "web/user_login.html", {"fro": form})

                request.session["info"] = form.data
                request.session.set_expiry(60 * 60 * 24)
                print(request.session["info"])
                return redirect("/index/")
            return render(request, "web/user_login.html", {"fro": form})
    except Exception as e:
        logger.error(e)


def image_code(request):
    img, code_sting = check_code()
    # session方法code 时间
    request.session["image_code"] = code_sting
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, "png")
    return HttpResponse(stream.getvalue())


def user_list(request):

    # 获得CSRF token
    try:

        queryset = models.UserAppInfo.objects.all()
        tille = "用户列表"

        return render(request, "web/user_list.html", {"fro": queryset, "tille": tille})
    except Exception as e:
        logger = logging.getLogger("django")
        logger.error(e)


def user_add(request):
    logger = logging.getLogger("django")
    try:
        if request.method == "GET":
            forms = UserAddFrom()
            tille = "用户添加"
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
        form = UserAddFrom(data=request.POST)
        if form.is_valid():
            mobile_phone = form.data["mobile_phone"]
            sdf = models.UserAppInfo.objects.filter(mobile_phone=mobile_phone).first()
            if not sdf:
                # 如果数据合法，保存到数据库
                form.save()
                return redirect("/user/list/")
            else:
                form.add_error("mobile_phone", "手机号已存在")
                return render(request, "web/chenge.html", {"form": form})
        else:
            # 校验失败显示错误信息
            # print(form.errors)

            return render(request, "web/chenge.html", {"form": form})
    except Exception as e:
        logger.error(e)


def user_edit(request, nid):
    logger = logging.getLogger("django")
    try:
        # 根据user_id 查询 username，手机号
        oo_mobile_phone = models.UserAppInfo.objects.get(user_id=nid).mobile_phone
        row_object = models.UserAppInfo.objects.filter(user_id=nid).first()
        tille = "修改用户信息"
        if request.method == "GET":
            # 根据ID去数据库获取要编辑的那一行数据（对象）

            form = UserEditFrom(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        else:
            form = UserEditFrom(data=request.POST, instance=row_object)

            if form.is_valid():
                # 请求参数
                mobile_phone_form = form.data["mobile_phone"]
                # 数据库数据
                get_item = models.UserAppInfo.objects.filter(
                    mobile_phone=mobile_phone_form
                ).first()

                if not get_item:
                    form.save()
                    return redirect("/user/list/")

                elif oo_mobile_phone == mobile_phone_form:

                    form.save()
                    return redirect("/user/list/")
                else:
                    form.add_error("mobile_phone", "手机号已存在")

                    return render(
                        request, "web/chenge.html", {"form": form, "tille": tille}
                    )

            return render(request, "web/chenge.html", {"form": form, "tille": tille})
    except Exception as e:
        logger.error(e)


def user_delet(request, nid):
    logger = logging.getLogger("django")
    try:
        row_object = models.UserAppInfo.objects.filter(user_id=nid).first()
        if not row_object:
            return render(request, "web/user_list.html")
        else:
            models.UserAppInfo.objects.filter(user_id=nid).delete()
            return redirect("/user/list/")
    except Exception as e:
        logger.error(e)


def user_logout(request):
    logger = logging.getLogger("django")
    try:
        request.session.clear()
        return redirect("/user/login/")
    except Exception as e:
        logger.error(e)


def user_revise(request, nid):
    logger = logging.getLogger("django")
    try:
        row_object = models.UserAppInfo.objects.filter(mobile_phone=nid).first()

        if request.method == "GET":
            tille = "修改个人密码"
            form = UserRevise(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        else:
            form = UserRevise(data=request.POST, instance=row_object)
            if form.is_valid():
                form.save()
                return redirect("/index/")
            else:

                return render(request, "web/chenge.html", {"form": form})

    except Exception as e:
        logger.error(e)
