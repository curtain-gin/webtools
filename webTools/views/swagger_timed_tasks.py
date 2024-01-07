import logging
import pickle
import json
import datetime
import random
import time
import requests

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from webTools.public.logger import get_logger
from webTools.public.daba_tuple_to_dict import execute_query
from webTools.forms.mock_serice_interfaces_from import *
from webTools.forms.new_timed_task_from import *
from webTools.public.is_json import JsonBUF
from webTools.public.identity import IdNumber
from webTools.public.story_case_test import Story_Test

from django.shortcuts import render, redirect, HttpResponse
from webTools.public.swagger_data_processing import DataProcessing

scheduler = BackgroundScheduler(timezone="Asia/Shanghai")
# 调度器使用默认的DjangoJobStore()
scheduler.add_jobstore(DjangoJobStore(), 'default')
try:
    def test2():
        env1 = "https://swagger.ennejb.cn/swagger/opcs/swagger-ui.html"
        token = models.UserAppInfo.objects.get(username="SDP").password
        DataProcessing.first_data(token, env1)
        env2 = "https://swagger.ennejb.cn/swagger/sms/swagger-ui.html"
        token = models.UserAppInfo.objects.get(username="SDP").password
        DataProcessing.first_data(token, env2)

        env3 = "https://swagger.ennejb.cn/swagger/es/swagger-ui.html"
        token = models.UserAppInfo.objects.get(username="SDP").password
        DataProcessing.first_data(token, env3)

        env4 = "https://swagger.ennejb.cn/swagger/file/swagger-ui.html"
        token = models.UserAppInfo.objects.get(username="SDP").password
        DataProcessing.first_data(token, env4)


    scheduler.start()

    sql = """
        SELECT * FROM `webtoolsdb`.`django_apscheduler_djangojob` LIMIT 0,1000
        """
    env_num = "default"

    result = execute_query(env_num, sql)
    num = 0
    for i in range(len(result)):
        if result[i]['id'] == "test2":
            num += 1
    if num != 1:
        scheduler.add_job(
            test2,
            "cron",
            hour="23",
            minute="59",
            second="55",
            id="test2",
        )
except Exception as e:
        get_logger().error(e)

def new_timed_task_list(request):
    try:
        if request.method == 'GET':
            sql = """
            SELECT
            * 
            FROM
            `webtoolsdb`.`webTools_customize_scheduled_tasks` AS a
            LEFT JOIN  `webtoolsdb`.`django_apscheduler_djangojob` AS b ON b.id = a.tasks_time_name
            LEFT JOIN `webtoolsdb`.`webTools_userappinfo` AS c ON a.principal_id = c.user_id
            LEFT JOIN `webtoolsdb`.`webTools_test_set_tasks` AS d ON a.task_test_set_id = d.test_set_tasks_id
            LEFT JOIN `webtoolsdb`.`webTools_story_test_cases_set` AS e ON a.story_test_set_id = e.story_test_set_id
            ORDER BY a.test_set_tasks_run_id DESC
            """
            env_num = "default"

            result = execute_query(env_num, sql)

            return render(request, "web/new_timed_task_list.html", {"data": result})
    except Exception as e:

        get_logger().error(e)
        return redirect('/swagger/timed/tasks/list/')


