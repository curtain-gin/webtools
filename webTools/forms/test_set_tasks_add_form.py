from  django import  forms
from  webTools import models
from  webTools.public.bootstrap import BootstrapModelFrom
class TestTasksAdd(BootstrapModelFrom):

    class Meta:
        model =models.Test_Set_Tasks
        fields='__all__'
