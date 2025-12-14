@echo off
SETLOCAL

echo === Configurando entorno virtual ===
powershell -ExecutionPolicy Bypass -File .\tools\setup_venv.ps1

echo.
echo === Inicializando base de datos ===
REM Activar el entorno virtual de Windows
call .\venv\Scripts\activate.bat
python -m configuracion.init_db
call deactivate

echo.

ENDLOCAL