def test(nid):
    loc_time = time.strftime("%Y %a %b %d %H:%M:%S ", time.localtime())
    test_report_name = loc_time + "TestReport"
    test_report_id = models.Test_Reports.objects.create(test_report_name=test_report_name,
                                                      test_report_cases=nid).test_report_id
    tasks_set_data=models.ManualTestCases.objects.filter(test_set_tasks=nid).values()
    test_case_random_num = random.randint(0, 99999999999999999999)
    if len(tasks_set_data) >0:
        for i in range(len(tasks_set_data)):
            test_case_environment_id_id = tasks_set_data[i]['environment_id_id']

            test_test_set_tasks_id_id = nid
            test_case_herders = models.SystemEnvironment.objects.filter(environment_id=test_case_environment_id_id).values()

            test_environment_hander = test_case_herders[0]['environment_hander']
            test_case_request_url = str(test_case_herders[0]['environment_url'][0:-1]) + str(
                tasks_set_data[i]['request_url'])
            print(test_case_request_url)
            test_case_request_method = tasks_set_data[i]['request_method']
            test_case_test_cases_name = tasks_set_data[i]['test_cases_name']
            test_case_request_parameters = tasks_set_data[i]['request_parameters']
            test_case_Extract_the_response_value = tasks_set_data[i]['Extract_the_response_value']
            test_case_Verify_the_response_value = tasks_set_data[i]['Verify_the_response_value']

            if test_case_request_method == 0:
                print(test_case_request_url)
                print(test_environment_hander)
                print(test_case_request_parameters)
                conclusion = requests.get(url=test_case_request_url, headers=eval(test_environment_hander),
                                          json=eval(test_case_request_parameters),
                                          )
                test_case_reponse = conclusion
                print(test_case_reponse)
            else:
                print(test_case_request_url)
                print(test_environment_hander)
                print(test_case_request_parameters)

                """
                test_case_reponse = requests.post(
                    url=url, headers=handerss, json=eval(request_parameters)
                )
                """
                conclusion = requests.post(url=test_case_request_url, headers=eval(test_environment_hander),
                                           json=eval(test_case_request_parameters), )
                test_case_reponse = conclusion
                print(test_case_reponse)

            json_f_or_t = JsonBUF.iso_json(test_case_reponse.text)
            if test_case_Extract_the_response_value == "" and json_f_or_t is True:
                models.Test_Set_Tasks_Run_Log.objects.create(serial_number=test_case_random_num,
                                                             test_cases_name=test_case_test_cases_name,
                                                             request_url=test_case_request_url,
                                                             request_method=test_case_request_method,
                                                             request_parameters=test_case_request_parameters,
                                                             response_parameters=test_case_reponse,
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

                resuitr = Story_Test.test_case_validation_results(test_case_reponse=test_case_reponse,
                                                                  extract_the_response_value=test_case_Extract_the_response_value,
                                                                  verify_the_response_value=test_case_Verify_the_response_value)

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
    else:
        print("Asdg")
    data_total = models.Test_Set_Tasks_Run_Log.objects.filter(test_report_id=test_report_id).count()
    data_suc = models.Test_Set_Tasks_Run_Log.objects.filter(test_report_id=test_report_id, run_the_result=1).count()
    data_fal = models.Test_Set_Tasks_Run_Log.objects.filter(test_report_id=test_report_id, run_the_result=2).count()
    print(data_total, data_suc, data_fal)

    if data_fal >= 1:
        wx_url = models.Web_Tootls_Disposition.objects.filter(disposition_key=1).values()[0]['disposition_value']
        web_url = models.Web_Tootls_Disposition.objects.filter(disposition_key=2).values()[0]['disposition_value']
        test_report_ad = '{0}/test/report/view/{1}/'.format(web_url,test_report_id)
        bot_url = wx_url
        dateata = {
            "msgtype": "markdown",
            "markdown": {
                "content": """测试集定时任务报告<font color=\"warning\">用例总数{0}</font>，如果需要可访问链接地址。\n
             >总数:<font color=\"comment\">{0}</font>
             >成功:<font color=\"comment\">{1}</font>
             >失败:<font color=\"comment\">{2}</font>
             >如需查看报告可挂VPN，报告地址:<font color=\"comment\">{3}</font>
             [点击跳转到报告地址,需要挂VPN]({3})
             """.format(data_total, data_suc, data_fal, test_report_ad)
            }
        }
        headers = {'content-type': 'application/json'}
        diag = requests.post(url=bot_url, headers=headers, json=dateata)
        print(diag.text)
    else:
        print(123)


def test_story(nid, name):
    story_data = models.Story_Test_Cases.objects.filter(story_test_set_id_id=nid).values().order_by(
        'serial_number')
    num = 0
    sdfa_dict = {}
    run_time = datetime.datetime.now()
    loc_time = time.strftime("%Y %a %b %d %H:%M:%S ", time.localtime())
    models.Story_Test_Cases_Set.objects.filter(story_test_set_id=nid).update(run_time=run_time)
    report_name = loc_time + 'Story测试报告'
    repoert_id=models.Story_Test_Reports.objects.create(story_test_report_name=report_name, story_test_report_cases=nid).story_test_report_id
    response_variable_data = models.Story_Test_Cases.objects.filter(story_test_set_id=nid).values()

    print("shahh%s" % response_variable_data)
    response_variable_dict = {}

    custom_variable_list = []
    if len(story_data)>0:
        for i in range(len(story_data)):
            print("shush俗话说%s" % i)
            print("未处理数据", story_data[i]['custom_variable'])
            if story_data[i]['custom_variable'] == None:
                continue
            else:
                custom_variable_list.append(story_data[i]['custom_variable'])
                daiga = (story_data[i]['custom_variable']).split('////')
                for ii in daiga:
                    print(ii)
                    if ii == '':
                        continue
                    else:
                        asdfadg = ii.split('///')
                        response_variable_dict[asdfadg[0]] = asdfadg[1]
        print("最后抽取自定义函数, 自定义固定函数%s" % response_variable_dict)

    # report_name_id = report_name_id[0]['story_test_report_id']
    if len(story_data) >0:
        for i in range(len(story_data)):
            story_test_case_url = story_data[i]['test_report_url']
            request_method = story_data[i]['request_method']
            story_test_name = story_data[i]['story_test_case_name']
            serial_number = story_data[i]['serial_number']
            story_test_case_id = story_data[i]['story_test_case_id']
            response_variable = story_data[i]['response_variable']
            test_report_request_parameters = story_data[i]['test_report_request_parameters']
            environment = int(story_data[i]['environment_id_id'])
            env_data = models.SystemEnvironment.objects.filter(environment_id=environment).values()
            environment_url = env_data[0]['environment_url']
            # repoert_id = models.Story_Test_Reports.objects.filter(story_test_report_name=report_name).values()[0][
            #     'story_test_report_id']

            environment_hander = env_data[0]['environment_hander']
            extract_the_response_value = story_data[i]['extract_the_response_value']
            verify_the_response_value = story_data[i]['verify_the_response_value']
            test_report_request_parameters_new = eval(test_report_request_parameters)
            new_lsit = []
            new_lsit2 = []
            custom_variable_location_list = []
            last_data_lsit = []

            story_test_case_url = environment_url + story_test_case_url[1:]
            environment_hander = eval(environment_hander)
            print(environment_hander)
            if request_method == 0:
                while "^" in str(test_report_request_parameters):
                    olde_data = str(test_report_request_parameters)
                    print(olde_data)
                    start_num = olde_data.find('^')
                    print(start_num)

                    stop_num = olde_data[start_num:].find('"')
                    print(stop_num)
                    rep_str = olde_data[start_num + 1:start_num + stop_num]
                    print(rep_str)
                    if rep_str == 'IsGenerateId':
                        random_sex = random.randint(0, 1)
                        rep_str_new = IdNumber.generate_id(sex=random_sex, id_city='杭州', idd_year='19980101')
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    elif rep_str == 'TesPhoneNum':
                        rep_str_new = IdNumber.test_phone_num()
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    # random_name
                    elif rep_str == 'RandomName':
                        rep_str_new = IdNumber.random_name()
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    else:
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, str(response_variable_dict[rep_str]))
                        print("替换后数据{0}".format(test_report_request_parameters))

                else:
                    print("修改后请求{0}".format(test_report_request_parameters))

                    test_case_reponse = requests.get(
                        url=story_test_case_url, headers=environment_hander, json=eval(test_report_request_parameters))
                    if response_variable != None:
                        data_dadf = json.loads(test_case_reponse.text)
                        print(type(data_dadf))
                        print(data_dadf['error'])
                        print("前职工%s" % response_variable.split('////'))
                        numf = 1
                        for i in response_variable.split('////'):
                            print("职工%s" % i)
                            if i != '' and numf != 0 and i[-1].isdigit() is None:
                                for ii in i:
                                    iod_idata = i.split('-')
                                    new_srt = ''
                                    iiff_list = []
                                    offff = ''
                                    print(iod_idata[1])
                                    if '[' in iod_idata[1]:
                                        for iii in iod_idata[1]:
                                            print("iii %s" % iii)
                                            if iii == '[':
                                                continue
                                            elif iii == ']':
                                                print("fjfjf kry %s" % offff)
                                                # iiff_list.append(offff)
                                                print(offff)

                                                data_dadf = data_dadf[offff]
                                                print("ewws%s" % data_dadf)
                                                offff = ''
                                            elif '[' not in iod_idata[1]:

                                                break
                                            else:
                                                offff = offff + iii
                                    else:
                                        numf = 0
                                        break
                                    response_variable_dict[iod_idata[0]] = data_dadf
                                    break
                            else:
                                continue

            else:
                print(str(test_report_request_parameters))

                while "^" in str(test_report_request_parameters):
                    olde_data = str(test_report_request_parameters)
                    print(olde_data)
                    start_num = olde_data.find('^')
                    print(start_num)

                    stop_num = olde_data[start_num:].find('"')
                    print(stop_num)
                    rep_str = olde_data[start_num + 1:start_num + stop_num]
                    # IdNumber
                    if rep_str == 'IsGenerateId':
                        random_sex = random.randint(0, 1)
                        rep_str_new = IdNumber.generate_id(sex=random_sex, id_city='杭州', idd_year='19980101')
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    elif rep_str == 'TesPhoneNum':
                        rep_str_new = IdNumber.test_phone_num()
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    # random_name
                    elif rep_str == 'RandomName':
                        rep_str_new = IdNumber.random_name()
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)
                    elif rep_str == "RandomAddres":
                        rep_str_new = "接口测试平台，随机地址" + IdNumber.random_name() + IdNumber.random_name() + IdNumber.random_name()
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, rep_str_new)

                    else:
                        test_report_request_parameters = str(test_report_request_parameters).replace(
                            "^" + rep_str, str(response_variable_dict[rep_str]))
                        print("替换后数据{0}".format(test_report_request_parameters))


                test_case_reponse = requests.post(
                    url=story_test_case_url, headers=environment_hander, json=eval(test_report_request_parameters)
                )
                print(test_case_reponse.text)
                if response_variable != None:
                    data_dadf = json.loads(test_case_reponse.text)
                    print(type(data_dadf))
                    print(data_dadf['error'])
                    print("前职工%s" % response_variable.split('////'))
                    numf = 1
                    for i in response_variable.split('////'):
                        print("职工%s" % i)
                        if i != '' and numf != 0:
                            for ii in i:
                                iod_idata = i.split('-')
                                new_srt = ''
                                iiff_list = []
                                offff = ''
                                print(iod_idata[1])
                                if '[' in iod_idata[1]:
                                    for iii in iod_idata[1]:
                                        print("iii %s" % iii)
                                        if iii == '[':
                                            continue
                                        elif iii == ']':
                                            print("fjfjf kry %s" % offff)
                                            # iiff_list.append(offff)
                                            print(offff)

                                            data_dadf = data_dadf[offff]
                                            print("ewws%s" % data_dadf)
                                            offff = ''
                                        elif '[' not in iod_idata[1]:

                                            break
                                        else:
                                            offff = offff + iii
                                else:
                                    numf = 0
                                    break
                                response_variable_dict[iod_idata[0]] = data_dadf
                                break

            print("最后自定义变量字典%s" % response_variable_dict)
            json_f_or_t = JsonBUF.iso_json(test_case_reponse.text)
            if extract_the_response_value == "" and json_f_or_t is True:

                models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                    execution_results=0, test_report_reponse_parameters=test_case_reponse.text
                )
                models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                               serial_number=serial_number,
                                                               request_url=story_test_case_url,
                                                               request_method=request_method,
                                                               request_parameters=test_report_request_parameters,
                                                               response_parameters=test_case_reponse.text,
                                                               Extract_the_response_value=extract_the_response_value,
                                                               Verify_the_response_value=verify_the_response_value,
                                                               test_case_create_time=loc_time,
                                                               run_the_result=1,
                                                               environment_id_id=environment,
                                                               story_test_set_id=nid,
                                                               test_report_id_id=repoert_id,
                                                               )
                return redirect("/story/test/cases/list/")
            elif json_f_or_t is False:
                models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                    execution_results=1, test_report_reponse_parameters=test_case_reponse.text
                )
                models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                               serial_number=serial_number,
                                                               request_url=story_test_case_url,
                                                               request_method=request_method,
                                                               request_parameters=test_report_request_parameters,
                                                               response_parameters=test_case_reponse.text,
                                                               Extract_the_response_value=extract_the_response_value,
                                                               Verify_the_response_value=verify_the_response_value,
                                                               test_case_create_time=loc_time,
                                                               run_the_result=2,
                                                               environment_id_id=environment,
                                                               story_test_set_id=nid,
                                                               test_report_id_id=repoert_id,
                                                               )

            else:
                print("进入校验")
                print(extract_the_response_value, verify_the_response_value)
                extract_the_response_value = extract_the_response_value.split(
                    "////"
                )
                request_txt = test_case_reponse.json()
                print(request_txt)
                offff = 0
                for ii in range(len(extract_the_response_value)):
                    request_txt_cope = request_txt
                    ndd = ""

                    for iii in extract_the_response_value[ii]:
                        if iii == "[":
                            ndd = ""
                            continue
                        elif iii == "]":
                            request_txt_cope = request_txt_cope[ndd]
                        else:
                            ndd = ndd + iii

                    if str(verify_the_response_value.split("////")[ii]) != str(
                            request_txt_cope
                    ):
                        break
                    else:
                        offff = offff + 1
                print(offff)
                print(len(extract_the_response_value))
                if offff == len(extract_the_response_value) - 1:
                    models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                        execution_results=0, test_report_reponse_parameters=request_txt
                    )
                    print("didididididi")
                    models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                   serial_number=serial_number,
                                                                   request_url=story_test_case_url,
                                                                   request_method=request_method,
                                                                   request_parameters=test_report_request_parameters,
                                                                   response_parameters=test_case_reponse.text,
                                                                   Extract_the_response_value=extract_the_response_value,
                                                                   Verify_the_response_value=verify_the_response_value,
                                                                   test_case_create_time=loc_time,
                                                                   run_the_result=1,
                                                                   environment_id_id=environment,
                                                                   story_test_set_id=nid,
                                                                   test_report_id_id=repoert_id,
                                                                   )

                else:

                    models.Story_Test_Cases.objects.filter(story_test_case_id=story_test_case_id).update(
                        execution_results=1, test_report_reponse_parameters=request_txt
                    )
                    models.Test_Story_Tasks_Run_Log.objects.create(test_cases_name=story_test_name,
                                                                   serial_number=serial_number,
                                                                   request_url=story_test_case_url,
                                                                   request_method=request_method,
                                                                   request_parameters=test_report_request_parameters,
                                                                   response_parameters=test_case_reponse.text,
                                                                   Extract_the_response_value=extract_the_response_value,
                                                                   Verify_the_response_value=verify_the_response_value,
                                                                   test_case_create_time=loc_time,
                                                                   run_the_result=2,
                                                                   environment_id_id=environment,
                                                                   story_test_set_id=nid,
                                                                   test_report_id_id=repoert_id,
                                                                   )
    print("开始发送定时故事")
    data_total = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=repoert_id).count()
    data_suc = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=repoert_id, run_the_result=1).count()
    data_fal = models.Test_Story_Tasks_Run_Log.objects.filter(test_report_id_id=repoert_id, run_the_result=2).count()
    print(data_total, data_suc, data_fal)

    if data_fal >= 1:
        wx_url = models.Web_Tootls_Disposition.objects.filter(disposition_key=1).values()[0]['disposition_value']
        web_url = models.Web_Tootls_Disposition.objects.filter(disposition_key=2).values()[0]['disposition_value']
        test_report_ad = '{0}/story/test/report/view/{1}/'.format(web_url, repoert_id)
        bot_url = wx_url
        dateata = {
            "msgtype": "markdown",
            "markdown": {
                "content": """故事模式定时  {4}任务报告<font color=\"warning\">用例总数{0}</font>，如果需要可访问链接地址。\n
             >总数:<font color=\"comment\">{0}</font>
             >成功:<font color=\"comment\">{1}</font>
             >失败:<font color=\"comment\">{2}</font>
             >如需查看报告可挂VPN，报告地址:<font color=\"comment\">{3}</font>
             [点击跳转到报告地址,需要挂VPN]({3})
             """.format(data_total, data_suc, data_fal, test_report_ad, name)
            }
        }

        headers = {'content-type': 'application/json'}
        diag = requests.post(url=bot_url, headers=headers, json=dateata)

        print(diag.text)
    else:
        print(1)


