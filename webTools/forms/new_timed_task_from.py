from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from webTools.public.bootstrap import BootstrapModelFrom
from webTools import models


class NewTimeTaskAddForm(BootstrapModelFrom):
    class Meta:
        model = models.Customize_scheduled_Tasks
        fields = '__all__'
    #
    # choice_weed = (
    #     (0, "未选择"),
    #     (1, "星期一"),
    #     (2, "星期二"),
    #     (3, "星期三"),
    #     (4, "星期四"),
    #     (5, "星期五"),
    #     (6, "星期六"),
    #     (7, "星期日"),
    # )
    #
    # # weed = forms.CharField(label='星期',
    # #                        widget=forms.Select(), choices=choice_weed
    # #                        required=False,)
    # weed = forms.ChoiceField(label='执行时间', widget=forms.Select(), choices=choice_weed,
    #                           initial=choice_weed[0],required=False,)
    # hour =forms.IntegerField(label='小时',
    #                           widget=forms.widgets.NumberInput(),
    #                           required=False,)
    # minute = forms.IntegerField(label='分钟',
    #                        widget=forms.widgets.NumberInput(),
    #                        required=False, )
    # second = forms.IntegerField(label='秒',
    #                          widget=forms.widgets.NumberInput(),
    #                          required=False, )
    def clean_hour(self):


        hour = self.cleaned_data.get("hour")
        print(hour)
        if hour !=None:
            if int(hour) > 23 :
                raise ValidationError("最大23，23小时请填写0")
            return hour




    def clean_minute(self):
        minute = self.cleaned_data.get("minute")
        print(minute)

        if minute !=None:
            if int(minute) > 59 :
                raise ValidationError("最大59，")
            return minute


    def clean_second(self):
        second = self.cleaned_data.get("second")
        minute = self.cleaned_data.get("minute")
        hour = self.cleaned_data.get("hour")
        print(second)
        if second !=None:
            if int(second) > 59  :
                raise ValidationError("最大59，")
            return second
        else:
            raise ValidationError("填写时间如选择时分秒执行就需要填写时分秒，选择分秒，就必须填写分秒，秒为必填单以此类推，（如需星期时分秒必填）")
    def clean_story_test_set(self):
        if  self.cleaned_data.get("tasks_method") == 2:
            story_test_set_id=self.cleaned_data.get("story_test_set")
            print("sdsfd%s"%story_test_set_id)
            if story_test_set_id==None:
                raise ValidationError("请选择有序测试集任务")
            else:
                return story_test_set_id
    def clean_task_test_set(self):
        if  self.cleaned_data.get("tasks_method") == 1:
            print()
            print(self.cleaned_data)
            test_set_tasks_id=self.cleaned_data.get("task_test_set")
            print("sdsfd%s"%test_set_tasks_id)
            if test_set_tasks_id==None:
                raise ValidationError("请选择无序测试集任务")
            else:
                return test_set_tasks_id
    def clean_weed(self):
        weed = self.cleaned_data.get("weed")
        if  self.cleaned_data.get("tasks_method") == 0:
            print()
            print(self.cleaned_data)

            print("sdsfd%s"%weed)
            if weed == 0 or weed==None or weed=="":
                raise ValidationError("请选择星期")
            else:
                return weed
        else:
            return weed

