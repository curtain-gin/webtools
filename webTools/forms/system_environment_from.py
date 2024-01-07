from  django import  forms
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from  webTools.public.bootstrap import BootstrapModelFrom
from  webTools import models



class SystemEnvironmentAddForm(BootstrapModelFrom):
    environment_hander =forms.CharField(label='环境请求头',
                                     widget=forms.Textarea(),
                                  required=True,)
    class Meta:
        model = models.SystemEnvironment
        fields = '__all__'