def new_timed_task_add(request):
    if request.method == 'GET':
        tille = "定时任务添加"
        forms = NewTimeTaskAddForm()
        return render(request, "web/chenge.html", {
            "form": forms,
            "tille": tille,
        }, )

    else:

        print(request.POST)
        form = NewTimeTaskAddForm(data=request.POST)  # 接收参数
        task_hour = form.data['hour']
        task_minute = form.data['minute']
        task_second = form.data['second']
        task_hour = form.data['hour']
        if form.is_valid():

            id_hour = form.data['tasks_time_name']
            d_weed =str( form.data['weed'])
            print(d_weed)
            print(type(d_weed))

            if form.data['tasks_method'] == "1":
                name_task = form.data['tasks_time_name']
                print(1)
                print("asdfasdfadf" + form.data['task_test_set'])
                if form.data['task_test_set'] != '' and d_weed != "0":
                        scheduler.add_job(
                        test,
                        'cron',
                        day_of_week=int(d_weed)-1,
                        hour=form.data['hour'],
                        minute=form.data['minute'],
                        second=form.data['second'],
                        id=name_task,
                        args=[form.data['task_test_set']],
                    )

                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] != '':
                    print("没有星期")

                    print(task_hour, task_minute, task_second)
                    num_se = int(task_hour) * 60 * 60 + int(task_minute) * 60 + int(task_second)

                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['task_test_set']],
                    )
                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] != '':
                    print("没有小时")

                    print(task_minute, task_second)
                    num_se = int(task_minute) * 60 + int(task_second)
                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['task_test_set']],
                    )
                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] == '' and form.data['second'] != '':
                    print("没有分钟")
                    num_se = int(task_second)

                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,
                        id=name_task,
                        args=[form.data['task_test_set']],
                    )

                else:

                    return render(request, "web/chenge.html", {"form": form})
            elif form.data['tasks_method'] == "0":

                name_task = form.data['tasks_time_name']
                scheduler.add_job(
                    test2,
                    'cron',
                    day_of_week=int(d_weed)-1,
                    hour=form.data['hour'],
                    minute=form.data['minute'],
                    second=form.data['second'],
                    id=name_task,

                )
            elif form.data['tasks_method'] == "2":
                print("进入娇艳")
                story_test_case_id = form.data['story_test_set']
                name_task = form.data['tasks_time_name']

                if form.data['story_test_set'] != '' and d_weed != "0":
                    scheduler.add_job(
                        test_story,
                        'cron',
                        day_of_week=int(d_weed)-1,
                        hour=form.data['hour'],
                        minute=form.data['minute'],
                        second=form.data['second'],
                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )

                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] != '':
                    print("没有星期")

                    print(task_hour, task_minute, task_second)
                    num_se = int(task_hour) * 60 * 60 + int(task_minute) * 60 + int(task_second)

                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] != '':
                    print("没有小时")


                    print(task_minute, task_second)
                    num_se = int(task_minute) * 60 + int(task_second)
                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] == '' and form.data['second'] != '':
                    print("没有分钟")

                    num_se = int(task_second)

                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,
                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
            form.save()
            return redirect('/new/timed/tasks/list/')
        else:
            return render(request, "web/chenge.html", {"form": form})



