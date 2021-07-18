@echo off 

:: ------- 配置项 ------- 

:: 要执行的文件名 
set FILE=backup.bat
:: 计划频率类型 
set FREQUENCY=DAILY 

:: 频率，与上面的计划频率类型对应 
set MODIFIER=1 

:: 该计划执行的时间（24 小时制） 
set DATETIME=15:00 

:: 计划的名字 
set NAME="Backup Mysql Job" 

:: 计划执行用户，不建议修改 
set USER="System" 

:: ------- 以下请勿修改 ------- 
schtasks /Create /SC %FREQUENCY% /MO %MODIFIER% /ST %DATETIME% /TN %NAME% /TR D:\mysql_dump_db\backup.bat 
::Start cmd.exe
::SchTasks /Delete /TN %NAME%
pause