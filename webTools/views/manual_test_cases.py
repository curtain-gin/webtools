from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.manual_test_cases_form import *
import requests
from webTools.public.logger import decorator_log
from webTools.public.is_json import JsonBUF
from webTools.public.logger import get_logger
from webTools.public.story_case_test import Story_Test
from webTools.public.wthfef.login_processing import LoginProcessing
import json

def list_of_manual_test_cases(request):
    forms = models.ManualTestCases.objects.all().order_by("-manual_test_cases_id")

    return render(request, "web/list_of_manual_test_cases.html", {"fro": forms})


def list_of_manual_test_cases_add(request):
    if request.method == "GET":
        forms = ManualTestCasesAddForm()

        tille = "测试用例添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    else:
        form = ManualTestCasesAddForm(data=request.POST)
        if form.is_valid():
            form.instance.creat_user = request.session["info"]["mobile_phone"]
            form.save()
            return redirect("/list/of/manual/test/cases/")
        else:
            return render(request, "web/chenge.html", {"form": form})


@decorator_log
def list_of_manual_test_cases_edit(request, nid):
    row_object = models.ManualTestCases.objects.filter(manual_test_cases_id=nid).first()
    if request.method == "GET":

        tille = "测试用例修改"
        form = ManualTestCasesAddForm(instance=row_object)
        return render(request, "web/chenge.html", {"form": form, "tille": tille})
    else:
        form = ManualTestCasesAddForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/list/of/manual/test/cases/")
        else:
            return render(request, "web/chenge.html", {"form": form})


@decorator_log
def list_of_manual_test_cases_delet(request, nid):
    row_object = models.ManualTestCases.objects.filter(manual_test_cases_id=nid).first()
    if not row_object:
        return render(request, "web/list_of_manual_test_cases.html")
    else:
        models.ManualTestCases.objects.filter(manual_test_cases_id=nid).delete()
        return redirect("/list/of/manual/test/cases/")


def list_of_manual_test_cases_run(request, nid):
    if request.method == "GET":
        sql_data = models.ManualTestCases.objects.get(manual_test_cases_id=nid)
        reqeust_url = sql_data.request_url
        handerss = sql_data.environment_id.environment_hander
        environment_url = sql_data.environment_id.environment_url
        request_parameters = sql_data.request_parameters
        url = environment_url + reqeust_url[1:]
        Extract_the_response_value = sql_data.Extract_the_response_value
        request_method = sql_data.request_method
        handerss = eval(handerss)
        print(environment_url)
        log_dat=LoginProcessing(environment_url)
        request_cookies=log_dat.run_request()
        if "huisuxitong" in  request_cookies.keys():
            handerss["Cookie"]=request_cookies["huisuxitong"]
        elif "waihuzhanghao" in request_cookies.keys():
            handerss["Cookie"]= request_cookies['waihuzhanghao']
        print(request_cookies)
        print(handerss)
        Verify_the_response_value = sql_data.Verify_the_response_value
        print(eval(request_parameters))
        if request_method == 0:
            test_case_reponse = requests.get(
                url=url, headers=handerss,
                json=eval(request_parameters),
                
                )


        else:
            print(url)
            test_case_reponse = requests.post(
                url=url, headers=handerss,
                json=eval(request_parameters),
            
            )
            print(test_case_reponse.text)
        json_f_or_t = JsonBUF.iso_json(test_case_reponse.text)
        print(test_case_reponse.text)
        if Extract_the_response_value == "" and json_f_or_t is True:

            models.ManualTestCases.objects.filter(manual_test_cases_id=nid).update(
                run_the_result=1, response_parameters=test_case_reponse.text
            )
            return redirect("/list/of/manual/test/cases/")
        elif json_f_or_t is False:
            models.ManualTestCases.objects.filter(manual_test_cases_id=nid).update(
                run_the_result=2, response_parameters=test_case_reponse.text
            )
            return redirect("/list/of/manual/test/cases/")
        else:
            resuitr = Story_Test.test_case_validation_results(test_case_reponse=test_case_reponse,
                                                              extract_the_response_value=Extract_the_response_value,
                                                              verify_the_response_value=Verify_the_response_value,
                                                              is_customize_the_function=0)


            if resuitr[0] == resuitr[1] - 1:
                models.ManualTestCases.objects.filter(manual_test_cases_id=nid).update(
                    run_the_result=1, response_parameters=test_case_reponse.text
                )

            else:

                models.ManualTestCases.objects.filter(manual_test_cases_id=nid).update(
                    run_the_result=2, response_parameters=test_case_reponse.text
                )
            return redirect("/list/of/manual/test/cases/")
    else:
        return redirect("/list/of/manual/test/cases/")


@decorator_log
def list_of_manual_test_cases_log(request, nid):
    if request.method == "GET":
        reponse_data = models.ManualTestCases.objects.filter(
            manual_test_cases_id=nid
        ).first()
        return render(
            request, "web/list_of_manual_test_cases_log.html", {"data": reponse_data}
        )
    else:
        reponse_data = models.ManualTestCases.objects.filter(
            manual_test_cases_id=nid
        ).first()
        return render(
            request, "web/list_of_manual_test_cases_log.html", {"data": reponse_data}
        )


def manual_test_disassociate_task_set(request,nid):
    """
    取消所有关联测试集
    """
    pass
