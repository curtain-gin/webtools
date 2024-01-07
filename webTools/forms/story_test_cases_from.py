from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from webTools.public.bootstrap import BootstrapModelFrom
from webTools import models
from django.http.request import *


class StoryTeseCasesForm(BootstrapModelFrom):
    class Meta:
        model = models.Story_Test_Cases_Set
        fields = '__all__'


class StoryTeseCasesAddForm(BootstrapModelFrom):
    class Meta:
        model = models.Story_Test_Cases_Set
        fields = ['story_test_set_name']


"""
    story_test_case_id = models.AutoField(verbose_name="故事测试用例ID", primary_key=True)
    story_test_case_name = models.CharField(verbose_name="故事测试用例名称", max_length=100)
    test_report_url = models.CharField(verbose_name="故事测试请求地址", max_length=200)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    test_report_request_parameters = models.TextField(verbose_name="故事测试请求参数", max_length=5000)
    extract_the_response_value = models.CharField(verbose_name="提取响应值", max_length=100)
    verify_the_response_value = models.CharField(verbose_name="提取响应值", max_length=100)
    test_report_reponse_parameters=models.CharField(verbose_name="故事测试响应参数", max_length=5000)
    serial_number = models.IntegerField(verbose_name="序号",)

    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    story_test_case_id = models.ForeignKey(
        null=True,
        verbose_name="故事测试用例ID",
        to=Story_Test_Cases_Set,
        to_field="story_test_case_id",
        on_delete=models.CASCADE,
    )


"""


class StoryTeseCasesDataAddForm(BootstrapModelFrom):
    response_variable = forms.CharField(label='响应自定义变量', required=False,
                                        widget=forms.Textarea(attrs={'class': 'form-control', "rows": "5"}))
    sql_statement = forms.CharField(label='sql语句', required=False,
                                    widget=forms.Textarea(attrs={'class': 'form-control', "rows": "5"}))
    custom_variable = forms.CharField(label='自定义变量', required=False,
                                      widget=forms.Textarea(attrs={'class': 'form-control', "rows": "5"}))

    class Meta:
        model = models.Story_Test_Cases
        fields = ['story_test_case_name', 'test_report_url', 'request_method',
                  'test_report_request_parameters', 'extract_the_response_value',
                  'verify_the_response_value',
                  'environment_id', 'story_test_case_id', 'custom_variable', 'response_variable', 'sql_statement',
                  'sql_variable',  'story_test_set_id','serial_number',]

    def clean_sql_statement(self):
        sql_statement_old = self.cleaned_data.get("sql_statement")

        sql_statement = str(self.cleaned_data.get("sql_statement")).lower()
        print(sql_statement)
        if "alter" in sql_statement or "show" in sql_statement or "insert" in sql_statement or\
                "delete" in sql_statement or "updata" in sql_statement or "drop " in sql_statement or\
                "use" in sql_statement or "create" in sql_statement or "desc" in sql_statement or \
            "update" in sql_statement or "rename" in sql_statement:
            raise ValidationError("无效SQL 只支持select查询")
        else:
            return sql_statement_old

    def clean_serial_number(self):
        serial_number = int(self.cleaned_data.get("serial_number"))
        print(self.cleaned_data)
        print(1)
        story_test_set_id_ndn = self.cleaned_data.get("story_test_set_id")
        serial_number = int(self.cleaned_data.get("serial_number"))

        environment_id = self.cleaned_data.get("environment_id")
        print(2)
        print(serial_number)
        print(story_test_set_id_ndn)
        print(environment_id)

        if serial_number !="" and story_test_set_id_ndn !=None:
            data_calt=models.Story_Test_Cases.objects.filter(story_test_set_id=story_test_set_id_ndn).values().order_by(
                    'serial_number')
            print(data_calt)
            print(len(data_calt))
            data_list=[  data_calt[i]["serial_number"] for  i in range(len(data_calt))]
            if int(serial_number) > data_list[-1]+1  :
                raise ValidationError("当前序号最大为%s，请填写%s"%(data_list[-1],data_list[-1]+1))
            else:
                return serial_number
        elif int(serial_number) ==  0:
            raise ValidationError("不能从0开始")
        else:
            return serial_number

