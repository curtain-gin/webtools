from django import forms
from webTools.public.bootstrap import BootstrapModelFrom
from webTools import models

class CaseAddFrom(BootstrapModelFrom):
    project = forms.CharField(label='关联项目', required=True,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    root = forms.CharField(label='脚本路径', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    branch_name = forms.CharField(label='分支名', required=True,
                                  widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    creator = forms.CharField(label='创建者', required=True,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label='备注', required=False,
                             widget=forms.Textarea(attrs={'class': 'form-control', "rows": "5"}))

    class Meta:
        model = models.Cases
        fields = ['project', 'root', 'branch_name', 'creator', 'remark']


class CaseEditFrom(BootstrapModelFrom):
    project = forms.CharField(label='关联项目', required=True,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    root = forms.CharField(label='脚本路径', widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    branch_name = forms.CharField(label='分支名', required=True,
                                  widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    creator = forms.CharField(label='创建者', required=True,
                              widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label='备注', required=False,
                             widget=forms.Textarea(attrs={'class': 'form-control', "rows": "5"}))

    class Meta:
        model = models.Cases
        fields = ['project', 'root', 'branch_name', 'creator', 'remark']
