from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from webTools.public.bootstrap import BootstrapModelFrom
from webTools import models
from django.http.request import *


class ItemComparisonForm(BootstrapModelFrom):
    class Meta:
        model = models.item_comparison
        fields = '__all__'
