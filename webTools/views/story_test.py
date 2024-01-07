import requests
import json
import os
import re
import time
import logging
import pandas
import random
import datetime
import requests
from urllib import parse
from urllib.parse import quote
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, HttpResponse
from webTools.forms.story_test_cases_from import *
from django.http.request import QueryDict
from django.http import Http404, FileResponse
from pyecharts.charts import Graph
from pyecharts import options as opts
from pyecharts.charts import Tree
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from webTools.public.is_json import JsonBUF, JudgmentType
from webTools.public.story_case_test import Story_Test

from webTools.public.swagger_data_processing import DataProcessing

from webTools.public.logger import get_logger
from webTools.public.encrypt import md5
from webTools.public.identity import IdNumber
from webTools.public.wthfef import login_processing

def story_test_cases_list(request):
    try:
        if request.method == "GET":
            foreee = models.Story_Test_Cases_Set.objects.filter().values()
            print(foreee)

            return render(request, "web/story_test_cases_list.html", {"dadf": foreee})
        else:
            return redirect("/story/test/cases/list/")

    except Exception as e:
        logging.error(e)


def story_test_cases_add(request):
    try:
        if request.method == "GET":

            data = StoryTeseCasesAddForm()
            return render(request, "web/chenge.html", {"form": data})
        elif request.method == "POST":
            data = request.POST
            info_dict = request.session.get("info")
            user_mobile_phone = info_dict["mobile_phone"]
            dataa = data.dict()
            print(dataa)
            daata = dataa['story_test_set_name']
            form = StoryTeseCasesAddForm(data)
            if models.Story_Test_Cases_Set.objects.filter(story_test_set_name=daata).first():
                form.add_error("story_test_set_name", "故事模式用例已存在")

            if form.is_valid():
                form.save()
                models.Story_Test_Cases_Set.objects.filter(story_test_set_name=daata).update(
                    create_user=user_mobile_phone,
                    run_time="未运行")
                return redirect("/story/test/cases/list/")
            else:
                return render(request, "web/chenge.html", {"form": form})

        else:
            data = models.Test_Set_Tasks.objects.all()
            return render(request, "web/story_test_cases_list.html", {"data": data})
    except Exception as e:
        logging.error(e)


def story_test_cases_data_list(request, nid):
    try:
        if request.method == "GET":
            name_cases = models.Story_Test_Cases_Set.objects.filter(story_test_set_id=int(nid)).values()
            story_test_case_name = name_cases[0]['story_test_set_name']
            tille = '故事模式 %s  步骤列表' % story_test_case_name
            data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).order_by('serial_number')
            return render(request, "web/stort_case_data_list.html", {"data": data, 'tille': tille})
        else:
            print(nid)
    except Exception as e:
        logging.error(e)


def story_test_cases_data_add(request):
    try:
        if request.method == "GET":
            data = StoryTeseCasesDataAddForm()
            return render(request, "web/chenge.html", {"form": data})
        elif request.method == "POST":
            data = request.POST
            dataa = data.dict()
            story_test_set_id_data = dataa['story_test_set_id']
            print(dataa)
            form = StoryTeseCasesDataAddForm(data=request.POST)
            if story_test_set_id_data != "":

                story_test_case_nama = dataa['story_test_case_name']

                if models.Story_Test_Cases.objects.filter(
                        story_test_case_name=story_test_case_nama,
                        story_test_set_id=story_test_set_id_data).first():
                    form.add_error("story_test_case_name", "名字重复已经存在")
                    return render(request, "web/chenge.html", {"form": form})

            if form.is_valid():
                serial_number_data = dataa['serial_number']
                if models.Story_Test_Cases.objects.filter(
                        story_test_set_id=story_test_set_id_data, serial_number=serial_number_data).first():
                    story_data = models.Story_Test_Cases.objects.filter(
                        story_test_set_id=story_test_set_id_data).values().order_by(
                        'serial_number')
                    for i in range(len(story_data)):
                        print("开始i循环%s" % i)
                        if i >= int(serial_number_data) - 1:
                            story_test_case_id_nn = story_data[i]["story_test_case_id"]
                            models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id_nn).update(
                                serial_number=i + 2)
                    form.save()
                else:
                    form.save()

                return redirect("/story/test/cases/list/")
            return render(request, "web/chenge.html", {"form": form})
        else:
            return redirect("/story/test/cases/list/")
    except Exception as e:
        logging.error(e)


