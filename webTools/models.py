from django.db import models


# Create your models here.


class Role(models.Model):
    """角色表"""

    role_id = models.AutoField(verbose_name="角色ID", primary_key=True)
    role_name = models.CharField(verbose_name="角色名字", max_length=32)

    def __str__(self):
        return self.role_name


class UserAppInfo(models.Model):
    """用户表"""

    user_id = models.AutoField(verbose_name="用户id", primary_key=True)
    username = models.CharField(verbose_name="用户名", max_length=32)
    email = models.EmailField(verbose_name="邮箱", max_length=32)
    mobile_phone = models.CharField(verbose_name="手机号", max_length=11)
    password = models.CharField(verbose_name="密码", max_length=32)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.username


class PermissionPath(models.Model):
    """权限路径"""

    permission_path_id = models.AutoField(
        verbose_name="权限路径id",
        primary_key=True,
    )
    permission_path_name = models.CharField(verbose_name="权限名称", max_length=100)
    permission_path = models.CharField(verbose_name="权限路径", max_length=200)
    role = models.ManyToManyField(Role)


class OpLogs(models.Model):
    """日志操作表"""

    log_id = models.AutoField(primary_key=True)
    re_time = models.CharField(max_length=32, verbose_name="请求时间")
    re_user = models.CharField(max_length=32, verbose_name="操作人")
    re_ip = models.CharField(max_length=32, verbose_name="请求IP")

    permission_path_id = models.ForeignKey(
        verbose_name="权限路径id",
        to=PermissionPath,
        to_field="permission_path_id",
        on_delete=models.CASCADE,
    )
    re_method = models.CharField(max_length=11, verbose_name="请求方法")
    re_content = models.TextField(null=True, verbose_name="请求参数")
    rp_content = models.TextField(null=True, verbose_name="响应参数")
    access_time = models.IntegerField(verbose_name="响应耗时/ms")


class AccessTimeOutLogs(models.Model):
    """超时操作日志表"""

    out_log_id = models.AutoField(primary_key=True)
    re_time = models.CharField(max_length=32, verbose_name="请求时间")
    re_user = models.CharField(max_length=32, verbose_name="操作人")
    re_ip = models.CharField(max_length=32, verbose_name="请求IP")
    permission_path_id = models.ForeignKey(
        verbose_name="权限路径id",
        to=PermissionPath,
        to_field="permission_path_id",
        on_delete=models.CASCADE,
    )
    re_method = models.CharField(max_length=11, verbose_name="请求方法")
    re_content = models.TextField(null=True, verbose_name="请求参数")
    rp_content = models.TextField(null=True, verbose_name="响应参数")
    access_time = models.IntegerField(verbose_name="响应耗时/ms")


