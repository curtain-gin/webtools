import random
import time
import json
from django.shortcuts import render
from webTools.public.identity import IdNumber
from webTools.public.logger import decorator_log
from webTools.forms.order_data_form import *
from datetime import datetime, timedelta
from webTools.public.daba_tuple_to_dict import execute_query


@decorator_log
def order_data_generation(request):
    """订单基础数据生成"""
    if request.method == "GET":
        fro = OrderDataFrom()
        tille = "除年龄外有一个输入框未填写或者填写错误，默认生成100条杭州地区，年月日19980101数据"
        return render(
            request, "web/order_data_generation.html", {"pp": fro, "tille": tille}
        )

    else:
        form = OrderDataFrom(data=request.POST)
        city_ord = form.data["city_ord"]
        year_ord = form.data["year_ord"]
        age_ord = form.data["age_ord"]
        num_ord = form.data["num_ord"]
        # 进行校验
        if form.is_valid():
            if age_ord != "" and year_ord == "":

                random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
                reques_data = []
                loc_year = int(time.strftime("%Y", time.localtime(time.time())))
                random_month = random.randint(1, 12)
                random_day = random.randint(1, 29)
                ord_y = loc_year - int(age_ord)
                ls = str(ord_y) + str(random_month) + str(random_day)
                for i in range(int(num_ord)):
                    user_num = IdNumber.generate_id(
                        random_sex, idd_year=ls, id_city=city_ord
                    )

                    name = IdNumber.random_name()
                    addres = (
                        IdNumber(user_num).get_area_name() + name + name + name + name
                    )

                    ooo_dict = {"fenzheng": user_num, "addres": addres, "name": name}
                    reques_data.append(ooo_dict)
                return render(
                    request,
                    "web/order_data_generation.html",
                    {"order_data": reques_data, "pp": form},
                )

            elif age_ord == "" and year_ord != "":

                try:
                    dat = datetime.strptime("%s" % year_ord, "%Y%m%d")
                    year_ord = datetime.strftime(dat + timedelta(), "%Y%m%d")

                    random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
                    reques_data = []
                    for i in range(int(num_ord)):
                        user_num = IdNumber.generate_id(
                            random_sex, idd_year=year_ord, id_city=city_ord
                        )

                        name = IdNumber.random_name()
                        addres = (
                            IdNumber(user_num).get_area_name()
                            + name
                            + name
                            + name
                            + name
                        )

                        ooo_dict = {
                            "fenzheng": user_num,
                            "addres": addres,
                            "name": name,
                        }
                        reques_data.append(ooo_dict)
                    return render(
                        request,
                        "web/order_data_generation.html",
                        {
                            "order_data": reques_data,
                            "pp": form,
                        },
                    )
                except:
                    form.add_error("year_ord", "请填写正确年月日 例如19880101")
                    return render(
                        request,
                        "web/order_data_generation.html",
                        {
                            "pp": form,
                        },
                    )

            else:
                form.add_error("age_ord", "请填写正确年龄， 不能同时填写年龄和年份")
                form.add_error("year_ord", "请填写正确年月日 例如19880101，不能同时填写年龄和年份")

                return render(
                    request,
                    "web/order_data_generation.html",
                    {
                        "pp": form,
                    },
                )

        else:
            if age_ord == "" and year_ord == "":
                form.add_error("age_ord", "年龄不能为空")
                form.add_error("year_ord", "请填写正确年月日 例如19880101")
            elif age_ord == "":
                form.add_error("age_ord", "年龄不能为空")
            elif year_ord == "":
                form.add_error("year_ord", "请填写正确年月日 例如19880101")
            tille = "除年龄外有一个输入框未填写或者填写错误，默认生成100条杭州地区，年月日19980101数据"
            random_sex = random.randint(0, 1)  # 随机生成男(1)或女(0)
            reques_data = []
            for i in range(100):
                user_num = IdNumber.generate_id(random_sex)
                name = IdNumber.random_name()
                addres = IdNumber(user_num).get_area_name() + name + name + name + name

                ooo_dict = {"fenzheng": user_num, "addres": addres, "name": name}
                reques_data.append(ooo_dict)
            return render(
                request,
                "web/order_data_generation.html",
                {"order_data": reques_data, "pp": form, "tille": tille},
            )
def json_parse(request):
    return render(request,"web/json_parse.html")


def sql_inquire(request):
    if request.method == "GET":
        return render(request, "web/sql_data.html")
    else:
        response_dict = request.POST.dict()
        select_environment=response_dict['select_environment']
        sql_data=response_dict['sql_data']
        env_num = "default"

        result = execute_query(env_num,sql_data)
        ddda = json.dumps(str(result))

        ddp_list=[]
        ddpd_list=[]
        for i in result[0]:

            ddp_list.append(i)
        for ii in range(len(result)):
            ddf=[]
            for iii,vvv in result[ii].items():
                ddf.append(vvv )

            ddpd_list.append(ddf)
        print(ddpd_list)



        return render(request, "web/sql_data.html",{"dd":ddpd_list, "oo": ddp_list})