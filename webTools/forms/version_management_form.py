from  django import  forms
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from  webTools.public.bootstrap import BootstrapModelFrom
from  webTools import models




class VersionManagementEdit(BootstrapModelFrom):

    class Meta:
        model = models.VersionManagement
        fields = '__all__'

class VersionManagementAdd(BootstrapModelFrom):

    class Meta:
        model = models.VersionManagement
        fields = '__all__'