def story_test_cases_data_information(request, nid):
    try:
        if request.method == 'GET':
            data = models.Story_Test_Cases.objects.filter(story_test_case_id=nid).first()
            return render(request, 'web/story_steps_info.html', {"data": data})
        elif request.method == 'POST':
            pass
        else:
            return redirect("/story/test/cases/list/")
    except Exception as e:
        logging.error(e)


def story_test_cases_data_edit(request, nid):
    try:
        row_object = models.Story_Test_Cases.objects.filter(story_test_case_id=nid).first()
        if request.method == 'GET':
            tille = '步骤编辑'
            form = StoryTeseCasesDataAddForm(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        elif request.method == "POST":
            data = request.POST
            dataa = data.dict()
            story_test_set_id_data = dataa['story_test_set_id']
            serial_number_in = dataa['serial_number']
            form = StoryTeseCasesDataAddForm(data=request.POST, instance=row_object)
            if form.is_valid():
                data_calt = models.Story_Test_Cases.objects.filter(
                    story_test_set_id=story_test_set_id_data).values().order_by(
                    'serial_number')
                serial_number_data = dataa['serial_number']
                if  int(serial_number_data) <= len(data_calt):
                    story_data = models.Story_Test_Cases.objects.filter(
                        story_test_set_id=story_test_set_id_data).values().order_by(
                        'serial_number')
                    stoy_lsit_nn = Story_Test.story_original_sorting(story_data, nid, serial_number_in)
                    for i in range(len(stoy_lsit_nn)):
                        models.Story_Test_Cases.objects.filter(story_test_case_id=stoy_lsit_nn[i]).update(
                            serial_number=i + 1)
                    form.save()
                    return redirect("/story/test/cases/list/")

                else:

                    form.add_error("serial_number", "   当前序号为%s，超过当前最大步骤值" % (serial_number_data,))
                    return render(request, "web/chenge.html", {"form": form})

            else:
                return render(request, "web/chenge.html", {"form": form})
        else:
            return redirect("/story/test/cases/list/")
    except Exception as e:
        logging.error(e)


def story_test_cases_data_delet(request, nid):
    row_object = models.Story_Test_Cases.objects.filter(story_test_case_id=nid).first()
    if not row_object:
        return render(request, "web/stort_case_data_list.html")
    else:
        models.Story_Test_Cases.objects.filter(story_test_case_id=nid).delete()
        return redirect("/story/test/cases/list/")


def story_test_cases_run(request, nid):
    try:
        if request.method == 'GET':

            story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values().order_by(
                'serial_number')

            stort_info_dic, stort_info_lit = Story_Test.interface_data_dictionary(story_data)

            print("zhen 故事集%s" % stort_info_dic)
            print("zhen 故事原始路径%s" % stort_info_lit)

            num = 0
            sdfa_dict = {}
            run_time = datetime.datetime.now()
            loc_time = time.strftime("%Y %a %b %d %H:%M:%S ", time.localtime())
            models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).update(run_time=run_time)
            report_name = loc_time + 'Story测试报告'
            models.Story_Test_Reports.objects.create(story_test_report_name=report_name, story_test_report_cases=nid)
            report_name_id = models.Story_Test_Reports.objects.filter(story_test_report_name=report_name).values()
            response_variable_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values()
            print("shahh%s" % response_variable_data)
            response_variable_dict = {}
            sql_variable_dict = {}
            response_variable_dict = Story_Test.fixed_custom_functions_list(story_data)
            report_name_id = report_name_id[0]['story_test_report_id']
            run_num = 0
            fail_num = 9999999999999
            regain_times = 0
            while run_num <= len(stort_info_lit) - 1:
                story_data_one = stort_info_dic[stort_info_lit[run_num]]
                print("当前执行%s 总路线%s" % (run_num, stort_info_lit))
                story_test_case_url = story_data_one['test_report_url']
                request_method = story_data_one['request_method']
                story_test_name = story_data_one['story_test_case_name']
                serial_number = story_data_one['serial_number']
                story_test_case_id = story_data_one['story_test_case_id']
                response_variable = story_data_one['response_variable']
                test_report_request_parameters = story_data_one['test_report_request_parameters']
                environment = int(story_data_one['environment_id_id'])
                env_data = models.SystemEnvironment.objects.filter(environment_id=environment).values()
                environment_url = env_data[0]['environment_url']
                environment_hander = env_data[0]['environment_hander']
                extract_the_response_value = story_data_one['extract_the_response_value']
                verify_the_response_value = story_data_one['verify_the_response_value']
                sql_statement = story_data_one['sql_statement']
                sql_variable = story_data_one['sql_variable']
                test_report_request_parameters_new = eval(test_report_request_parameters)
                new_lsit = []
                new_lsit2 = []
                custom_variable_location_list = []
                last_data_lsit = []
                log_dat=LoginProcessing()
                request_cookies=log_dat.run_the_result(story_test_case_url)               
                story_test_case_url = environment_url + story_test_case_url[1:]
                environment_hander = eval(environment_hander)
                if sql_statement != None and sql_variable != None:
                    sql_variable_dict = Story_Test.sql_custom_variables_dict(sql_statement=sql_statement,
                                                                             sql_variable=sql_variable,
                                                                             response_variable_dict=response_variable_dict)
                    print(sql_variable_dict)
                    is_customize_the_function = 1
                else:
                    is_customize_the_function = 0
                if request_method == 0:
                    test_report_request_parameters = Story_Test.custom_modified_requests(response_variable_dict,
                                                                                         test_report_request_parameters)
                    test_case_reponse = requests.get(
                        url=story_test_case_url, headers=environment_hander,
                        json=eval(test_report_request_parameters),
                        cookies=request_cookies)
                    json_reponse = test_case_reponse.text

                    if response_variable != None:
                        response_variable_dict = Story_Test.response_variable_add(response_variable_dict,
                                                                                  test_case_reponse,
                                                                                  response_variable)


                else:
                    print(str(test_report_request_parameters))
                    test_report_request_parameters = Story_Test.custom_modified_requests(response_variable_dict,
                                                                                         test_report_request_parameters)
                    test_case_reponse = requests.post(
                        url=story_test_case_url, headers=environment_hander, json=eval(test_report_request_parameters,
                            cookies=request_cookies)
                    )
                    print("默认返回值%s", test_case_reponse.text)
                    if response_variable != None:
                        response_variable_dict = Story_Test.response_variable_add(response_variable_dict,
                                                                                  test_case_reponse,
                                                                                  response_variable)

                json_f_or_t = JsonBUF.iso_json(test_case_reponse.text)
                json_reponse = test_case_reponse.text
                if extract_the_response_value == "" and json_f_or_t is True:

                    models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                        execution_results=0, test_report_reponse_parameters=json_reponse
                    )
                    models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                   serial_number=serial_number,
                                                                   request_url=story_test_case_url,
                                                                   request_method=request_method,
                                                                   request_parameters=test_report_request_parameters,
                                                                   response_parameters=json_reponse,
                                                                   Extract_the_response_value=extract_the_response_value,
                                                                   Verify_the_response_value=verify_the_response_value,
                                                                   test_case_create_time=loc_time,
                                                                   run_the_result=1,
                                                                   environment_id_id=environment,
                                                                   story_test_set_id=nid,
                                                                   test_report_id_id=report_name_id,
                                                                   )
                    return redirect("/story/test/cases/list/")
                elif json_f_or_t is False:
                    models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                        execution_results=1, test_report_reponse_parameters=json_reponse
                    )
                    models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                   serial_number=serial_number,
                                                                   request_url=story_test_case_url,
                                                                   request_method=request_method,
                                                                   request_parameters=test_report_request_parameters,
                                                                   response_parameters=json_reponse,
                                                                   Extract_the_response_value=extract_the_response_value,
                                                                   Verify_the_response_value=verify_the_response_value,
                                                                   test_case_create_time=loc_time,
                                                                   run_the_result=2,
                                                                   environment_id_id=environment,
                                                                   story_test_set_id=nid,
                                                                   test_report_id_id=report_name_id,
                                                                   )
                    return redirect("/story/test/cases/list/")
                else:

                    # 进入校验

                    resuitr = Story_Test.test_case_validation_results(test_case_reponse=test_case_reponse,
                                                                      extract_the_response_value=extract_the_response_value,
                                                                      verify_the_response_value=verify_the_response_value,
                                                                      is_customize_the_function=is_customize_the_function,
                                                                      response_variable_dict=response_variable_dict)

                    if resuitr[0] == resuitr[1] - 1 and resuitr[2] == True:

                        models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                            execution_results=0, test_report_reponse_parameters=json_reponse
                        )

                        models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                       serial_number=serial_number,
                                                                       request_url=story_test_case_url,
                                                                       request_method=request_method,
                                                                       request_parameters=test_report_request_parameters,
                                                                       response_parameters=json_reponse,
                                                                       Extract_the_response_value=extract_the_response_value,
                                                                       Verify_the_response_value=verify_the_response_value,
                                                                       test_case_create_time=loc_time,
                                                                       run_the_result=1,
                                                                       environment_id_id=environment,
                                                                       story_test_set_id=nid,
                                                                       test_report_id_id=report_name_id,
                                                                       )
                        run_num += 1
                        last_num = 0

                    else:

                        models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                            execution_results=1, test_report_reponse_parameters=json_reponse
                        )
                        models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                       serial_number=serial_number,
                                                                       request_url=story_test_case_url,
                                                                       request_method=request_method,
                                                                       request_parameters=test_report_request_parameters,
                                                                       response_parameters=json_reponse,
                                                                       Extract_the_response_value=extract_the_response_value,
                                                                       Verify_the_response_value=verify_the_response_value,
                                                                       test_case_create_time=loc_time,
                                                                       run_the_result=2,
                                                                       environment_id_id=environment,
                                                                       story_test_set_id=nid,
                                                                       test_report_id_id=report_name_id,

                                                                       )
                        if fail_num == 9999999999999:

                            fail_num = run_num
                            run_num = int(resuitr[2])
                        else:
                            print("当前执行%s 失败名%s" % (run_num, fail_num))

                            if regain_times <= 1:
                                regain_times += 1
                                print("当前次数%s" % regain_times)
                            else:
                                run_num = 9999999999999999999

            return redirect("/story/test/cases/list/")
    except Exception as e:
        logging.error(e)


