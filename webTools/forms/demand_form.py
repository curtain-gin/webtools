from django import forms
from webTools.public.bootstrap import BootstrapModelFrom

from webTools import models


class DemandAddFrom(BootstrapModelFrom):
    choice_status = (
        (0, '待处理'),
        (1, '处理中'),
        (2, '已完成'),
        (3, '不处理'),
    )

    title = forms.CharField(label='需求描述', required=True,
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))

    detail = forms.CharField(label='详细说明', required=False,
                             widget=forms.widgets.Textarea(attrs={'class': 'form-control'}))

    reporter = forms.CharField(label='提出人', required=True,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='状态', widget=forms.Select(attrs={'class': 'form-control'}), choices=choice_status,
                               initial=choice_status[0])

    Solver = forms.CharField(label='处理人', required=True,
                             widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label='备注', required=False, widget=forms.Textarea(attrs={'class': 'form-control',"rows": "5"}))

    class Meta:
        model = models.Demands
        fields = ['title', 'detail', 'reporter', 'status', 'Solver', 'remark']


class DemandEditFrom(BootstrapModelFrom):
    choice_status = (
        (0, '待处理'),
        (1, '处理中'),
        (2, '已完成'),
        (3, '不处理'),
    )

    title = forms.CharField(label='需求描述', required=True,
                            widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    detail = forms.CharField(label='详细说明', required=False, widget=forms.Textarea(attrs={'class': 'form-control'}))
    reporter = forms.CharField(label='提出人', required=True,
                               widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(label='状态', widget=forms.Select(attrs={'class': 'form-control'}), choices=choice_status,
                               initial=choice_status[0])

    Solver = forms.CharField(label='处理人', required=True,
                             widget=forms.widgets.TextInput(attrs={'class': 'form-control'}))
    remark = forms.CharField(label='备注',required=False, widget=forms.Textarea(attrs={'class': 'form-control',"rows": "5"}))

    class Meta:
        model = models.Demands
        fields = ['title', 'detail', 'reporter', 'status', 'Solver', 'remark']
