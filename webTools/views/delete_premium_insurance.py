import re
from django.shortcuts import render, redirect, HttpResponse
from webTools.public.daba_tuple_to_dict import execute_query, other_query
from decimal import Decimal

# import logging
#
# logger = logging.getLogger('django')
from webTools.public.logger import get_logger


def premium_insurance_list(request):
    tille = "赠险单删除"
    if request.method == "GET":
        return render(request, "web/delete_premium_insurance.html", {"tille": tille})
    else:
        response_dict = request.POST.dict()
        print(response_dict)
        if (
            response_dict["appnt_mobile"] == ""
            and response_dict["product_name"] == ""
            and response_dict["product_id"] == ""
        ):
            return render(
                request, "web/delete_premium_insurance.html", {"msg": "至少一个条件不为空！"}
            )

        else:
            sql = "del_flag=0"
            for i in response_dict:
                if i not in ["select_environment", "csrfmiddlewaretoken"]:
                    if response_dict[i]:
                        if i == "product_name":

                            sql = '{} and {} like "%{}%"'.format(
                                sql, i, response_dict[i]
                            )
                        else:
                            sql = '{} and {}="{}"'.format(sql, i, response_dict[i])
                    else:
                        sql = sql
                else:
                    sql = sql
            try:
                mysql = "SELECT * FROM zkr_ins_product.order_presenter WHERE {} order by create_date desc limit 100 ".format(
                    sql
                )
                get_logger().info(mysql)
                env_num = response_dict["select_environment"]
                result = execute_query(env_num, mysql)
                for i in range(len(result)):
                    result[i]["env"] = env_num
                return render(
                    request,
                    "web/delete_premium_insurance.html",
                    {"pp": result, "tille": tille},
                )
            except Exception as e:
                get_logger().error(e)
                return render(
                    request, "web/delete_premium_insurance.html", {"tille": tille}
                )


def premium_insurance_delet(request, nid1, env, nid2=""):
    tille = "赠险单删除"
    try:
        sql = 'UPDATE zkr_ins_product.order_presenter SET del_flag = 1 where order_id="{}" and policy_no="{}" '.format(
            nid1, nid2
        )
        print("sql:", sql)
        other_query(env, sql)
        request_date = []
        ooooo = {"sql": sql}

        request_date.append(ooooo)
        # return render(request, 'web/delete_premium_insurance.html', {
        #     'msg': '删除成功'
        # })
        return redirect("/premium/insurance/list/", {"msg": "删除成功"})
    except Exception as e:
        get_logger().error(e)
        return render(request, "web/delete_premium_insurance.html", {"tille": tille})
