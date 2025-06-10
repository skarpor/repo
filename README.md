# 仓库管理及台账管理项目文档
## 项目概述
  * **项目名称** ：repo
  * **应用组成** ：包含 repo_app（仓库管理）、assert（资产 / 台账管理）
  * **打包文件位置** ：dist/ 目录下
## 环境搭建
  * **安装主依赖**
在命令行工具中运行以下命令：
```powershell
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install django-import-export -i https://pypi.tuna.tsinghua.edu.cn/simple
```
  * **安装后台模板依赖**
```powershell
pip install django-jazzmin -i https://pypi.tuna.tsinghua.edu.cn/simple
```
## 项目操作指南
  * **查看帮助信息**
```powershell
python manage.py help
```
  * **管理员用户管理**
    * 创建或修改管理员用户：
```powershell
python manage.py  changepassword
python manage.py  createsuperuser
```
  * **启动项目**
```powershell
python manage.py runserver  0.0.0.0:8000
```
  * **数据库迁移**
    * 生成迁移文件：
```shell
python manage.py makemigrations
```
    * 执行迁移：
```shell
python manage.py migrate
```
  * **清理并重建数据库**
    * 手动清理相关记录：先进入数据库管理工具（如 MySQL Workbench、phpMyAdmin 等），找到 django_migrations 表，执行 SQL 语句 `DELETE FROM django_migrations WHERE app = 'your_app_name';`，将与您删除的应用相关的记录删除。
    * 创建 migrations 文件夹及空的 `__init__.py` 文件：在您的 Django 应用目录下手动创建一个名为 migrations 的文件夹，并在其中新建一个空的 `__init__.py` 文件，以确保 Django 能识别该文件夹为 Python 包。
    * 重新生成并执行迁移：
```shell
python manage.py makemigrations
python manage.py migrate
```
