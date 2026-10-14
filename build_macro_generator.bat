@echo off
setlocal
set "BUILD_RESULT=0"

pushd "%~dp0"
if errorlevel 1 (
    echo ERRO: nao foi possivel acessar a pasta do projeto.
    endlocal
    exit /b 1
)

set "PYTHON=%~dp0.venv\Scripts\python.exe"
if exist "%PYTHON%" (
    "%PYTHON%" -m PyInstaller --version >nul 2>&1
    if errorlevel 1 set "PYTHON="
) else (
    set "PYTHON="
)

if not defined PYTHON (
    for /f "delims=" %%P in ('where python 2^>nul') do if not defined PYTHON set "PYTHON=%%P"
)

if not defined PYTHON (
    echo ERRO: Python nao foi encontrado no ambiente do projeto nem no PATH.
    set "BUILD_RESULT=1"
    goto :finish
)

"%PYTHON%" -m PyInstaller --version >nul 2>&1
if errorlevel 1 (
    echo ERRO: PyInstaller nao foi encontrado no Python selecionado: "%PYTHON%".
    echo Instale-o com: "%PYTHON%" -m pip install pyinstaller
    set "BUILD_RESULT=1"
    goto :finish
)

rem Validate sources and Tk before starting either expensive build.
"%PYTHON%" -c "import ast, pathlib, tkinter; files = ['Macro Generator.py', 'macro_core.py', 'auto_update.py', 'ui_theme.py', 'preview.py', 'constants.py', 'libraries.py', 'updater.py']; [ast.parse(pathlib.Path(p).read_text(encoding='utf-8'), filename=p) for p in files]"
if errorlevel 1 goto :error

echo [1/3] Compilando updater...
"%PYTHON%" -m PyInstaller --onefile --noconsole --clean --name updater updater.py
if errorlevel 1 goto :error

echo [2/3] Compilando Macro Generator...
"%PYTHON%" -m PyInstaller --onefile --noconsole --clean --name "MacroGenerator" --paths "%CD%" --add-binary "dist\updater.exe;." "Macro Generator.py"

if errorlevel 1 goto :error

echo.
echo [3/3] Concluido.
echo.
echo O executavel para distribuir esta em:
echo dist\MacroGenerator.exe
echo.
goto :finish

:error
echo.
echo ERRO durante a compilacao.
set "BUILD_RESULT=1"

:finish
popd
endlocal & exit /b %BUILD_RESULT%
