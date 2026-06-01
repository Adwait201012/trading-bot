@echo off
echo Setting up Indian Stock Market Trading Bot...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Install from https://python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Setup complete!
echo.
echo To run the bot:
echo   python main.py              -- continuous mode (every 5 min)
echo   python main.py --once       -- single scan
echo   python main.py --portfolio  -- show portfolio
echo   python main.py --reset      -- reset portfolio
echo.
pause
