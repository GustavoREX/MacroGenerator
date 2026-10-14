@echo off
setlocal
pushd "%~dp0" || exit /b 1
set "APP_PYTHON=python"
if exist ".venv\Scripts\python.exe" set "APP_PYTHON=.venv\Scripts\python.exe"
"%APP_PYTHON%" launcher.py
set "RESULT=%ERRORLEVEL%"
if not "%RESULT%"=="0" echo Confira as dependencias com setup.bat.
popd
endlocal & exit /b %RESULT%
