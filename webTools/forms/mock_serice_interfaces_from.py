from  django import  forms
from  webTools import models
from  webTools.public.bootstrap import BootstrapModelFrom
from django.core.exceptions import ValidationError

import json
class MockServiceInterfaceAdd(BootstrapModelFrom):

    class Meta:
        model =models.Mock_Service_Interface
        fields='__all__'

class MockServiceInterfaceEdit(BootstrapModelFrom):
    """
    mock服务编辑
    """

    class Meta:
        model =models.Mock_Service_Interface
        fields=['interface_name','request_parameters','response_parameters','in_field_description','reponse_in_field_description']

