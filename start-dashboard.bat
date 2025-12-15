@echo off
REM Stack Overflow Dashboard - Startup Script (Windows)
REM This script starts both the Flask backend and React frontend

setlocal enabledelayedexpansion

cls
echo.
echo ========================================================
echo    Stack Overflow Data Analysis Dashboard
echo    Starting Backend and Frontend...
echo ========================================================
echo.

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Check if app.py exists
if not exist "app.py" (
    echo Error: app.py not found in %SCRIPT_DIR%
    echo Please run this script from the Projekti_BigData directory
    pause
    exit /b 1
)

REM Check if frontend folder exists
if not exist "frontend" (
    echo Error: frontend folder not found
    pause
    exit /b 1
)

REM Check Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check Node is available
node --version >nul 2>&1
if errorlevel 1 (
    echo Error: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo Checking requirements...
echo.
for /f "tokens=*" %%i in ('python --version') do set PYTHON_VER=%%i
for /f "tokens=*" %%i in ('node --version') do set NODE_VER=%%i
for /f "tokens=*" %%i in ('npm --version') do set NPM_VER=%%i

echo Python found: %PYTHON_VER%
echo Node.js found: %NODE_VER%
echo npm found: %NPM_VER%
echo.

REM Start Flask backend in new window
echo Starting Flask backend on http://localhost:5000...
start "Flask Backend" python app.py
echo Flask started
timeout /t 3 /nobreak

REM Start React frontend in new window
echo Starting React frontend on http://localhost:3000...
cd /d "%SCRIPT_DIR%frontend"
start "React Frontend" cmd /k npm start
cd /d "%SCRIPT_DIR%"

echo.
echo ========================================================
echo               DASHBOARD STARTED!
echo ========================================================
echo.
echo Dashboard URL: http://localhost:3000
echo API Server: http://localhost:5000
echo.
echo The dashboard will open automatically in your browser.
echo If not, manually visit: http://localhost:3000
echo.
echo To stop the servers:
echo  1. Close the Flask Backend window
echo  2. Close the React Frontend window
echo  3. Or press Ctrl+C in each window
echo.
echo ========================================================
echo.

REM Try to open browser
start http://localhost:3000

REM Keep window open
pause
```

Now let me also make the bash script executable and create a simple instruction file:
