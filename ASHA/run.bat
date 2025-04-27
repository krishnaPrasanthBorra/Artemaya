@echo off
echo Starting ASHA - AI Career Companion...
echo.

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Error: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

REM Run the launcher script
python run.py

REM If we get here, the application has ended
echo.
echo ASHA has been closed.
pause 