class Demands(models.Model):
    """需求表"""

    choice_status = (
        (0, "待处理"),
        (1, "处理中"),
        (2, "已完成"),
        (3, "不处理"),
    )
    demand_id = models.AutoField(verbose_name="需求id", primary_key=True)
    title = models.CharField(verbose_name="需求描述", max_length=500)
    detail = models.CharField(verbose_name="详细说明", max_length=1000)
    reporter = models.CharField(verbose_name="提出人", max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(verbose_name="状态", choices=choice_status)
    Solver = models.CharField(verbose_name="处理人", max_length=10)
    remark = models.CharField(verbose_name="备注", max_length=100)


class Defects(models.Model):
    """问题表"""

    choice_status = (
        (0, "待处理"),
        (1, "处理中"),
        (2, "已完成"),
        (3, "不处理"),
    )
    defect_id = models.AutoField(verbose_name="问题id", primary_key=True)
    module = models.CharField(verbose_name="所属工具模块", max_length=500)
    detail = models.CharField(verbose_name="问题描述", max_length=1000)
    expected_results = models.CharField(verbose_name="预期结果", max_length=1000)
    actual_results = models.CharField(verbose_name="实际结果", max_length=1000)
    reporter = models.CharField(verbose_name="提出人", max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(verbose_name="状态", choices=choice_status)
    Solver = models.CharField(verbose_name="处理人", max_length=10)
    remark = models.CharField(verbose_name="备注", max_length=100)


class Suggestions(models.Model):
    """建议表"""

    choice_status = (
        (0, "待处理"),
        (1, "处理中"),
        (2, "已完成"),
        (3, "不处理"),
    )
    suggest_id = models.AutoField(verbose_name="建议id", primary_key=True)
    module = models.CharField(verbose_name="所属工具模块", max_length=500)
    detail = models.CharField(verbose_name="建议描述", max_length=1000)
    reporter = models.CharField(verbose_name="提出人", max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(verbose_name='状态', choices=choice_status)
    Solver = models.CharField(verbose_name='处理人', max_length=10)
    remark = models.CharField(verbose_name='备注', max_length=100)


class Cases(models.Model):
    """ 提交脚本记录表"""
    case_id = models.AutoField(verbose_name='提交记录id', primary_key=True)
    project = models.CharField(verbose_name='所属项目', max_length=500)
    root = models.CharField(verbose_name='代码路径', max_length=1000)
    branch_name = models.CharField(verbose_name='分支名', max_length=10)
    create_time = models.DateTimeField(auto_now_add=True)
    creator = models.CharField(verbose_name='创建人', max_length=10)
    remark = models.CharField(verbose_name='备注', max_length=100)


class SystemEnvironment(models.Model):
    """环境表"""

    environment_id = models.AutoField(verbose_name="环境id", primary_key=True)
    environment_name = models.CharField(verbose_name="环境名", max_length=100)
    environment_url = models.CharField(verbose_name="服务url", max_length=100)
    swagger_url = models.CharField(verbose_name="swagger服务url", max_length=100)
    environment_hander = models.CharField(verbose_name="环境请求头", max_length=1000)
    download_address = models.CharField(verbose_name="下载地址", max_length=1000)

    def __str__(self):
        return self.environment_name


class SwaggerTasks(models.Model):
    """swagger任务表"""

    swagger_tasks_id = models.AutoField(verbose_name="swagger任务id", primary_key=True)
    swagger_tasks_name = models.CharField(verbose_name="swagger任务名称", max_length=100)
    swagger_json_addres = models.CharField(
        verbose_name="swagger json地址", max_length=100
    )
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )


class ScheduledTasks(models.Model):
    """定时任务表"""

    scheduled_tasks_id = models.AutoField(verbose_name="定时任务id", primary_key=True)
    scheduled_tasks_name = models.CharField(verbose_name="定时任务名称", max_length=32)
    timed_task_execution_time = models.CharField(verbose_name="定时任务时间", max_length=10)
    whether_to_loop_or_not = models.IntegerField(
        verbose_name="循环时间",
    )

    def __str__(self):
        return self.scheduled_tasks_name


class VersionManagement(models.Model):
    """版本表"""

    version_id = models.AutoField(verbose_name="版本ID", primary_key=True)
    version_name = models.CharField(verbose_name="版本名称", max_length=32)
    version_number = models.CharField(verbose_name="版本号", max_length=32)
    creat_time = models.CharField(verbose_name="创建时间", max_length=32)
    creat_user = models.CharField(verbose_name="创建人", max_length=32)
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    download_address = models.CharField(verbose_name="下载地址", max_length=1000, default="无", null=True, blank=True)

    def __str__(self):
        return self.version_name


class InterfaceInfo(models.Model):
    """测试接口表"""

    interface_id = models.AutoField(verbose_name="接口ID", primary_key=True)
    interface_name = models.CharField(verbose_name="接口名称", max_length=500)
    request_url = models.CharField(verbose_name="请求地址", max_length=500)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    request_parameters = models.CharField(verbose_name="请求参数", max_length=5000)
    response_parameters = models.CharField(verbose_name="响应参数", max_length=5000)
    version_id = models.ForeignKey(
        null=True,
        verbose_name="版本id",
        to=VersionManagement,
        to_field="version_id",
        on_delete=models.CASCADE,
    )
    creat_user = models.CharField(verbose_name="创建人", max_length=32)
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    choice_add_type = (
        (0, "手动"),
        (1, "同步"),
    )
    interface_add_type = models.IntegerField(
        verbose_name="添加类型", choices=choice_add_type
    )
    in_field_description = models.TextField(verbose_name="请求注释", max_length=20000)
    reponse_in_field_description = models.TextField(verbose_name="响应注释", max_length=20000)


class Mock_Service_Interface(models.Model):
    """mock服务表"""

    mock_service_id = models.AutoField(verbose_name="mock接口ID", primary_key=True)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    interface_name = models.CharField(verbose_name="接口名称", max_length=1000)
    request_url = models.CharField(verbose_name="请求地址", max_length=500)
    request_parameters = models.CharField(verbose_name="请求参数", max_length=5000)
    response_parameters = models.TextField(verbose_name="响应参数", max_length=300000)

    choice_add_type = (
        (0, "手动"),
        (1, "同步"),
    )
    interface_add_type = models.IntegerField(
        verbose_name="添加类型", choices=choice_add_type
    )
    in_field_description = models.TextField(verbose_name="请求注释", max_length=20000)
    reponse_in_field_description = models.TextField(verbose_name="响应注释", max_length=20000)


class Swagger_InterfaceInfo(models.Model):
    """swagger接口表"""

    interface_id = models.AutoField(verbose_name="接口ID", primary_key=True)
    interface_name = models.CharField(verbose_name="接口名称", max_length=200)
    request_url = models.CharField(verbose_name="请求地址", max_length=200)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    request_parameters = models.TextField(verbose_name="请求参数", max_length=30000)
    response_parameters = models.TextField(verbose_name="响应参数", max_length=30000)
    version_id = models.ForeignKey(
        null=True,
        verbose_name="版本id",
        to=VersionManagement,
        to_field="version_id",
        on_delete=models.CASCADE,
    )
    creat_user = models.CharField(verbose_name="创建人", max_length=32)
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    choice_add_type = (
        (0, "手动"),
        (1, "同步"),
    )
    interface_add_type = models.IntegerField(
        verbose_name="添加类型", choices=choice_add_type
    )


class Test_Set_Tasks(models.Model):
    """测试集任务"""
    test_set_tasks_id = models.AutoField(verbose_name="测试集任务ID", primary_key=True)
    test_set_tasks_name = models.CharField(verbose_name="测试集任务名", max_length=200)

    def __str__(self):
        return self.test_set_tasks_name


class Webtools_Scheduled_Tasks(models.Model):
    """平台定时任务"""
    webtools_scheduled_tasks_id = models.AutoField(verbose_name="平台定时任务ID", primary_key=True)
    webtools_scheduled_tasks_name = models.CharField(verbose_name="平台定时任务名", max_length=200)
    webtools_scheduled_tasks_time = models.CharField(verbose_name="定时时间", max_length=200)
    test_set_tasks_id = models.ForeignKey(
        null=True,
        verbose_name="测试集任务ID",
        to=Test_Set_Tasks,
        to_field="test_set_tasks_id",
        on_delete=models.CASCADE,
    )


class ManualTestCases(models.Model):
    """手动测试用例表"""

    manual_test_cases_id = models.AutoField(verbose_name="手动测试用例id", primary_key=True)
    creat_user = models.CharField(verbose_name="创建人", max_length=11)

    test_cases_name = models.CharField(verbose_name="手动测试用例名称", max_length=32)
    request_url = models.CharField(verbose_name="请求地址", max_length=100)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    request_parameters = models.TextField(verbose_name="请求参数", )
    response_parameters = models.TextField(verbose_name="响应参数", )
    Extract_the_response_value = models.TextField(verbose_name="提取响应值", )
    Verify_the_response_value = models.TextField(verbose_name="校验响应值", )
    test_case_create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    choice_run_the_result = (
        (0, "未执行"),
        (1, "成功"),
        (2, "失败"),
    )
    run_the_result = models.IntegerField(
        verbose_name="运行结果", choices=choice_run_the_result, default=0
    )
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )

    test_set_tasks = models.ManyToManyField(Test_Set_Tasks, related_name='test_set_tasks_many')
    interface_logs = models.CharField(verbose_name="接口日志", max_length=1000)


class Test_Reports(models.Model):
    """测试报告表"""
    test_report_id = models.AutoField(verbose_name="测试报告ID", primary_key=True)
    test_report_name = models.CharField(verbose_name="测试报告名称", max_length=100)
    test_report_cases = models.CharField(verbose_name="测试用例集", max_length=5000)


class Story_Test_Reports(models.Model):
    """故事测试报告表"""
    story_test_report_id = models.AutoField(verbose_name="故事测试报告ID", primary_key=True)
    story_test_report_name = models.CharField(verbose_name="故事测试报告名称", max_length=100)
    story_test_report_cases = models.CharField(verbose_name="故事测试用例集", max_length=5000)
    def __str__(self):
        return self.story_test_report_name
class Test_Set_Tasks_Run_Log(models.Model):
    test_set_tasks_run_id = models.AutoField(verbose_name="测试集任务执行日志id", primary_key=True)
    test_cases_name = models.CharField(verbose_name="手动测试用例名称", max_length=32)
    serial_number = models.CharField(verbose_name="序号", max_length=100)
    request_url = models.CharField(verbose_name="请求地址", max_length=100)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    request_parameters = models.TextField(verbose_name="请求参数", max_length=5000)
    response_parameters = models.TextField(verbose_name="响应参数", max_length=5000)
    Extract_the_response_value = models.TextField(verbose_name="提取响应值", )
    Verify_the_response_value = models.TextField(verbose_name="校验响应值",)
    test_case_create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    choice_run_the_result = (
        (0, "未执行"),
        (1, "成功"),
        (2, "失败"),
    )
    run_the_result = models.IntegerField(
        verbose_name="运行结果", choices=choice_run_the_result, default=0
    )
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    test_set_tasks_id = models.ForeignKey(
        null=True,
        verbose_name="测试集ID",
        to=Test_Set_Tasks,
        to_field="test_set_tasks_id",
        on_delete=models.CASCADE,
    )
    test_report_id = models.ForeignKey(
        null=True,
        verbose_name="测试报告ID",
        to=Test_Reports,
        to_field="test_report_id",
        on_delete=models.CASCADE,
    )


class Story_Test_Cases_Set(models.Model):
    """故事测试用例集"""
    story_test_set_id = models.AutoField(verbose_name="故事测试用例集ID", primary_key=True)
    story_test_set_name = models.CharField(verbose_name="故事测试集名称", max_length=100)
    create_user = models.CharField(verbose_name="创建人", max_length=100)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    run_time = models.CharField(verbose_name="运行时间", max_length=5000, blank=True)

    def __str__(self):
        return self.story_test_set_name


class Customize_scheduled_Tasks(models.Model):
    test_set_tasks_run_id = models.AutoField(verbose_name="自定义定时任务ID", primary_key=True)
    tasks_time_name = models.TextField(verbose_name="定时任务名称", max_length=5000)

    choice_tasks_method = (
        (0, "swagger定时任务类型"),
        (1, "测试集定时任务类型"),
        (2, "故事模式定时任务类型"),
    )
    tasks_method = models.IntegerField(
        verbose_name="定时任务类型", choices=choice_tasks_method
    )
    choice_weed = (
        (0, "未选择"),
        (1, "星期一"),
        (2, "星期二"),
        (3, "星期三"),
        (4, "星期四"),
        (5, "星期五"),
        (6, "星期六"),
        (7, "星期日"),
    )
    weed = models.IntegerField(
        verbose_name="执行时间", choices=choice_weed, blank=True, null=True,default=0,
    )

    hour = models.IntegerField(verbose_name="时", blank=True, null=True)
    minute = models.IntegerField(verbose_name="分", blank=True, null=True)
    second = models.IntegerField(verbose_name="秒", blank=True, null=True)
    principal = models.ForeignKey(
        null=True,
        verbose_name="负责人",
        to=UserAppInfo,
        to_field="user_id",
        on_delete=models.CASCADE,
    )
    task_test_set = models.ForeignKey(
        null=True,
        blank=True,
        verbose_name="测试集id",
        to=Test_Set_Tasks,
        to_field="test_set_tasks_id",
        on_delete=models.CASCADE,

    )
    story_test_set = models.ForeignKey(
        null=True,
        blank=True,
        verbose_name="故事测试用例集",
        to=Story_Test_Cases_Set,
        to_field="story_test_set_id",
        on_delete=models.CASCADE,

    )



class Story_Test_Cases(models.Model):
    """故事测试用例"""
    story_test_case_id = models.AutoField(verbose_name="故事测试用例ID", primary_key=True)
    story_test_case_name = models.CharField(verbose_name="故事测试用例名称", max_length=100)
    test_report_url = models.CharField(verbose_name="故事测试请求地址", max_length=200)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    test_report_request_parameters = models.TextField(verbose_name="故事测试请求参数", max_length=5000)
    extract_the_response_value = models.TextField(verbose_name="提取响应值",)
    verify_the_response_value = models.TextField(verbose_name="校验值",)
    test_report_reponse_parameters = models.TextField(verbose_name="故事测试响应参数", )
    serial_number = models.IntegerField(verbose_name="序号" )
    response_variable= models.CharField(null=True, blank=True,verbose_name="响应自定义变量", max_length=1000)
    sql_statement=models.CharField(null=True, blank=True, verbose_name="sql语句", max_length=5000)
    sql_variable=models.CharField(null=True, blank=True, verbose_name="sql变量", max_length=5000)
    custom_variable = models.CharField(null=True, blank=True, verbose_name="自定义变量", max_length=2000)
    custom_time= models.CharField(null=True, blank=True, verbose_name="自定义时间", max_length=2000)

    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    story_test_set_id = models.ForeignKey(
        null=True,
        verbose_name="故事测试用例集ID",
        to=Story_Test_Cases_Set,
        to_field="story_test_set_id",
        on_delete=models.CASCADE,
    )

    choice_execution_results = (
        (0, "成功"),
        (1, "失败"),
    )
    execution_results = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="执行结果", choices=choice_execution_results
    )