def scheduler_job_execution_list(request):
    if request.method == "GET":
        try:
            job_sql = """
                SELECT * FROM `webtoolsdb`.`django_apscheduler_djangojobexecution` ORDER BY `run_time` DESC LIMIT 0,1000
            """
            data = execute_query("default", job_sql)

            return render(request, "web/django_job_execution.html", {"data": data})
        except Exception as e:
            get_logger().error(e)
def scheduler_job_delet(request,nid):
    logger =logging.getLogger('django')

    try :
        if request.method == "GET":
            row_object=models.Customize_scheduled_Tasks.objects.filter(test_set_tasks_run_id=nid).first()
            if not  row_object:
                return redirect("/new/timed/tasks/list/")
        
            else:
                row_object_new=models.Customize_scheduled_Tasks.objects.filter(test_set_tasks_run_id=nid).values()
                logger.info("定时任务删除数据%s"%row_object_new)
                tasks_name_job=row_object_new[0]['tasks_time_name']
                scheduler.remove_job(job_id=tasks_name_job)

                models.Customize_scheduled_Tasks.objects.filter(test_set_tasks_run_id=nid).delete()
                return redirect("/new/timed/tasks/list/")
        else:
            return redirect("/new/timed/tasks/list/")
    except Exception as e:
        logger.error(e)

