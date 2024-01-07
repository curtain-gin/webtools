from  django import  forms
from  webTools import models
from  webTools.public.bootstrap import BootstrapModelFrom
class PermissionAdd(BootstrapModelFrom):
    role = forms.CheckboxSelectMultiple()

    class Meta:
        model =models.Role
        fields='__all__'

class PermissionEdit(BootstrapModelFrom):
    role = forms.CheckboxSelectMultiple()
    class Meta:
        model =models.Role
        fields='__all__'
