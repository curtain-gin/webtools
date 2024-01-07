import pickle
import json
import datetime
import time
import random
import requests
from webTools.public.is_json import JsonBUF
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from webTools.public.logger import get_logger
from webTools.public.daba_tuple_to_dict import execute_query
from webTools.forms.test_set_tasks_add_form import *

from django.shortcuts import render, redirect, HttpResponse
from webTools.public.swagger_data_processing import DataProcessing
from webTools.public.story_case_test import Story_Test


def test_set_tasks_list(request):
    data = models.Test_Set_Tasks.objects.all()
    tille = '测试集任务列表'
    return render(
        request, "web/test_set_tasks_list.html", {"data": data, "tille": tille}
    )


def test_set_tasks_add(request):
    if request.method == "GET":
        forms = TestTasksAdd()
        tille = "测试集任务添加"
        return render(
            request,
            "web/chenge.html",
            {
                "form": forms,
                "tille": tille,
            },
        )
    elif request.method == "POST":
        form = TestTasksAdd(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/test/set/tasks/list/")
        else:
            return render(request, "web/chenge.html", {"form": form})

    else:
        forms = models.Test_Set_Tasks.objects.all()
        return render(request, "web/test_set_tasks_list.html", {"data": forms})


def test_set_tasks_edit(request, nid):
    row_object = models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid).first()
    tille = "测试任务编辑"
    if request.method == "GET":
        form = TestTasksAdd(instance=row_object)
        return render(request, "web/chenge.html", {"form": form, "tille": tille})
    else:
        form = TestTasksAdd(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect("/test/set/tasks/list/")
        else:
            return render(request, "web/chenge.html", {"form": form, "tille": tille})


def test_set_tasks_run(request, nid):
    loc_time = time.strftime("%Y %a %b %d %H:%M:%S ", time.localtime())
    test_report_name = loc_time + "TestReport"
    test_reports = models.Test_Reports.objects.create(test_report_name=test_report_name,
                                                      test_report_cases=nid)
    fh = models.Test_Reports.objects.filter(test_report_name=test_report_name).values()
    test_report_id = fh[0]['test_report_id']


    tasks_set_data=models.ManualTestCases.objects.filter(test_set_tasks=nid).values()
    print("初始数据%s"%tasks_set_data)
    print("初始数据长度%s"%len(tasks_set_data))
    test_case_random_num = random.randint(0, 99999999999999999999)
    for i in range(len(tasks_set_data)):
        test_case_environment_id_id = tasks_set_data[i]['environment_id_id']

        test_test_set_tasks_id_id = nid
        test_case_herders = models.SystemEnvironment.objects.filter(environment_id=test_case_environment_id_id).values()

        test_environment_hander = test_case_herders[0]['environment_hander']
        test_case_request_url = str(test_case_herders[0]['environment_url'][0:-1]) + str(tasks_set_data[i]['request_url'])
        print(test_case_request_url)
        test_case_request_method = tasks_set_data[i]['request_method']
        test_case_test_cases_name = tasks_set_data[i]['test_cases_name']
        test_case_request_parameters = tasks_set_data[i]['request_parameters']
        test_case_Extract_the_response_value = tasks_set_data[i]['Extract_the_response_value']
        test_case_Verify_the_response_value = tasks_set_data[i]['Verify_the_response_value']
        print("J校验值%s"%test_case_Verify_the_response_value)

        if test_case_request_method == 0:

            conclusion = requests.get(url=test_case_request_url, headers=eval(test_environment_hander),
                                      json=eval(test_case_request_parameters),
                                      )
            test_case_reponse = conclusion
        else:


            conclusion = requests.post(url=test_case_request_url, headers=eval(test_environment_hander),
                                       json=eval(test_case_request_parameters), )
            test_case_reponse = conclusion

        json_f_or_t = JsonBUF.iso_json(test_case_reponse.text)
        if test_case_Extract_the_response_value == "" and json_f_or_t is True:

            models.Test_Set_Tasks_Run_Log.objects.create(serial_number=test_case_random_num,
                                                         test_cases_name=test_case_test_cases_name,
                                                         request_url=test_case_request_url,
                                                         request_method=test_case_request_method,
                                                         request_parameters=test_case_request_parameters,
                                                         response_parameters=test_case_reponse.text,
                                                         Extract_the_response_value=test_case_Extract_the_response_value,
                                                         Verify_the_response_value=test_case_Verify_the_response_value,
                                                         run_the_result=1,
                                                         environment_id_id=test_case_environment_id_id,
                                                         test_set_tasks_id_id=test_test_set_tasks_id_id,
                                                         test_report_id_id=test_report_id
                                                         )
        elif json_f_or_t is False:

            models.Test_Set_Tasks_Run_Log.objects.create(serial_number=test_case_random_num,
                                                         test_cases_name=test_case_test_cases_name,
                                                         request_url=test_case_request_url,
                                                         request_method=test_case_request_method,
                                                         request_parameters=test_case_request_parameters,
                                                         response_parameters=test_case_reponse.text,
                                                         Extract_the_response_value=test_case_Extract_the_response_value,
                                                         Verify_the_response_value=test_case_Verify_the_response_value,
                                                         run_the_result=2,
                                                         environment_id_id=test_case_environment_id_id,
                                                         test_set_tasks_id_id=test_test_set_tasks_id_id,
                                                         test_report_id_id=test_report_id
                                                         )
        else:



            request_txt=json.loads(test_case_reponse.text)



            resuitr = Story_Test.test_case_validation_results(test_case_reponse=test_case_reponse,
                                                              extract_the_response_value=test_case_Extract_the_response_value ,
                                                              verify_the_response_value=test_case_Verify_the_response_value,is_customize_the_function=0)

            if resuitr[0] == resuitr[1] - 1:

                models.Test_Set_Tasks_Run_Log.objects.create(serial_number=test_case_random_num,
                                                             test_cases_name=test_case_test_cases_name,
                                                             request_url=test_case_request_url,
                                                             request_method=test_case_request_method,
                                                             request_parameters=test_case_request_parameters,
                                                             response_parameters=test_case_reponse.text,
                                                             Extract_the_response_value=test_case_Extract_the_response_value,
                                                             Verify_the_response_value=test_case_Verify_the_response_value,
                                                             run_the_result=1,
                                                             environment_id_id=test_case_environment_id_id,
                                                             test_set_tasks_id_id=test_test_set_tasks_id_id,
                                                             test_report_id_id=test_report_id
                                                             )

            else:


                models.Test_Set_Tasks_Run_Log.objects.create(serial_number=test_case_random_num,
                                                             test_cases_name=test_case_test_cases_name,
                                                             request_url=test_case_request_url,
                                                             request_method=test_case_request_method,
                                                             request_parameters=test_case_request_parameters,
                                                             response_parameters=test_case_reponse.text,
                                                             Extract_the_response_value=test_case_Extract_the_response_value,
                                                             Verify_the_response_value=test_case_Verify_the_response_value,
                                                             run_the_result=2,
                                                             environment_id_id=test_case_environment_id_id,
                                                             test_set_tasks_id_id=test_test_set_tasks_id_id,
                                                             test_report_id_id=test_report_id
                                                             )
    return redirect("/test/set/tasks/list/")
def test_set_tasks_view(request, nid):
    if   request.method=='GET':
        datat=models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid)
        print(datat)
        test_set_tasks_name=models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid).values()[0]['test_set_tasks_name']
        test_set_tasks_id=models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid).values()[0]['test_set_tasks_id']
        tille='测试集%s：测试用例'%test_set_tasks_name
        test_set_cases_data=models.ManualTestCases.objects.filter(test_set_tasks=nid).values()
        print(test_set_cases_data)
        return render(request, "web/set_cases_list.html", {"data": test_set_cases_data, "tille": tille,'test_set_tasks_id':test_set_tasks_id})
    else:
        pass
