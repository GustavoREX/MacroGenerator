@echo off
setlocal
pushd "%~dp0" || exit /b 1
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
    if errorlevel 1 goto :error
)
".venv\Scripts\python.exe" -m pip install -r requirements-build.txt
if errorlevel 1 goto :error
popd
endlocal & exit /b 0
:error
echo ERRO: nao foi possivel preparar o ambiente. Confira o Python e a conexao.
popd
endlocal & exit /b 1
