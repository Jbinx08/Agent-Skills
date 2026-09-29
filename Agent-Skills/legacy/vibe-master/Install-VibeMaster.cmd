@echo off
setlocal EnableExtensions
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0tools\Install-VibeMaster.ps1"
set "VIBE_EXIT=%ERRORLEVEL%"
echo.
if not "%VIBE_EXIT%"=="0" echo Installation failed with exit code %VIBE_EXIT%.
pause
exit /b %VIBE_EXIT%
