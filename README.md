# repo
仓库管理及台账管理

打包后的文件在dist/目录下

项目名为repo

应用为 repo_app（仓库管理）、assert（资产\台账管理）

太乱了，不整了





# 备品备件进出口管理系统

## 创建项目

```powershell
django-admin startproject apps
cd .\apps\
python manage.py startapp repo
python manage.py startapp asset
```

```python
SECRET_KEY = 'your_secret_key'  # 请替换成更安全的密钥
DEBUG = True  # 正式环境改成 False
ALLOWED_HOSTS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sparepartsapp',  # 你的应用
]
# 设置Django的时区为上海时间
TIME_ZONE = 'Asia/Shanghai'

# 关闭Django的时区支持
USE_TZ = False
```

启动

```powershell
python manage.py startapp warehouse
python manage.py runserver  0.0.0.0:8000
```

```shell
python manage.py makemigrations
python manage.py migrate
```

重新清理数据库

```shell
# 首先，您需要进入数据库管理工具（如MySQL Workbench、phpMyAdmin等），找到django_migrations表，并删除与您删除的应用相关的记录。这些记录通常包含迁移文件的名称和状态。

# DELETE FROM django_migrations WHERE app = 'your_app_name';

# 在您的Django应用目录中，手动创建一个名为migrations的文件夹，并在其中创建一个空的__init__.py文件。这是为了确保Django能够识别该文件夹为一个Python包。
python manage.py makemigrations
python manage.py migrate
```

```bash
# websocket相关的启动
uvicorn repo.asgi:application  --host 0.0.0.0 --port 8000 --reload
```

## 打包exe文件

### 生成spec文件

```powershell
pyi-makespec -D manage.py
```

### 编辑spec文件

```
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['manage.py'],
    pathex=[],
    binaries=[],
    datas=[
    ('D:/develop/Python38/Lib/site-packages/django/contrib/admin/templates/', 'django/contrib/admin/templates'),
    ('D:/develop/Python38/Lib/site-packages/import_export/templates/', 'import_export/templates'),
],
    hiddenimports=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'repo_app',
        'repo_app.admin',
        'repo_app.models',
        'repo_app.apps',
        'repo_app.resources',
        'import_export',
        'import_export.admin',
        'import_export.resources',
		'django.template.context_processors',
		'asset',
        'asset.admin',
        'asset.models',
        'asset.apps',
        'asset.resources',
],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='manage',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='manage',
)
```

```powershell
pyinstaller manage.spec
```

### 一键启动脚本

```powershell
@echo off
chcp 65001 
set PYTHONIOENCODING=utf-8
color 0A

:: 设置要启动的exe路径（请替换为你的程序路径）
set "exePath=.\manage.exe"
set "exeName=manage.exe"  
:: 设置启动参数（如果没有参数，可以留空或删除）
set "params=runserver 127.0.0.1:8000 --noreload"  

:: 检查程序是否正在运行，如果是则关闭
tasklist /FI "IMAGENAME eq %exeName%" 2>NUL | find /I "%exeName%" >NUL
if %ERRORLEVEL% == 0 (
    echo 检测到 %exeName% 正在运行，正在关闭...
    taskkill /F /IM "%exeName%" >NUL
    timeout /t 2 /nobreak >NUL  
    echo 已关闭 %exeName%
)

:: 检查程序是否存在
if not exist "%exePath%" (
    echo 错误：找不到程序文件！
    echo 路径: %exePath%
    pause
    exit /b
)
if exist "debug.log" (
    del "debug.log"
    if errorlevel 1 (
        echo 删除失败！
        exit /b 1
    )
    echo 成功删除 debug.log 文件
) else (
    echo debug.log 文件不存在
)
:: 启动程序
echo 正在启动 %exeName%...
start "" "%exePath%" %params%

echo 程序已启动！
timeout /t 3 /nobreak >NUL  :: 等待3秒后自动关闭窗口（可选）
exit
```