class Test_Story_Tasks_Run_Log(models.Model):
    test_set_tasks_run_id = models.AutoField(verbose_name="故事任务执行日志id", primary_key=True)
    test_cases_name = models.CharField(verbose_name="测试步骤", max_length=32)
    serial_number = models.CharField(verbose_name="序号", max_length=100)
    request_url = models.CharField(verbose_name="请求地址", max_length=100)
    choice_request_method = (
        (0, "GET"),
        (1, "POST"),
    )
    request_method = models.IntegerField(
        verbose_name="请求方法", choices=choice_request_method
    )
    request_parameters = models.TextField(verbose_name="请求参数", )
    response_parameters = models.TextField(verbose_name="响应参数", )
    Extract_the_response_value = models.TextField(verbose_name="提取响应值", )
    Verify_the_response_value = models.TextField(verbose_name="校验响应值", )
    test_case_create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    choice_run_the_result = (
        (0, "未执行"),
        (1, "成功"),
        (2, "失败"),
    )
    run_the_result = models.IntegerField(
        verbose_name="运行结果", choices=choice_run_the_result, default=0
    )
    environment_id = models.ForeignKey(
        null=True,
        verbose_name="环境id",
        to=SystemEnvironment,
        to_field="environment_id",
        on_delete=models.CASCADE,
    )
    story_test_set = models.ForeignKey(
        null=True,
        blank=True,
        verbose_name="故事测试用例集",
        to=Story_Test_Cases_Set,
        to_field="story_test_set_id",
        on_delete=models.CASCADE,

    )

    test_report_id = models.ForeignKey(
        null=True,
        verbose_name="故事测试报告ID",
        to=Story_Test_Reports,
        to_field="story_test_report_id",
        on_delete=models.CASCADE,
    )
class Web_Tootls_Disposition(models.Model):
    web_tools_disposition_id = models.AutoField(verbose_name="配置表ID", primary_key=True)
    disposition_key = models.CharField(verbose_name="配置key", max_length=1000)
    disposition_value = models.CharField(verbose_name="配置value", max_length=100)
class weapon_knife_butterfly(models.Model):
    web_tools_disposition_id = models.AutoField(verbose_name="ID", primary_key=True)
    weapon_knife_butterfly_price= models.CharField(verbose_name="价格", max_length=1000)
    weapon_knife_butterfly_time = models.CharField(verbose_name="时间", max_length=100)
    weapon_knife_butterfly_num= models.CharField(verbose_name="数量", max_length=100)

class item_comparison(models.Model):
    item_comparison_id = models.AutoField(verbose_name="物品ID", primary_key=True)
    item_comparison_old_id = models.CharField(verbose_name="原有id", max_length=1000)
    item_comparison_name = models.CharField(verbose_name="名称", max_length=100)
    en_item_comparison_name = models.CharField(verbose_name="yingwen名称", max_length=100)
    tpye_item_comparison_name = models.CharField(verbose_name="分类名称", max_length=100)


