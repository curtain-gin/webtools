import requests
import json
import os
import time
import logging
import pandas
from urllib import parse
from urllib.parse import quote
import requests
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.swagger_management_form import *
from webTools.forms.interface_info_form import *
from webTools.forms.version_management_form import *
from django.http.request import QueryDict
from django.http import Http404, FileResponse
from webTools.public.swagger_data_processing import DataProcessing

from webTools.public.logger import get_logger
from webTools.public.encrypt import md5


# from webTools.public.swagger_data_processing import


def story_test_report_list(request):
    try:
        tille = "故事测试报告列表"
        forff = models.Story_Test_Reports.objects.all().order_by("-story_test_report_id")
        return render(
            request, "web/story_test_report_list.html", {"data": forff, "tille": tille}
        )
    except Exception as e:
        print(1)


def story_test_report_view(request, nid):
    # test_task_id = models.Story_Test_Reports.objects.get(story_test_report_id=nid).story_test_report_id
    test_report_name = models.Story_Test_Reports.objects.get(story_test_report_id=nid).story_test_report_name
    tille = test_report_name
    total_number_of_test_set_tasks = models.Test_Story_Tasks_Run_Log.objects.filter(
        test_report_id_id=nid).count()
    total_number_of_failures = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=nid,
                                                                            run_the_result=2).count()
    total_number_of_successes = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=nid
                                                                               ,
                                                                             run_the_result=1).count()

    case_data = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=nid)
    print(total_number_of_test_set_tasks)
    print(total_number_of_failures)
    print(total_number_of_successes)
    print(case_data)
    return render(
        request, "web/storytest_task_report_log.html", {"data": total_number_of_test_set_tasks, "tille": tille,
                                                   "total_number_of_test_set_tasks": total_number_of_test_set_tasks,
                                                   "total_number_of_failures": total_number_of_failures,
                                                   "total_number_of_successes": total_number_of_successes,
                                                   "fro": case_data}
    )

def story_test_report_case_log(request,nid):



    if request.method == "GET":
        reponse_data = models.Test_Story_Tasks_Run_Log.objects.filter(
            test_set_tasks_run_id=nid
        ).first()
        return render(
            request, "web/story_case_info_log.html", {"data": reponse_data}
        )
    else:
        reponse_data = models.Test_Set_Tasks_Run_Log.objects.filter(
            test_set_tasks_run_id=nid
        ).first()
        return render(
            request, "web/story_case_info_log.html", {"data": reponse_data}
        )