def story_test_set_edit(request, nid):
    try:
        row_object = models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).first()
        tille = "有序测试集测试任务编辑"
        if request.method == "GET":
            form = StoryTeseCasesAddForm(instance=row_object)
            return render(request, "web/chenge.html", {"form": form, "tille": tille})
        else:
            form = StoryTeseCasesAddForm(data=request.POST, instance=row_object)
            if form.is_valid():
                form.save()
                return redirect("/story/test/cases/list/")
            else:
                return render(request, "web/chenge.html", {"form": form, "tille": tille})
    except Exception as e:
        logger = logging.getLogger('django')
        logger.error(e)


def story_test_set_delet(request, nid):
    logger = logging.getLogger('django')
    try:
        if request.method == "GET":
            row_object = models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).first()
            if not row_object:
                return redirect("/story/test/cases/list/")
            else:
                models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).delete()
                return redirect("/story/test/cases/list/")
    except Exception as e:
        logger.error(e)
def story_test_cases_data_up(request,nid):
    if request.method == "GET":
        ni=models.Story_Test_Cases.objects.filter(story_test_case_id=nid).values()
        print(ni)
        ni_serial=ni[0]["serial_number"]
        ni_set=ni[0]["story_test_set_id_id"]
        story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=ni_set).values().order_by(
            'serial_number')
        if  int(ni_serial) !=1 :

            models.Story_Test_Cases.objects.filter(story_test_set_id=ni_set,serial_number=ni_serial-1).update( serial_number=ni_serial)
            models.Story_Test_Cases.objects.filter(story_test_case_id=nid).update(serial_number=ni_serial-1)
            return redirect("/story/test/cases/list/")
        else:
            return redirect("/story/test/cases/list/")
    else:
        return redirect("/story/test/cases/list/")
