#!/bin/bash

# Stack Overflow Dashboard - Startup Script
# This script starts both the Flask backend and React frontend

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print banner
clear
echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║   Stack Overflow Data Analysis Dashboard                   ║"
echo "║   Starting Backend and Frontend...                         ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if we're in the right directory
if [ ! -f "$SCRIPT_DIR/app.py" ]; then
    echo -e "${RED}Error: app.py not found in $SCRIPT_DIR${NC}"
    echo "Please run this script from the Projekti_BigData directory"
    exit 1
fi

# Check if frontend folder exists
if [ ! -d "$SCRIPT_DIR/frontend" ]; then
    echo -e "${RED}Error: frontend folder not found${NC}"
    exit 1
fi

# Check Python is available
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo -e "${RED}Error: Python is not installed or not in PATH${NC}"
    exit 1
fi

# Check Node is available
if ! command -v node &> /dev/null; then
    echo -e "${RED}Error: Node.js is not installed or not in PATH${NC}"
    exit 1
fi

echo -e "${YELLOW}Checking requirements...${NC}"
sleep 1

# Try to use python3, fallback to python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo -e "${GREEN}✓ Python found: $PYTHON_CMD${NC}"
echo -e "${GREEN}✓ Node.js found: $(node --version)${NC}"
echo -e "${GREEN}✓ npm found: $(npm --version)${NC}"
echo ""

# Start Flask backend in background
echo -e "${YELLOW}Starting Flask backend on http://localhost:5000...${NC}"
cd "$SCRIPT_DIR"
$PYTHON_CMD app.py > /tmp/flask_dashboard.log 2>&1 &
FLASK_PID=$!
echo -e "${GREEN}Flask PID: $FLASK_PID${NC}"

# Wait for Flask to start
echo -e "${YELLOW}Waiting for Flask to start...${NC}"
sleep 3

# Check if Flask is running
if ! ps -p $FLASK_PID > /dev/null; then
    echo -e "${RED}Flask failed to start!${NC}"
    echo -e "${RED}Check /tmp/flask_dashboard.log for errors${NC}"
    exit 1
fi

echo -e "${GREEN}✓ Flask backend started successfully${NC}"
echo ""

# Start React frontend in background
echo -e "${YELLOW}Starting React frontend on http://localhost:3000...${NC}"
cd "$SCRIPT_DIR/frontend"
npm start > /tmp/react_dashboard.log 2>&1 &
REACT_PID=$!
echo -e "${GREEN}React PID: $REACT_PID${NC}"

# Wait for React to compile
echo -e "${YELLOW}Compiling React app (this may take a minute)...${NC}"
sleep 5

# Check if React is running
if ! ps -p $REACT_PID > /dev/null; then
    echo -e "${RED}React failed to start!${NC}"
    echo -e "${RED}Check /tmp/react_dashboard.log for errors${NC}"
    kill $FLASK_PID 2>/dev/null
    exit 1
fi

echo -e "${GREEN}✓ React frontend started successfully${NC}"
echo ""

# Print startup info
echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                 🎉 DASHBOARD STARTED! 🎉                   ║"
echo "╠════════════════════════════════════════════════════════════╣"
echo "║                                                            ║"
echo "║  🌐 Dashboard URL: http://localhost:3000                  ║"
echo "║  📊 API Server: http://localhost:5000                     ║"
echo "║                                                            ║"
echo "║  The dashboard will open automatically in your browser.   ║"
echo "║  If not, manually visit: http://localhost:3000            ║"
echo "║                                                            ║"
echo "║  Press Ctrl+C to stop both servers                        ║"
echo "║                                                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Wait for React to fully start (checking for the browser auto-open)
sleep 3

# Open browser if available
if command -v open &> /dev/null; then
    # macOS
    open "http://localhost:3000" 2>/dev/null
elif command -v xdg-open &> /dev/null; then
    # Linux
    xdg-open "http://localhost:3000" 2>/dev/null
elif command -v start &> /dev/null; then
    # Windows
    start "http://localhost:3000" 2>/dev/null
fi

# Function to cleanup on exit
cleanup() {
    echo -e "${YELLOW}"
    echo ""
    echo "Shutting down dashboard..."
    echo -e "${NC}"

    # Kill both processes
    if ps -p $FLASK_PID > /dev/null 2>&1; then
        kill $FLASK_PID 2>/dev/null
        echo -e "${GREEN}✓ Flask backend stopped${NC}"
    fi

    if ps -p $REACT_PID > /dev/null 2>&1; then
        kill $REACT_PID 2>/dev/null
        echo -e "${GREEN}✓ React frontend stopped${NC}"
    fi

    echo -e "${GREEN}Dashboard shutdown complete${NC}"
    exit 0
}

# Set trap to cleanup on Ctrl+C
trap cleanup SIGINT SIGTERM

# Keep script running
while true; do
    # Check if Flask process is still running
    if ! ps -p $FLASK_PID > /dev/null 2>&1; then
        echo -e "${RED}Flask backend stopped unexpectedly!${NC}"
        echo -e "${RED}Check /tmp/flask_dashboard.log for errors${NC}"
        kill $REACT_PID 2>/dev/null
        exit 1
    fi

    # Check if React process is still running
    if ! ps -p $REACT_PID > /dev/null 2>&1; then
        echo -e "${RED}React frontend stopped unexpectedly!${NC}"
        echo -e "${RED}Check /tmp/react_dashboard.log for errors${NC}"
        kill $FLASK_PID 2>/dev/null
        exit 1
    fi

    sleep 5
done
```

Now create a Windows batch file version as well:

```
Projekti_BigData/start-dashboard.bat
```

<edit_description>
Create batch startup script for Windows users
</edit_description>

```
@echo off
REM Stack Overflow Dashboard - Startup Script (Windows)
REM This script starts both the Flask backend and React frontend

setlocal enabledelayedexpansion

REM Colors - Windows 10+ supports ANSI
for /F %%A in ('echo prompt $H ^| cmd') do set "BS=%%A"

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
