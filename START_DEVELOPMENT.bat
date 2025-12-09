@echo off
title Pathfinder Development Servers
color 0A
echo ========================================
echo  Pathfinder Development Environment
echo ========================================
echo.
echo This will start BOTH required servers.
echo Keep this window open!
echo.
echo Press Ctrl+C to stop both servers
echo ========================================
echo.

cd /d "%~dp0"

echo Starting Vite Dev Server (Terminal 1)...
start "Vite Dev Server" cmd /k "npm run dev"

timeout /t 3 /nobreak >nul

echo Starting Laravel Server (Terminal 2)...
start "Laravel Server" cmd /k "php artisan serve"

echo.
echo ========================================
echo  Servers are starting!
echo ========================================
echo.
echo Vite: http://localhost:5173
echo Laravel: http://localhost:8000
echo.
echo Visit: http://localhost:8000 in your browser
echo Press Ctrl+Shift+R to hard refresh
echo.
echo Keep both terminal windows open!
echo ========================================
echo.
pause

