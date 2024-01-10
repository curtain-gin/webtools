## 安装步骤/Initiation steps



安装依赖/Install dependencies

```
pip install -r requirements.txt
```

创建mysql数据库

```
CREATE DATABASE webtoolsdb;
```

生成数据库迁移文件

```
python manage.py makemigrations
```

数据迁移

```
python manage.py migrate
```

