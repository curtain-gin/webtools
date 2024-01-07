
from  webTools.public.bootstrap import BootstrapModelFrom

from  webTools import models

class SwaggerMangementAdd(BootstrapModelFrom):

    class Meta:
        model =  models.SwaggerTasks
        fields='__all__'
class SwaggerInterfaceInfoAdd(BootstrapModelFrom):
    class Meta:
        model =  models.Swagger_InterfaceInfo
        fields='__all__'

