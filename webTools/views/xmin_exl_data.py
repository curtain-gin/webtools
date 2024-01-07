import os
import time
from urllib import parse
from urllib.parse import quote
from django.shortcuts import render, redirect, HttpResponse

from django.http import Http404, FileResponse
from webTools.public.export_excel import xw_toExcel
from webTools.public.opreate_xmind_new import main_cases
from webTools.public.logger import decorator_log
from webTools.public.logger import get_logger

import logging


@decorator_log
def xmind_conversion(request):

    # logger = logging.getLogger('django')
    if request.method == "GET":
        get_logger().info("xmind转换")

        excelname = 0
        error = ""
        return render(
            request, "web/xmind_conversion.html", {"file": excelname, "error": error}
        )
    else:
        try:
            XMIND_ERROR = ""
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            files_name = request.FILES.getlist("myfile")[0]
            if str(files_name).endswith(".xmind") != True:

                XMIND_ERROR = "请上传xmind文件"
                return render(
                    request, "web/xmind_conversion.html", {"error": XMIND_ERROR}
                )

            file_obj = request.FILES.get("myfile")
            storage_path = os.path.join(
                os.path.dirname(BASE_DIR), "webTools/data/up_xmind"
            )
            destination = open(os.path.join(storage_path, str(files_name)), "wb+")

            for chunk in file_obj.chunks():

                destination.write(chunk)
            destination.close()

            # 开始对xmind文件进行处理
            t = time.time()
            time.sleep(2)
            stamp = int(round(t * 1000))
            data, namelist, xmind_path = main_cases()
            excelname = "{}{}{}.xlsx".format(namelist[0], " ", stamp)
            result = xw_toExcel(data[0], excelname, xmind_path, namelist[0])
            # 发生错误
            if result == "false":
                XMIND_ERROR = "文件转换错误,请上传正确.xmind文件"
                render(request, "web/xmind_conversion.html", {"error": XMIND_ERROR})
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            storage_path = parse.unquote(
                os.path.join(os.path.dirname(BASE_DIR), "webTools/data/up_excl/%s")
                % excelname
            )
            # logger.info(storage_path)
            response = FileResponse(open(storage_path, "rb"))
            response["content_type"] = "application/octet-stream"
            # response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(storage_path)
            response["Content-Disposition"] = "attachment; filename={0}.xlsx".format(
                quote(excelname)
            )
            return response
        except Exception as e:
            # logger.error(e)
            XMIND_ERROR = "文件转换错误,请上传正确.xmind文件"
            return render(request, "web/xmind_conversion.html", {"error": XMIND_ERROR})


def xmind_to_exl_down(request):
    logger = logging.getLogger("django")
    try:
        if request.method == "GET":
            logger = logging.getLogger("django")

            BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            storage_path = parse.unquote(
                os.path.join(
                    os.path.dirname(BASE_DIR),
                    "webTools/data/up_xmind/xmind_template/xmind模版.xmind",
                )
            )

            logger.info(storage_path)
            response = FileResponse(open(storage_path, "rb"))
            response["content_type"] = "application/octet-stream"
            response["Content-Disposition"] = "attachment; filename={0}.xmind".format(
                quote("xmind模版")
            )

            return response
        else:
            return redirect("/xmind/exl/data/")
    except Exception as e:
        logger.error(e)
