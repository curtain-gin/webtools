## 安装步骤/Initiation steps



安装依赖/Install dependencies

```sh
pip install -r requirements.txt
```

创建mysql数据库

```sh
CREATE DATABASE webtoolsdb;
```

生成数据库迁移文件

```sh
python manage.py makemigrations
```

数据迁移

```sh
python manage.py migrate
```

插入数据

`permissionpath`

```sql
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (1, '功能列表', '/permission/path/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (2, '功能添加', '/permission/path/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (3, '功能编辑', '/permission/path/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (4, '功能删除', '/permission/path/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (5, '用户列表', '/user/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (6, '用户增加', '/user/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (7, '用户编辑', '/user/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (8, '用户删除', '/user/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (10, '权限添加', '/permission/role/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (11, '会员删除列表', '/other/user/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (12, '会员删除', '/other/user/members/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (13, '游客删除', '/other/user/nom/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (14, '保单数据生成', '/data/generation/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (15, '超时日志', '/log/out/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (16, '正常日志', '/log/normal/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (17, '角色编辑', '/permission/role/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (18, '角色删除', '/permission/role/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (19, '角色添加', '/permission/role/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (21, '用户注销', '/user/logout/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (22, '角色列表', '/permission/role/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (23, 'xmind转换页面', '/xmind/exl/data/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (24, '转换下载', '/xmind/exl/data/download/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (25, '个人修改密码', '/user/revise/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (26, '角色列表', '/permission/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (27, '游客删除列表', '/other/user/visitor/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (28, '主页', '/index/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (29, '用户登陆', '/user/login/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (30, '投保次数重置', '/insure/num/reset/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (31, '需求列表', '/demand/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (32, '需求增加', '/demand/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (33, '需求编辑', '/demand/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (34, '需求删除', '/demand/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (35, '问题列表', '/defect/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (36, '问题增加', '/defect/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (37, '问题编辑', '/defect/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (38, '问题删除', '/defect/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (39, '建议列表', '/suggestion/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (40, '新增建议', '/suggestion/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (41, '编辑建议', '/suggestion/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (42, '建议删除', '/suggestion/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (43, '产品库查询数据', '/product/library/select/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (45, '赠险单列表', '/premium/insurance/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (46, '赠险单删除', '/premium/insurance/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (47, '非赠险单列表', '/insurance/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (48, '非赠险单删除', '/insurance/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (53, '脚本提交记录列表', '/case/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (54, '添加脚本提交', '/case/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (55, '编辑脚本提交记录', '/case/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (56, '删除脚本提交记录', '/case/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (57, 'TS下载', '/swagger/ts/down/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (58, 'swagger接口列表', '/swagger/InterfaceInfo/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (59, '手动测试用例', '/list/of/manual/test/cases/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (60, '定时任务列表', '/swagger/timed/tasks/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (61, 'MOCK列表', '/mockserice/interfaces/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (62, 'MCOK查看', '/mockserice/interfaces/info/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (63, 'MOCK添加', '/mockserice/interfaces/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (64, 'swagger接口添加', '/swagger/management/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (65, '环境管理', '/request/environment/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (66, '环境编辑', '/request/environment/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (67, 'swagger接口添加', '/swagger/management/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (68, 'swagger接口添加', '/swagger/management/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (69, 'swagger接口添加', '/list/of/interfaces/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (70, 'swagger接口查看', '/swagger/interfaceInfo/info/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (71, '版本列表', '/version/management/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (72, '同步', '/swagger/management/auto/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (73, '测试集任务列表', '/test/set/tasks/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (74, '测试集任务添加', '/test/set/tasks/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (75, '测试集任务编辑', '/test/set/tasks/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (76, '接口测试用例添加', '/list/of/manual/test/cases/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (77, '权限不足', '/permission/info/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (78, 'swagger接口导入模版下载', '/swagger/template/down/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (79, '测试集任务执行', '/test/set/tasks/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (80, 'swagger手动执行同步', '/swagger/management/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (81, 'mock服务编辑', '/mockserice/interfaces/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (82, '需求下载', '/demand/download/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (83, '问题反馈下载', '/defect/download/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (84, '建议优化下载', '/suggestion/download/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (85, '测试集报告列表', '/test/report/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (86, '测试集任务测试报告', '/test/report/view/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (87, '测试集测试是用例日志', '/test/report/case/log/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (88, 'swagger定时任务天假', '/swagger/timed/tasks/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (89, '新定时任务列表', '/new/timed/tasks/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (90, '新定时任务添加', '/new/timed/tasks/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (91, '手动测试用例执行', '/list/of/manual/test/cases/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (92, '定时任务执行列表', '/scheduler/job/execution/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (93, '测试页面', '/test/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (94, '故事模式测试用例', '/story/test/cases/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (95, '故事添加', '/story/test/cases/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (96, '故事模式测试用例单', '/story/test/cases/data/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (98, '故事测试步骤列表', '/story/test/cases/data/list/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (99, '故事测试用例步骤信息', '/story/test/cases/data/information/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (100, '步骤编辑', '/story/test/cases/data/information/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (102, '故事测试用例执行', '/story/test/cases/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (104, '环境新建', '/request/environment/add/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (105, 'ts下载', '/version/ts/down/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (106, '定时任务删除', '/scheduler/job/delet/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (107, '定时任务编辑', '/scheduler/job/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (108, 'JSON解析', '/json/parse/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (109, 'SQL查询', '/sql/inquire/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (110, '版本编辑', '/version/management/edit/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (111, '数据配置', '/data/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (112, 'quanbu', '/all/data/run/');
INSERT INTO `webTools_permissionpath` (`permission_path_id`, `permission_path_name`, `permission_path`) VALUES (113, 'quanbu', '/all/data/run/');
```

