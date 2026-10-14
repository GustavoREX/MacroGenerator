@echo off
setlocal
set "BUILD_RESULT=0"
pushd "%~dp0" || exit /b 1
set "APP_PYTHON=python"
set "PYINSTALLER_CONFIG_DIR=%~dp0build\pyinstaller-cache"
if exist ".venv\Scripts\python.exe" set "APP_PYTHON=.venv\Scripts\python.exe"
set "BUILD_CLEAN="
if /I "%~1"=="clean" set "BUILD_CLEAN=--clean"

"%APP_PYTHON%" -c "import ast,pathlib,PIL,numpy,ttkbootstrap,tkinterdnd2,onnxruntime,PyInstaller,importlib.util; assert importlib.util.find_spec('rembg'); [ast.parse(p.read_text(encoding='utf-8'),filename=str(p)) for folder in ['.','core','modes'] for p in pathlib.Path(folder).glob('*.py')]"
if errorlevel 1 (
    echo ERRO: dependencias ausentes ou fonte invalido. Execute setup.bat.
    goto :error
)

echo [1/3] Compilando atualizador...
"%APP_PYTHON%" -m PyInstaller --noconfirm %BUILD_CLEAN% --onefile --noconsole --name updater updater.py
if errorlevel 1 goto :error

echo [2/3] Compilando Macro x Token...
"%APP_PYTHON%" -m PyInstaller --noconfirm %BUILD_CLEAN% --onefile --noconsole --name "Macro x Token" --icon Token.ico --paths "%CD%" --add-binary "dist\updater.exe;." --add-data "Token.ico;." --add-data "borders;borders" --collect-all tkinterdnd2 --collect-data ttkbootstrap --collect-data rembg --collect-binaries onnxruntime --copy-metadata rembg --copy-metadata onnxruntime --copy-metadata pymatting launcher.py
if errorlevel 1 goto :error

echo [3/3] Preparando arquivo para a release...
"%APP_PYTHON%" -c "from pathlib import Path; import shutil; from constants import VERSAO; out=Path('release'); out.mkdir(exist_ok=True); target=out / ('MacroXToken.V'+VERSAO+'.exe'); shutil.copy2('dist/Macro x Token.exe',target); print(target)"
if errorlevel 1 goto :error
echo Concluido. Aplicativo: dist\Macro x Token.exe
goto :finish
:error
echo ERRO durante a compilacao.
set "BUILD_RESULT=1"
:finish
popd
endlocal & exit /b %BUILD_RESULT%
