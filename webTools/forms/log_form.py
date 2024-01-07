
from  webTools.public.bootstrap import BootstrapModelFrom

from  webTools import models

class LogNormalModelFrom(BootstrapModelFrom):

    class Meta:
        model =  models.OpLogs
        fields='__all__'

class LogModelFrom(BootstrapModelFrom):

    class Meta:
        model =  models.AccessTimeOutLogs
        fields='__all__'