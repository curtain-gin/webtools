from  django import  forms
from  webTools import models
from  webTools.public.bootstrap import BootstrapModelFrom
class PermissionPathAdd(BootstrapModelFrom):
    role = forms.CheckboxSelectMultiple()

    class Meta:
        model =models.PermissionPath
        fields='__all__'

class PermissionPathedit(BootstrapModelFrom):
    role = forms.CheckboxSelectMultiple()

    class Meta:
        model =models.PermissionPath
        fields='__all__'