`permissionpath_role`

```sql
NSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (1, 1, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (2, 2, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (3, 3, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (4, 4, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (5, 5, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (6, 6, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (7, 7, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (8, 8, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (10, 10, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (11, 11, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (29, 11, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (12, 12, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (34, 12, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (13, 13, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (35, 13, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (14, 14, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (28, 14, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (15, 15, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (16, 16, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (17, 17, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (18, 18, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (19, 19, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (21, 21, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (43, 21, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (22, 22, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (23, 23, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (32, 23, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (24, 24, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (33, 24, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (25, 25, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (42, 25, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (26, 26, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (30, 27, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (31, 27, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (36, 28, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (37, 28, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (38, 29, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (39, 29, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (40, 30, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (41, 30, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (44, 31, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (45, 31, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (46, 32, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (47, 32, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (48, 33, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (49, 33, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (50, 34, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (51, 34, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (52, 35, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (53, 35, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (54, 36, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (55, 36, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (56, 37, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (57, 37, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (58, 38, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (59, 38, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (60, 39, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (61, 39, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (62, 40, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (63, 40, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (64, 41, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (65, 41, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (66, 42, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (67, 42, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (68, 43, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (69, 43, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (72, 45, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (73, 45, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (74, 46, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (75, 46, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (76, 47, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (77, 47, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (78, 48, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (79, 48, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (88, 53, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (89, 53, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (90, 54, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (91, 54, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (92, 55, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (93, 55, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (94, 56, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (95, 56, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (96, 57, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (97, 57, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (98, 58, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (99, 58, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (100, 59, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (101, 59, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (102, 60, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (103, 60, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (104, 61, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (105, 61, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (106, 62, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (107, 62, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (108, 63, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (109, 63, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (110, 64, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (111, 64, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (112, 65, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (113, 65, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (114, 66, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (199, 66, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (115, 67, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (116, 67, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (117, 68, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (118, 68, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (119, 69, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (120, 69, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (121, 70, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (122, 70, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (123, 71, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (124, 71, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (125, 72, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (126, 73, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (127, 73, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (128, 74, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (129, 74, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (130, 75, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (131, 75, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (132, 76, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (133, 76, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (134, 77, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (135, 77, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (136, 78, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (137, 78, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (138, 79, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (139, 79, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (140, 80, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (141, 80, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (142, 81, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (143, 81, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (144, 82, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (145, 82, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (146, 83, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (147, 83, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (148, 84, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (149, 84, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (150, 85, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (151, 85, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (152, 86, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (153, 86, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (154, 87, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (155, 87, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (156, 88, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (157, 88, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (158, 89, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (159, 89, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (160, 90, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (161, 90, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (162, 91, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (163, 91, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (164, 92, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (165, 92, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (166, 93, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (167, 94, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (168, 94, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (169, 95, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (170, 95, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (171, 96, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (172, 96, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (175, 98, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (176, 98, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (177, 99, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (178, 99, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (179, 100, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (180, 100, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (183, 102, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (184, 102, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (187, 104, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (188, 104, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (189, 105, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (190, 105, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (191, 106, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (192, 106, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (193, 107, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (194, 107, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (195, 108, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (196, 108, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (197, 109, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (198, 109, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (200, 110, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (201, 110, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (202, 111, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (203, 111, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (204, 112, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (205, 112, 2);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (206, 113, 1);
INSERT INTO `webTools_permissionpath_role` (`id`, `permissionpath_id`, `role_id`) VALUES (207, 113, 2);
```

 `webTools_role`

```sql
INSERT INTO `webTools_role` (`role_id`, `role_name`) VALUES (1, '管理员');
INSERT INTO `webTools_role` (`role_id`, `role_name`) VALUES (2, '用户');
INSERT INTO `webTools_role` (`role_id`, `role_name`) VALUES (3, '敏感数据权限');
```

`webTools_userappinfo`

```sql
INSERT INTO `webTools_userappinfo` (`user_id`, `username`, `email`, `mobile_phone`, `password`) VALUES (1, 'admin', 'your_email@qq.com', '15611111111', '0dd1df5a9cf95a4f6385bb94c26ec502');
COMMIT;
```

`userappinfo_role`

```sql
INSERT INTO `webTools_userappinfo_role` (`id`, `userappinfo_id`, `role_id`) VALUES (1, 1, 1);
COMMIT;
```

启动django

```
python manage.py runserver 0.0.0.0:8000
```

![image-20240110183839542](/home/f1v3/.config/Typora/typora-user-images/image-20240110183839542.png)

使用手机号登陆/默认密码123456

![image-20240110183940566](/home/f1v3/.config/Typora/typora-user-images/image-20240110183940566.png)

成功登陆
