@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
    py -3 "%~dp0install.py"
) else (
    python "%~dp0install.py"
)
set "install_status=%errorlevel%"
echo.
pause
exit /b %install_status%
