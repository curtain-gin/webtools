import random
import json
import requests
import pickle

from webTools.public.identity import IdNumber
from webTools.public.is_json import JsonBUF, JudgmentType
from webTools.public.daba_tuple_to_dict import execute_query


class Story_Test():
    """
    有序测试用例数据处理
    """
    @classmethod
    def fixed_custom_functions_list(self, data_custom_variable):
        """
           S.fixed_custom_functions_list(data_custom_variable) -> list
           Return  a dictionary of fixed custom functions
           """
        print(data_custom_variable)
        response_variable_dict = {}
        custom_variable_list = []
        for i in range(len(data_custom_variable)):

            if data_custom_variable[i]['custom_variable'] == None:
                continue
            else:
                custom_variable_list.append(data_custom_variable[i]['custom_variable'])
                daiga = (data_custom_variable[i]['custom_variable']).split('////')
                for ii in daiga:
                    print(ii)
                    if ii == '':
                        continue
                    else:
                        asdfadg = ii.split('///')
                        response_variable_dict[asdfadg[0]] = asdfadg[1]
        #print("最后抽取自定义函数, 自定义固定函数%s" % response_variable_dict)
        return response_variable_dict

    @classmethod
    def custom_modified_requests(self, response_variable_dict, test_report_request_parameters):

        """
                   S.custom_modified_requests(response_variable_dict,test_report_request_parameters) -> dict
                   Return a post-replace request dictionary
        """
        while "^" in str(test_report_request_parameters):
            olde_data = str(test_report_request_parameters)
            start_num = olde_data.find('^')
            stop_num = olde_data[start_num:].find('"')
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

        print("修改后请求{0}".format(test_report_request_parameters))
        return test_report_request_parameters

    @classmethod
    def response_variable_add(self, response_variable_dict, test_case_reponse, response_variable):
        """
                           S.custom_modified_requests(response_variable_dict,test_case_reponse,response_variable) -> dict
                           Return  a dictionary of custom functions
        """
        print(response_variable_dict)
        print("前职工%s" % response_variable.split('////'))

        response_variable_list_all = response_variable.split('////')

        for reponse_ver in response_variable_list_all[:-1]:
            if isinstance(test_case_reponse, list):
                request_txt_cope = test_case_reponse
            else:
                request_txt_cope = test_case_reponse.json()
            response_variable_list = reponse_ver.split('-')
            print("hanshu %s" % response_variable_list)
            response_variable_list_name = response_variable_list[0]
            response_variable_list_value = response_variable_list[1]
            print(response_variable_list_name)
            print(response_variable_list_value)
            diifg = []
            ndd = ""
            for iii in response_variable_list_value:

                if iii == "[":
                    ndd = ''

                elif iii == "]":
                    diifg.append(ndd)
                else:
                    ndd = ndd + iii
                print(diifg)

            for sdt in range(len(diifg)):
                print(sdt)
                print(diifg[sdt])
                if JudgmentType.is_int(diifg[sdt]):
                    print(1)
                    request_txt_cope = request_txt_cope[int(diifg[sdt]) - 1]
                    print(request_txt_cope)
                else:
                    print(0)
                    request_txt_cope = request_txt_cope[diifg[sdt]]
                    print(request_txt_cope)
            response_variable_dict[response_variable_list_name] = request_txt_cope
        print("添加的自定义函数字典%s" % response_variable_dict)
        return response_variable_dict

    @classmethod
    def test_case_validation_results(self, **kwargs):
        """
          S.custom_modified_requests(**kwargs)) -> dict
          Return  a list of length 2, one of which is the number of checksums and the other is the number of checksums
        """
        print("进入校验")

        print(kwargs["extract_the_response_value"], kwargs["verify_the_response_value"])
        extract_the_response_value = kwargs["extract_the_response_value"]
        test_case_reponse = kwargs["test_case_reponse"]
        verify_the_response_value = kwargs["verify_the_response_value"]

        is_customize_the_function = kwargs["is_customize_the_function"]
        if is_customize_the_function == 1:
            response_variable_dict = kwargs["response_variable_dict"]

        extract_the_response_value = extract_the_response_value.split("////")

        print("返回值%s" % test_case_reponse.text)
        print(type(test_case_reponse.text))

        offff = 0

        numm = 0
        print(extract_the_response_value)
        for ii in extract_the_response_value[:-1]:

            request_txt_cope = json.loads(test_case_reponse.text)
            print(request_txt_cope)

            ndd = ""

            diifg = []
            for iii in ii:
                if iii == "[":
                    ndd = ''

                elif iii == "]":
                    diifg.append(ndd)


                else:
                    ndd = ndd + iii
            print(diifg)
            for sdt2 in range(len(diifg)):
                print(diifg[sdt2])

            for sdt in range(len(diifg)):
                print(JudgmentType.is_int(diifg[sdt]))
                if JudgmentType.is_int(diifg[sdt]):

                    print(1)
                    request_txt_cope = request_txt_cope[int(diifg[sdt]) - 1]
                    print(request_txt_cope)
                else:
                    print(0)
                    print(request_txt_cope)
                    print(type(request_txt_cope))
                    print(diifg[sdt])

                    request_txt_cope = request_txt_cope[diifg[sdt]]
                    print(request_txt_cope)
            print(type(numm))

            verify_the_response_value_va = str(verify_the_response_value.split("////")[numm])
            if "-" in str(verify_the_response_value_va):
                verify_list = verify_the_response_value_va.split("-")
                verify_the_response_value_vaa = verify_list[0]
                print("验证书%s" % verify_the_response_value_vaa)
                print("返会值%s" % str(request_txt_cope))
                ver_path = int(verify_list[1])

                if is_customize_the_function == 1 and "^" in verify_the_response_value_vaa and response_variable_dict[
                    verify_the_response_value_vaa[1:]] == request_txt_cope:
                    print("123123123ddududududududududu")
                    print("sql验证书%s" % str(response_variable_dict[verify_the_response_value_vaa[1:]]))
                    print("sql返会值%s" % str(request_txt_cope))
                    offff = offff + 1
                elif str(request_txt_cope) != None and verify_the_response_value_vaa == "!=NULL":
                    offff = offff + 1

                elif str(request_txt_cope) == None and verify_the_response_value_vaa == "NULL":
                    offff = offff + 1

                elif verify_the_response_value_vaa != str(request_txt_cope):
                    offff = offff

                    rult = [offff, len(extract_the_response_value), ver_path]
                    return rult
                else:
                    offff = offff + 1
                numm += 1


            else:

                verify_the_response_value_va = str(verify_the_response_value.split("////")[numm])
                if is_customize_the_function == 1 and "^" in verify_the_response_value_va and response_variable_dict[
                    verify_the_response_value_va[1:]] == request_txt_cope:
                    print("123123123ddududududududududu")
                    print("sql验证书%s" % str(response_variable_dict[verify_the_response_value_va[1:]]))
                    print("sql返会值%s" % str(request_txt_cope))
                    offff = offff + 1
                elif str(request_txt_cope) != None and verify_the_response_value_va == "!=NULL":
                    offff = offff + 1
                elif str(request_txt_cope) == None and verify_the_response_value_va == "NULL":
                    offff = offff + 1
                elif verify_the_response_value_va != str(request_txt_cope):
                    offff = offff
                else:
                    offff = offff + 1
                numm += 1
        ver_path = True
        print("校验{0} hou {1}".format(offff, len(extract_the_response_value)))
        rult = [offff, len(extract_the_response_value), ver_path]
        return rult

    @classmethod
    def sql_custom_variables_dict(self, **kwargs):
        """
          S.sql_custom_variables_dict(**kwargs) -> dict
          Return A mapping dictionary that returns the results of SQL execution
        """
        sql_statement = kwargs["sql_statement"]
        sql_variable = kwargs["sql_variable"]
        response_variable_dict = kwargs["response_variable_dict"]

        env_num = "default"

        result = execute_query(env_num, sql_statement)
        dd = json.dumps(str(result))

        response_variable_dict = Story_Test.response_variable_add(response_variable_dict, result, sql_variable)
        return response_variable_dict

    @classmethod
    def interface_data_dictionary(self, *args):
        """
                 S.interface_data_dictionary(self,*args) -> dict

               """

        story_test_set_list = args[0]
        story_test_set_dict = {}
        story_ng_list = []
        for i in range(len(story_test_set_list)):
            story_test_set_dict[i] = story_test_set_list[i]
            story_ng_list.append(i)

        return story_test_set_dict, story_ng_list

    @classmethod
    def story_original_sorting(self, *args):
        """
                 S.story_original_sorting(self,*args) -> list

        """
        story_data = args[0]
        now_data_id = args[1]
        serial_number_in = args[2]
        stoy_lsit_nn = [story_data[i]["story_test_case_id"] for i in range(len(story_data))]
        inde_ex = stoy_lsit_nn.index(now_data_id)
        stoy_lsit_datae = stoy_lsit_nn[inde_ex]
        stoy_lsit_nn.pop(inde_ex)
        stoy_lsit_nn.insert(int(serial_number_in) - 1, stoy_lsit_datae)
        return stoy_lsit_nn