def story_test_cases_data_down(request,nid):
    if request.method == "GET":
        ni=models.Story_Test_Cases.objects.filter(story_test_case_id=nid).values()
        ni_serial=ni[0]["serial_number"]
        ni_set=ni[0]["story_test_set_id_id"]
        print(ni_set)
        story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=ni_set).values().order_by(
            'serial_number')

        if story_data[len(story_data)-1]['serial_number']!= int(ni_serial):
            models.Story_Test_Cases.objects.filter(story_test_set_id=ni_set,serial_number=ni_serial+1).update( serial_number=ni_serial)
            models.Story_Test_Cases.objects.filter(story_test_case_id=nid).update(serial_number=ni_serial+1)
            return redirect("/story/test/cases/list/")
        else:
            return redirect("/story/test/cases/list/")
    else:
        return redirect("/story/test/cases/list/")
def story_test_cases_copy(request,nid):
    if request.method =="GET":
        story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values().order_by(
            'serial_number')
        print(story_data)
        models.Story_Test_Cases_Set.objects.create( story_test_set_name="复制%s"%nid,create_user="系统",)
        nes_set=models.Story_Test_Cases_Set.objects.filter(story_test_set_name="复制%s"%nid,create_user="系统").values()
        new_sdet_id=nes_set[0]['story_test_set_id']
        for i in range(len(story_data)):

            story_test_case_name = story_data[i]['story_test_case_name'],
            test_report_url = story_data[i]['test_report_url'],

            request_method =story_data[i]['request_method'],
            print(request_method)
            test_report_request_parameters = story_data[i]['test_report_request_parameters'],
            extract_the_response_value = story_data[i]['extract_the_response_value'],
            verify_the_response_value = story_data[i]['verify_the_response_value'],
            test_report_reponse_parameters = story_data[i]['test_report_reponse_parameters'],
            serial_number = story_data[i]['serial_number'],
            print(serial_number)
            response_variable =story_data[i]['response_variable'],
            sql_statement =story_data[i]['sql_statement'],
            sql_variable = story_data[i]['sql_variable'],
            custom_variable = story_data[i]['custom_variable'],
            custom_time = story_data[i]['custom_time'],
            environment_id = story_data[i]['environment_id_id'],
            story_test_set_id = story_data[i]['story_test_set_id_id'],
            execution_results = story_data[i]['execution_results'],
            models.Story_Test_Cases.objects.create(story_test_case_name=story_test_case_name[0],
                                                   test_report_url=test_report_url[0],
                                                   request_method=request_method[0],
                                                   test_report_request_parameters=test_report_request_parameters[0],
                                                   extract_the_response_value=extract_the_response_value[0],
                                                   verify_the_response_value =verify_the_response_value[0],
                                                   test_report_reponse_parameters=test_report_reponse_parameters[0],
                                                   serial_number=serial_number[0],
                                                   response_variable=response_variable[0],
                                                   sql_statement= sql_statement[0],
                                                   sql_variable=sql_variable[0],
                                                   custom_variable=custom_variable[0],
                                                   custom_time=custom_time[0],
                                                   environment_id_id =  environment_id[0],
                                                   story_test_set_id_id=new_sdet_id,
                                                   execution_results=execution_results[0],

                                                   )
        return redirect("/story/test/cases/list/")
