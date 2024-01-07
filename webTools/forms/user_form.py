from  django import  forms
from  django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from  webTools.public.bootstrap import BootstrapModelFrom
from django.forms import widgets
from  webTools import models
from webTools.public.encrypt import md5


class RegisterModelFrom(BootstrapModelFrom):

    mobile_phone =mmobile_validation = forms.CharField(label='手机号', validators=[
    RegexValidator(r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}', '手机号格式错误')])
    password =forms.CharField(label='密码',widget=forms.PasswordInput())
    confirem_password =forms.CharField(label='重复密码',widget=forms.PasswordInput())
    code= forms.CharField(label='验证码')

    class Meta:
        model =  models.UserAppInfo
        fields='__all__'
class LoginModelFrom(BootstrapModelFrom):


    mobile_phone =forms.CharField(label='手机号',
                                  validators=[RegexValidator(r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}','手机号格式错误')],
                                  required=True,)
    password =forms.CharField(label='密码',
                              widget=forms.PasswordInput(),
                              required=True,)
    # code = forms.CharField(label='验证码',
    #                            widget=forms.TextInput(),
    #                            required=True, )
    class Meta:
        model =  models.UserAppInfo
        # fields=['mobile_phone','password','code']
        fields=['mobile_phone','password'   ]




class UserAddFrom(BootstrapModelFrom):
    mobile_phone = forms.CharField(label='手机号',
                                   validators=[RegexValidator(
                                       r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}',
                                       '手机号格式错误')],
                                   required=True,
                                   widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
                                   )

    confirem_password = forms.CharField(label='重复密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password=forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # role =forms.SelectMultiple()
    # role =forms.CharField(label='角色',widget=forms.CheckboxSelectMultiple())
    role =forms.CheckboxSelectMultiple()

    class Meta:
        model = models.UserAppInfo
        fields = ['username','email','mobile_phone','password','confirem_password','role']

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirem_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirem_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm
class UserEditFrom(BootstrapModelFrom):
    mobile_phone = forms.CharField(label='手机号',
                                   validators=[RegexValidator(
                                       r'^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}',
                                       '手机号格式错误')],
                                   widget=forms.widgets.TextInput(attrs={'class': 'form-control'}),
                                   required=True, )

    username=forms.CharField(label='用戶名',disabled=True)
    # confirem_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    # password = forms.CharField(label='密码', widget=forms.PasswordInput(), attrs={'class': 'form-control'})
    role = forms.CheckboxSelectMultiple()
    class Meta:
        model = models.UserAppInfo
        fields = ['username', 'email', 'mobile_phone','role']



class UserRevise(BootstrapModelFrom):
    confirem_password = forms.CharField(label='重复密码', widget=forms.PasswordInput())
    password=forms.CharField(label='密码', widget=forms.PasswordInput())

    class Meta:
        model =  models.UserAppInfo
        fields=['password','confirem_password']
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    def clean_confirem_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirem_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        # 返回什么，此字段以后保存到数据库就是什么。
        return confirm