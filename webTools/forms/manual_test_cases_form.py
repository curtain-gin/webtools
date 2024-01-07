from  django import  forms
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from  webTools.public.bootstrap import BootstrapModelFrom
from  webTools import models


class ManualTestCasesAddForm(BootstrapModelFrom):

    class Meta:
        model = models.ManualTestCases
        fields= ["test_cases_name","request_url","request_method",
                 "request_parameters","Extract_the_response_value","Verify_the_response_value",
                 "environment_id","test_set_tasks"]
    def __init__(self, *args, **kwargs):
        super(ManualTestCasesAddForm, self).__init__(*args, **kwargs)
        self.fields['test_set_tasks'].required = False
