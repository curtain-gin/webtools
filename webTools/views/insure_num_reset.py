#!/usr/bin/env python
# -*- coding:utf-8 -*-
# *********************************************************
# @@ScriptName:
# @@Author: 周雅
# @@Create Date:
# @@Modify Date:
# @@Description:
# *********************************************************
from django.http import HttpResponseRedirect
from django.shortcuts import render

from webTools.public.daba_tuple_to_dict import other_query
import logging

logger = logging.getLogger("django")


def insure_num_reset(request):
    tille = "投保次数重置"
    try:
        if request.method == "GET":
            return render(request, "web/insure_num_reset.html")
        else:
            response_dict = request.POST.dict()
            print(response_dict)
            if response_dict["phone"] == "" and response_dict["user_id"] == "":
                """手机号和user_id都为空"""
                # return render(request, 'web/insure_num_reset.html', {'tille': tille})
                return render(
                    request, "web/insure_num_reset.html", {"msg": "手机号和user_id至少一个不为空！"}
                )

            elif response_dict["phone"] != "" and response_dict["user_id"] == "":
                logger.info("zhiyoushoujihao")
                member_phone = response_dict["phone"]

                env_num = response_dict["select_environment"]
                try:
                    sql = (
                        """
                               update zkr_ins_product.insure_number_record set order_number=0 , updated_by='auto' where  phone = %s  AND is_deleted =0
                               """
                        % member_phone
                    )
                    logger.info(sql, env_num)
                    result = other_query(env_num, sql)
                    for i in range(len(result)):
                        result[i]["env"] = env_num
                    # return render(request, 'web/insure_num_reset.html', {"pp": "重置成功", 'tille': tille})
                    return render(request, "web/insure_num_reset.html", {"msg": "执行成功"})
                except Exception as e:
                    logger.error(e)
                    return render(
                        request,
                        "web/insure_num_reset.html",
                        {"msg": "投保次数重置失败，请检查传参并重试"},
                    )

            elif response_dict["phone"] == "" and response_dict["user_id"] != "":
                userid = response_dict["user_id"]

                env_num = response_dict["select_environment"]
                try:
                    sql = (
                        """
                               update zkr_ins_product.insure_number_record set order_number=0 , updated_by='auto' where user_id = %s   AND is_deleted =0
                               """
                        % userid
                    )
                    logger.info(sql, env_num)
                    result = other_query(env_num, sql)
                    for i in range(len(result)):
                        result[i]["env"] = env_num
                    # return render(request, 'web/insure_num_reset.html', {"pp": "重置成功", 'tille': tille})
                    return render(request, "web/insure_num_reset.html", {"msg": "执行成功"})
                except Exception as e:
                    logger.error(e)
                    return render(
                        request,
                        "web/insure_num_reset.html",
                        {"msg": "投保次数重置失败，请检查传参并重试"},
                    )

            else:
                logger.info("lianggedouyou")
                userid = response_dict["user_id"]
                phone = response_dict["phone"]
                env_num = response_dict["select_environment"]
                try:
                    sql = 'update zkr_ins_product.insure_number_record set order_number=0 , updated_by="auto" where phone ="{}" and user_id = "{}"   AND is_deleted =0'.format(
                        phone, userid
                    )
                    logger.info(sql, env_num)
                    result = other_query(env_num, sql)
                    for i in range(len(result)):
                        result[i]["env"] = env_num
                    return render(request, "web/insure_num_reset.html", {"msg": "执行成功"})
                except Exception as e:
                    logger.error(e)
                    return render(
                        request,
                        "web/insure_num_reset.html",
                        {"msg": "投保次数重置失败，请检查传参并重试"},
                    )

    except Exception as e:
        logger.error(e)
    return render(request, "web/insure_num_reset.html", {"tille": tille})
