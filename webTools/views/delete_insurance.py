import re
from django.shortcuts import render, redirect, HttpResponse
from webTools.public.daba_tuple_to_dict import execute_query, other_query
from decimal import Decimal

# import logging
#
# logger = logging.getLogger('django')
from webTools.public.logger import get_logger


def insurance_list(request):
    tille = "非赠险单删除"
    if request.method == "GET":
        return render(request, "web/delete_insurance.html", {"tille": tille})
    else:
        response_dict = request.POST.dict()
        env_num = response_dict["select_environment"]
        if response_dict["phone_number"] == "":
            return render(request, "web/delete_insurance.html", {"msg": "手机号不能为空！"})
        else:
            if (
                response_dict["product_name"] == ""
                and response_dict["product_id"] == ""
            ):
                return render(
                    request, "web/delete_insurance.html", {"msg": "产品名称和产品id至少一个条件不为空！"}
                )

            else:
                sql = (
                    "b.del_flag = 0 and a.del_flag=0 and b.phone_number = '{}'".format(
                        response_dict["phone_number"]
                    )
                )
                if response_dict["is_online"] == "yes":
                    sql = '{} and  a.inner_order_source IN  ("wechatPreH5","wechatPreH5Sms") '.format(
                        sql
                    )
                else:
                    sql = sql
                for i in response_dict:
                    if i not in [
                        "select_environment",
                        "csrfmiddlewaretoken",
                        "is_online",
                        "phone_number",
                    ]:
                        if response_dict[i]:
                            if i == "product_name":

                                sql = '{} and a.{} like "%{}%"'.format(
                                    sql, i, response_dict[i]
                                )
                            else:
                                sql = '{} and a.{}="{}"'.format(
                                    sql, i, response_dict[i]
                                )
                        else:
                            sql = sql
                    else:
                        sql = sql

                try:
                    mysql = "select a.order_id,a.order_status,a.pay_status,a.prem_turnin_status,a.inner_order_source,b.phone_number,a.product_id, a.product_name,a.create_date from zkr_ins_product.order_base a left join zkr_ins_product.order_policy_holder b on a.order_id=b.order_id  where {} ".format(
                        sql
                    )
                    print(mysql)
                    result = execute_query(env_num, mysql)
                    for i in range(len(result)):
                        result[i]["env"] = env_num
                    return render(
                        request,
                        "web/delete_insurance.html",
                        {"pp": result, "tille": tille},
                    )
                except Exception as e:
                    get_logger().error(e)
                    return render(
                        request, "web/delete_insurance.html", {"tille": tille}
                    )


def insurance_delet(request, nid1, env):
    tille = "非赠险单删除"
    try:
        sql1 = 'update zkr_ins_product.order_new_covenant set del_flag=1  where order_id  ="{}"'.format(
            nid1
        )
        sql2 = 'update zkr_ins_product.order_policy_holder set del_flag=1  where order_id  ="{}"'.format(
            nid1
        )
        sql3 = 'update zkr_ins_product.order_insured set del_flag=1  where order_id  ="{}"'.format(
            nid1
        )
        sql4 = 'update zkr_ins_product.order_base set del_flag=1  where order_id  ="{}"'.format(
            nid1
        )
        sql5 = 'update zkr_ins_product.order_property set del_flag=1  where order_id  ="{}"'.format(
            nid1
        )

        other_query(env, sql1)
        other_query(env, sql2)
        other_query(env, sql3)
        other_query(env, sql4)
        other_query(env, sql5)

        request_date = []
        ooooo = {
            "sql": sql1,
            "sql": sql2,
            "sql": sql3,
            "sql": sql4,
            "sql": sql5,
        }

        request_date.append(ooooo)
        # return render(request, 'web/delete_premium_insurance.html', {
        #     'msg': '删除成功'
        # })
        return redirect("/insurance/list/", {"msg": "删除成功"})
    except Exception as e:
        get_logger().error(e)

        return render(request, "web/delete_insurance.html", {"tille": tille})
