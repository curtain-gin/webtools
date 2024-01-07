from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.log_form import *

# from webTools.public.logger import get_logger


def log_normal(requerst):

    try:

        data = models.OpLogs.objects.all().order_by("-re_time")[0:5000]
        tile = "正常日志"
    except Exception as e:
        print(e)
        # get_logger().error(e)
    return render(requerst, "web/user_log.html", {"fro": data, "tille": tile})


def log_out(requerst):

    try:
        data = models.AccessTimeOutLogs.objects.all().order_by("-re_time")[0:500]
        tile = "超时日志"
    except Exception as e:
        print(e)
        # get_logger().error(e)
    return render(requerst, "web/user_log.html", {"fro": data, "tille": tile})