def test_set_tasks_case_delet(request, nid,niid):
    if request.method == 'GET':
        row_object = models.ManualTestCases.objects.filter(manual_test_cases_id=nid).first()
        if not row_object:
            return redirect("/test/set/tasks/view/{0}/".format(niid))
        else:
            models.ManualTestCases.objects.filter(manual_test_cases_id=nid).delete()
            return redirect("/test/set/tasks/view/{0}/".format(niid))

def test_set_tasks_delet(request,nid):
    if request.method== "GET":
        row_object = models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid).first()
        if not row_object:
            return redirect("/test/set/tasks/list/")
        else:
            models.Test_Set_Tasks.objects.filter(test_set_tasks_id=nid).delete()
            return redirect("/test/set/tasks/list/")
def test_set_tasks_disassociate(request,nid,setnid):
    if request.method== "GET":

        row_object = models.ManualTestCases.objects.filter(manual_test_cases_id=nid)
        row_object2 = models.Test_Set_Tasks.objects.filter(test_set_tasks_id=setnid)

        print(row_object)
        print(row_object2)

        if not row_object:
            return redirect("/test/set/tasks/list/")
        else:
            row_object=row_object[0]
            row_object2=row_object2[0]
            row_object.test_set_tasks.remove(row_object2)
            row_object.save()
            return redirect("/test/set/tasks/list/")
def test_set_tasks_disassociaten(request,nid):
    if request.method== "GET":

        row_object = models.ManualTestCases.objects.filter(manual_test_cases_id=nid)
        row_object2=row_object[0].test_set_tasks.values()

        print(row_object)
        print(row_object2)

        if not row_object:
            return redirect("/list/of/manual/test/cases/")
        else:

            if len(row_object2) >1:
                for i in row_object2:
                    test_id=i['test_set_tasks_id']
                    print(test_id)
                    data = models.Test_Set_Tasks.objects.filter(test_set_tasks_id=test_id)
                    print(data)
                    row_object_data = row_object[0]
                    row_object_data.test_set_tasks.remove(test_id)
                    row_object_data.save()
            else:
                row_object2=row_object2[0]['test_set_tasks_id' ]

                row_object[0].test_set_tasks.remove(row_object2)
                row_object[0].save()
            return redirect("/list/of/manual/test/cases/")