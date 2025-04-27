@echo off
echo Starting Artemaya...
echo.

python run.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error occurred while starting the application.
    echo Please make sure Python is installed and available in your PATH.
    echo.
    pause
    exit /b 1
)

exit /b 0 