def data_tu(request,nid):
    story_name = models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).values()[0]['story_test_set_name']
    story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values().order_by(
        'serial_number')
    buzhou_lsit=[]
    for  iiiii in story_data:
        buzhou_lsit.append(iiiii["story_test_case_name"]+iiiii["test_report_url"])


    print(buzhou_lsit)
    nodes = []
    links = []
    for i in range(len(story_data)):
        pp=opts.GraphNode(name=story_data[i]['story_test_case_name']+story_data[i]['test_report_url'], symbol_size=60)


        nodes.append(pp)
    print(nodes)

    for i in range(len(story_data)):
        print(i , len(story_data))
        ext_ldit = str(story_data[i]['extract_the_response_value']).split('////')
        sdfsdf_list = str(story_data[i]['verify_the_response_value']).split("////")
        if "-" in str(story_data[i]['verify_the_response_value']):

            for ii in range(len(sdfsdf_list)):
                if "-" in  sdfsdf_list[ii]:

                    sdf_list=str( sdfsdf_list[ii]).split('-')
                    print(sdf_list[1])
                    links.append( {"source": story_data[i]['story_test_case_name']+story_data[i]['test_report_url'],
                     "target": buzhou_lsit[int(sdf_list[1])-1], "value":ext_ldit[ii]+ "="+sdf_list[0], "draggable": "true", })

                else:
                    links.append({"source": buzhou_lsit[i],
                                  "target": buzhou_lsit[i + 1], "value":ext_ldit[ii]+ "="+sdfsdf_list[ii]  , "draggable": "true", })

        elif int(i)+1 ==int(len(story_data)):
            continue
        else:
            links.append({"source":buzhou_lsit[i] ,
                          "target": buzhou_lsit[i+1] , "value":"无重定向[正常执行]"  , "draggable": "true", })



    init_opts = opts.InitOpts(width="100%",
                              height="1500px",
                              renderer="canvas",
                              page_title="%s关系图"%story_name,
                              theme=ThemeType.MACARONS,
                              js_host=""
                              )
    edge_label = opts.LabelOpts(
        is_show=True,
        position="middle",
        color="blue",
        formatter=JsCode(
            """
            function(params){
            return params.value
            }
            """
        )
    )

    linestyle_opts = opts.LineStyleOpts(
        width=1,
        opacity=0.9,
        curve=0.1,
        type_="dashed",  # "solid",

    )

    graph = Graph(init_opts)
    graph.add("", nodes, links, repulsion=30000, edge_symbol=['circle', 'arrow'],
              is_draggable=True, edge_label=edge_label, linestyle_opts=linestyle_opts,
              )
    graph.set_global_opts(title_opts=opts.TitleOpts(title="%s关系图"%story_name), )
    current_directory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    tu_path=os.path.join( current_directory,"templates/web/diagram.html")

    graph.render(r'%s'%tu_path)
    return render(request, "web/diagram.html",)

def data_tree(request,nid):
    story_name = models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).values()[0]['story_test_set_name']
    story_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values().order_by(
        'serial_number')
    isd=[story_data[i]["story_test_case_name"] for i in range(len(story_data))]
    print(
        isd
    )

    # data=story_data
    story_dict={}
    # for i in range(len(story_data)):
    #     story_dict['name']



    dat_json=requests.get(url="https://echarts.apache.org/examples/data/asset/data/flare.json").text
    dat_jsonn=json.loads(dat_json)
    print(dat_json)


    current_directory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    tu_path = os.path.join(current_directory, "templates/web/tree.html")


    c = (
        Tree()
        .add(
            "",
            [dat_jsonn],
            collapse_interval=2,
            orient="TB",
            label_opts=opts.LabelOpts(
                position="top",
                horizontal_align="right",
                vertical_align="middle",
                rotate=-90,
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-上下方向"))
        .render(r'%s'%tu_path)
    )



    return render(request, "web/tree.html", )
