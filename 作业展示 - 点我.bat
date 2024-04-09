@echo off  
REM 检查 Jupyter Notebook 是否已安装  
where jupyter >nul 2>&1  
if %errorlevel% neq 0 (  
    echo Jupyter Notebook 未找到，请确保已安装。  
    exit /b 1  
)  
  
REM 打开 The3rdHomework.ipynb 文件  
jupyter notebook demo\The3rdHomework.ipynb