import json
from django import forms
from webTools.public.bootstrap import BootstrapModelFrom
from webTools import models
from django.core.exceptions import ValidationError


class InterfaceInfoAddForm(BootstrapModelFrom):

    request_parameters = forms.CharField(
        label="请求参数",
        widget=forms.Textarea(),
        required=False,
    )
    response_parameters = forms.CharField(
        label="响应参数",
        widget=forms.Textarea(),
        required=False,
    )

    class Meta:
        model = models.InterfaceInfo
        fields = "__all__"
    def clean_request_parameters(self):

        try:
            json.loads(self.request_parameters)

        except Exception as e:
            raise ValidationError("请填写json格式")
        return  self.request_parameters
    def clean_response_parameters(self):

        try:
            json.loads(self.response_parameters)

        except Exception as e:
            raise ValidationError("请填写json格式")
        return  self.response_parameters