def scheduler_job_edit(request,nid):
    row_object=models.Customize_scheduled_Tasks.objects.filter(test_set_tasks_run_id=nid).first()
    tille ="定时任务修改"
    if request.method=="GET":
        form=  NewTimeTaskAddForm(instance=row_object)
        return render(request,"web/chenge.html",{"form":form,"tille":tille})
    else:
        row_object_new = models.Customize_scheduled_Tasks.objects.filter(test_set_tasks_run_id=nid).values()

        tasks_name_job = row_object_new[0]['tasks_time_name']
        form =  NewTimeTaskAddForm(data=request.POST,instance=row_object)
        task_request_methed=form.data['tasks_method']
        task_weed =form.data['weed']
        task_hour = form.data['hour']
        task_minute = form.data['minute']
        task_second = form.data['second']
        task_hour = form.data['hour']
        if form.is_valid():

            id_hour = form.data['tasks_time_name']
            d_weed =str( form.data['weed'])
            print(d_weed)
            print(type(d_weed))

            if form.data['tasks_method'] == "1":
                name_task = form.data['tasks_time_name']
                print(1)
                print("asdfasdfadf" + form.data['task_test_set'])
                if form.data['task_test_set'] != '' and d_weed != "0":
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test,
                        'cron',
                        day_of_week=int(d_weed)-1,
                        hour=form.data['hour'],
                        minute=form.data['minute'],
                        second=form.data['second'],
                        id=name_task,
                        args=[form.data['task_test_set']],
                    )

                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] != '':
                    print("没有星期")

                    print(task_hour, task_minute, task_second)
                    num_se = int(task_hour) * 60 * 60 + int(task_minute) * 60 + int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['task_test_set']],
                    )
                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] != '':
                    print("没有小时")

                    print(task_minute, task_second)
                    num_se = int(task_minute) * 60 + int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['task_test_set']],
                    )
                elif form.data['tasks_method'] == "1" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] == '' and form.data['second'] != '':
                    print("没有分钟")
                    num_se = int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test,
                        'interval',
                        seconds=num_se,
                        id=name_task,
                        args=[form.data['task_test_set']],
                    )

                else:

                    return render(request, "web/chenge.html", {"form": form})
            elif form.data['tasks_method'] == "0":

                name_task = form.data['tasks_time_name']
                scheduler.remove_job(job_id=tasks_name_job)
                scheduler.add_job(
                    test2,
                    'cron',
                    day_of_week=int(d_weed)-1,
                    hour=form.data['hour'],
                    minute=form.data['minute'],
                    second=form.data['second'],
                    id=name_task,

                )
            elif form.data['tasks_method'] == "2":
                print("进入娇艳")
                story_test_case_id = form.data['story_test_set']
                name_task = form.data['tasks_time_name']

                if form.data['story_test_set'] != '' and d_weed != "0":
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test_story,
                        'cron',
                        day_of_week=int(d_weed)-1,
                        hour=form.data['hour'],
                        minute=form.data['minute'],
                        second=form.data['second'],
                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )

                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] != '':
                    print("没有星期")

                    print(task_hour, task_minute, task_second)
                    num_se = int(task_hour) * 60 * 60 + int(task_minute) * 60 + int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] != '':
                    print("没有小时")


                    print(task_minute, task_second)
                    num_se = int(task_minute) * 60 + int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,

                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
                elif form.data['story_test_set'] != '' and form.data[
                    'tasks_method'] == "2" and d_weed == "0" and form.data['hour'] == '' and form.data[
                    'minute'] == '' and form.data['second'] != '':
                    print("没有分钟")

                    num_se = int(task_second)
                    scheduler.remove_job(job_id=tasks_name_job)
                    scheduler.add_job(
                        test_story,
                        'interval',
                        seconds=num_se,
                        id=name_task,
                        args=[form.data['story_test_set'], form.data['tasks_time_name']],
                    )
            form.save()
            return redirect('/new/timed/tasks/list/')
        else:
            return render(request, "web/chenge.html", {"form": form})
