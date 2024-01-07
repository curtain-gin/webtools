from  django import  forms
from django.core.exceptions import ValidationError

from  datetime import datetime

from  webTools.public import  constant as const
from webTools.public.logger import get_logger

class OrderDataFrom(forms.Form):
    city_ord = forms.CharField(required=False,label='城市',max_length=32,widget=forms.widgets.TextInput(attrs={'class': 'form-control' ,}))
    year_ord = forms.CharField(required=False,label='年份',max_length=8,widget=forms.widgets.TextInput(attrs={'class': 'form-control',}  ))
    age_ord = forms.CharField(required=False,label='年龄',max_length=3,widget=forms.widgets.NumberInput(attrs={'class': 'form-control' ,}  ))
    num_ord = forms.CharField(required=False,label='自定义条数',max_length=10,widget=forms.widgets.NumberInput(attrs={'class': 'form-control' ,}  ))

    def clean_city_ord(self):
        get_logger().info('订单生成校验城市')
        city_ord = str(self.cleaned_data.get("city_ord"))
        city_list = []
        for i, o in const.AREA_INFO.items():
            if city_ord in o:
                city_list.append(i)
        if len(city_list) <1 or city_ord=='' :

            raise ValidationError("请填写正确地区")
        else:
            return city_ord
    def clean_year_ord(self):
        get_logger().info('订单生成校验年份')
        year_ord = self.cleaned_data.get("year_ord")
        # try:
        #     datae_time=datetime.strptime("%s" % year_ord, "%Y%m%d")
        #
        # except:
        #     raise ValidationError("请填写正确年月日 例如19880101")
        return  year_ord
    def clean_age_ord(self):
        get_logger().info('订单生成校验年龄')
        age_ord = self.cleaned_data.get("age_ord")
        # if age_ord=='':
        #     raise ValidationError("请填写正确年龄")
        # # elif age_ord =='' :
        # elif int(age_ord) >200:
        #     raise ValidationError("年龄过大")
        # else:
        return age_ord
    def clean_num_ord(self):
        get_logger().info('订单生成校验条数')
        num_ord = self.cleaned_data.get("num_ord")
        if num_ord == '':
            raise ValidationError("请填写正确条数")
        # elif age_ord =='' :
        elif int(num_ord) > 5000:
            raise ValidationError("最大条数5000条")
        else:
            return num_ord


