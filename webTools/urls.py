from django.urls import path, include, re_path
from webTools.views import (
    index,
    permission,
    permission_path,
    other_user,
    order_data_generation,
    user_log,
    xmin_exl_data,
    error_page,
    tools_role,
    manual_test_cases,
    request_environment,
    interfaces_test,
    swagger_management,
    mock_management,
    swagger_timed_tasks,
    test_set_tasks,
    test_report,
    story_test, story_report,
    version_management,
    test_jiji,
    user,
    insure_num_reset,
    demand,
    defect,
    suggestion,
    delete_premium_insurance,
    delete_insurance,
    auto_framework_commit,
    data_b

)

urlpatterns = [

    # 验证码url
    path('image/code/', user.image_code),

    # 用户
    path('user/login/', user.user_login),
    path('user/list/', user.user_list),
    path('user/add/', user.user_add),
    # path('user/info/',user.user_info),
    path('user/logout/', user.user_logout),
    path('user/edit/<int:nid>/', user.user_edit),
    path('user/delet/<int:nid>/', user.user_delet),
    path('user/revise/<int:nid>/', user.user_revise),

    # 主页url
    path('index/', index.index),

    # 权限角色
    path('permission/list/', permission.user_permission_role_list),
    path('permission/role/add/', permission.user_permission_role_add),
    path('permission/role/edit/<int:nid>/', permission.user_permission_role_edit),
    path('permission/role/delet/<int:nid>/', permission.user_permission_role_delet),

    # 权限路径
    path('permission/path/list/', permission_path.permission_path_list),
    path('permission/path/add/', permission_path.permission_path_add),
    path('permission/path/edit/<int:nid>/', permission_path.permission_path_edit),
    path('permission/path/delet/<int:nid>/', permission_path.user_permission_path_delet),
    path('permission/info/', permission_path.user_permission_path_info),

    # 日志
    path('log/out/', user_log.log_out),
    path('log/normal/', user_log.log_normal),
    # 小工具
    ##会员非会员删除
    path('other/user/list/', other_user.other_list),
    path('other/user/visitor/list/', other_user.other_visitor_user_list),
    path('other/user/members/delet/<str:nid>/<str:env>/', other_user.other_membersuser_delet),
    path('other/user/nom/delet/<str:nid>/<str:env>/', other_user.other_nom_user_delet),
    ##订单基础数据生成
    path('data/generation/', order_data_generation.order_data_generation),
    # xmind 转换
    path('xmind/exl/data/', xmin_exl_data.xmind_conversion),
    path('xmind/exl/data/download/xmind/', xmin_exl_data.xmind_to_exl_down),
    # 赠险单删除
    path('premium/insurance/list/', delete_premium_insurance.premium_insurance_list),
    path('premium/insurance/delet/<str:nid1>/<str:nid2>/<str:env>/', delete_premium_insurance.premium_insurance_delet),
    path('premium/insurance/delet/<str:nid1>/<str:env>/', delete_premium_insurance.premium_insurance_delet),
    # 非赠险单删除
    path('insurance/list/', delete_insurance.insurance_list),
    path('insurance/delet/<str:nid1>/<str:env>/', delete_insurance.insurance_delet),
    # 投保次数重置
    path('insure/num/reset/', insure_num_reset.insure_num_reset),
    # json解析
    path('json/parse/', order_data_generation.json_parse),
    # SQL查询
    path('sql/inquire/', order_data_generation.sql_inquire),

    # 脚本提交记录
    path('case/list/', auto_framework_commit.case_list),
    path('case/add/', auto_framework_commit.case_add),
    path('case/edit/<int:nid>/', auto_framework_commit.case_edit),
    path('case/delet/<int:nid>/', auto_framework_commit.case_delet),
    # 需求汇总
    path('demand/list/', demand.demand_list),
    path('demand/add/', demand.demand_add),
    path('demand/edit/<int:nid>/', demand.demand_edit),
    path('demand/delet/<int:nid>/', demand.demand_delet),
    path('demand/download/', demand.demand_download),
    # 问题反馈
    path('defect/list/', defect.defect_list),
    path('defect/add/', defect.defect_add),
    path('defect/edit/<int:nid>/', defect.defect_edit),
    path('defect/delet/<int:nid>/', defect.defect_delet),
    path('defect/download/', defect.defect_download),
    # 建议优化
    path('suggestion/list/', suggestion.suggestion_list),
    path('suggestion/add/', suggestion.suggestion_add),
    path('suggestion/edit/<int:nid>/', suggestion.suggestion_edit),
    path('suggestion/delet/<int:nid>/', suggestion.suggestion_delet),
    path('suggestion/download/', suggestion.suggestion_download),
    # 日志
    path('log/out/', user_log.log_out),
    path('log/normal/', user_log.log_normal),
    # 产品库查询数据
    path('product/library/select/', tools_role.prduct_library_select),
    # 手动测试用例管理
    path('list/of/manual/test/cases/', manual_test_cases.list_of_manual_test_cases),
    path('list/of/manual/test/cases/', manual_test_cases.list_of_manual_test_cases),
    path('list/of/manual/test/cases/add/', manual_test_cases.list_of_manual_test_cases_add),
    path('list/of/manual/test/cases/edit/<int:nid>/', manual_test_cases.list_of_manual_test_cases_edit),
    path('list/of/manual/test/cases/delet/<int:nid>/', manual_test_cases.list_of_manual_test_cases_delet),
    path('list/of/manual/test/cases/run/<int:nid>/', manual_test_cases.list_of_manual_test_cases_run),
    path('list/of/manual/test/cases/log/<int:nid>/', manual_test_cases.list_of_manual_test_cases_log),
    # 环境管理
    path('request/environment/list/', request_environment.request_environmentl_list),
    path('request/environment/add/', request_environment.request_environmentl_add),
    path('request/environment/edit/<int:nid>/', request_environment.request_environmentl_edit),
    path('request/environment/delet/<int:nid>/', request_environment.request_environmentl_delet),
    # 测试接口
    path('testrestsrt/', test_jiji.test_jijiji_jjj),
    # 接口列表
    path('list/of/interfaces/', interfaces_test.interfaces_test_list),
    path('list/of/interfaces/add/', interfaces_test.interfaces_test_add),
    path('list/of/interfaces/info/<int:nid>/', interfaces_test.interfaces_test_info),
    path('list/of/interfaces/edit/<int:nid>/', interfaces_test.interfaces_test_edit),
    # 版本管理
    path('version/management/list/', version_management.version_management_list),
    path('version/management/add/', version_management.version_management_add),
    path('version/management/edit/<int:nid>/', version_management.version_management_edit),
    path('version/ts/down/<int:nid>/', version_management.version_ts_dow),
    # swagger管理
    path('swagger/management/list/', swagger_management.swagger_management_list),
    path('swagger/management/add/', swagger_management.swagger_management_add),
    path('swagger/management/run/<int:nid>/', swagger_management.swagger_management_run),
    path('swagger/management/auto/', swagger_management.swagger_management_auto_run),
    path('swagger/InterfaceInfo/list/', swagger_management.swagger_interfaceInfo_list),
    path('swagger/InterfaceInfo/add/', swagger_management.swagger_interfaceInfo_add),
    path('swagger/authentication/', swagger_management.swagger_authentication),
    path('swagger/interfaceInfo/info/<int:nid>/', swagger_management.swagger_info),
    path('swagger/ts/down/<int:nid>/', swagger_management.swagger_ts_down),
    path('swagger/template/down/', swagger_management.swagger_template_down),
    path('swagger/swagger/upload/', swagger_management.swagger_upload),

    # mock服务
    path('mockserice/interfaces/list/', mock_management.mock_serice_interfaces_list),
    path('mockserice/interfaces/add/', mock_management.mock_serice_interfaces_add),
    path('mockserice/interfaces/edit/<int:nid>/', mock_management.mock_serice_interfaces_edit),
    path('mockserice/interfaces/info/<int:nid>/', mock_management.mock_serice_interfaces_info),
    re_path('^mock/[a-zA-Z0-9]*', mock_management.mock_server),
    # 定时任务
    path('new/timed/tasks/list/', swagger_timed_tasks.new_timed_task_list),
    path('new/timed/tasks/add/', swagger_timed_tasks.new_timed_task_add),
    path('scheduler/job/execution/list/', swagger_timed_tasks.scheduler_job_execution_list),
    path('scheduler/job/delet/<int:nid>/', swagger_timed_tasks.scheduler_job_delet),
    path('scheduler/job/edit/<int:nid>/', swagger_timed_tasks.scheduler_job_edit),
    # 测试集任务
    path('test/set/tasks/list/', test_set_tasks.test_set_tasks_list),
    path('test/set/tasks/add/', test_set_tasks.test_set_tasks_add),
    path('test/set/tasks/edit/<int:nid>/', test_set_tasks.test_set_tasks_edit),
    path('test/set/tasks/run/<int:nid>/', test_set_tasks.test_set_tasks_run),
    path('test/set/tasks/view/<int:nid>/', test_set_tasks.test_set_tasks_view),
    path('test/set/tasks/delet/<int:nid>/<int:niid>/', test_set_tasks.test_set_tasks_case_delet),
    path('test/set/tasks/delet/<int:nid>/', test_set_tasks.test_set_tasks_delet),
    path('test/set/tasks/disassociate/<int:nid>/<int:setnid>/', test_set_tasks.test_set_tasks_disassociate),
    path('test/set/tasks/disassociaten/<int:nid>/', test_set_tasks.test_set_tasks_disassociaten),

    # 测试报告地址
    path('test/report/list/', test_report.test_report_list),
    path('test/report/view/<int:nid>/', test_report.test_report_view_),
    path('test/report/case/log/<int:nid>/', test_report.test_report_case_log),

    # 故事模式
    path('story/test/cases/list/', story_test.story_test_cases_list),
    path('story/test/cases/data/copy/<int:nid>/', story_test.story_test_cases_copy),
    path('story/test/cases/add/', story_test.story_test_cases_add),
    path('story/test/cases/edit/<int:nid>/', story_test.story_test_set_edit),
    path('story/test/cases/delet/<int:nid>/', story_test.story_test_set_delet),
    path('story/test/cases/data/list/<int:nid>/', story_test.story_test_cases_data_list),
    path('story/test/cases/data/web/diagraml/<int:nid>/', story_test.data_tu),
    path('story/test/cases/data/web/tree/<int:nid>/', story_test.data_tree),

    path('story/test/cases/data/add/', story_test.story_test_cases_data_add),
    path('story/test/cases/data/information/<int:nid>/', story_test.story_test_cases_data_information),
    path('story/test/cases/data/information/edit/<int:nid>/', story_test.story_test_cases_data_edit),
    path('story/test/cases/data/information/delet/<int:nid>/', story_test.story_test_cases_data_delet),
    path('story/test/cases/run/<int:nid>/', story_test.story_test_cases_run),
    path('story/test/cases/data/information/up/<int:nid>/', story_test.story_test_cases_data_up),
    path('story/test/cases/data/information/down/<int:nid>/', story_test.story_test_cases_data_down),
    # 故事测试报告地址
    path('story/test/report/list/', story_report.story_test_report_list),
    path('story/test/report/view/<int:nid>/', story_report.story_test_report_view),
    path('story/test/report/case/log/<int:nid>/', story_report.story_test_report_case_log),
    #buf
    path('data/list/', data_b.data_list),
    path('all/data/run/', data_b.all_data_run),
]
hander400 = error_page.bad_request
hander403 = error_page.permission_denied
hander404 = error_page.page_not_found
hander500 = error_page.error
