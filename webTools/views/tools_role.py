from django.shortcuts import render, redirect, HttpResponse
from webTools.public.logger import decorator_log
from webTools.public.logger import get_logger
from webTools.public.daba_tuple_to_dict import execute_query, other_query


@decorator_log
def prduct_library_select(request):
    """产品库授权检查表 查询数据"""
    if request.method == "GET":
        return render(request, "web/product_library_select.html")
    else:
        get_logger().info("进入产品库查询")
        response_dict = request.POST.dict()
        env_num = response_dict["select_environment"]
        sql = """
            SELECT * FROM `zkr_ins_product`.`authorization_check` LIMIT 0,1000

            """
        result = execute_query(env_num, sql)
        for i in range(len(result)):
            result[i]["env"] = env_num
        return render(request, "web/product_library_select.html", {"pp": result})
