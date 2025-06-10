@echo off
chcp 65001 
set PYTHONIOENCODING=utf-8
color 0A

:: 设置要启动的exe路径（请替换为你的程序路径）
set "exePath=.\dist\manage\manage.exe"
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