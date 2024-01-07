from  django import  forms
import logging
from  webTools import models
class BootstrapModelFrom(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        logger=logging.getLogger('django')
        try:
            super().__init__(*args,**kwargs)
            for name,field in self.fields.items():
                if field.widget.attrs:
                    field.widget.attrs = {
                        'class': "form-control form-control-user ",
                    }
                else:
                    field.widget.attrs = {
                        'class': "form-control form-control-user ",
                        "placeholder": field.label,
                    }

        except Exception as  e:
            logger.error(e)
