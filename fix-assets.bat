@echo off
echo ========================================
echo Fixing Asset Loading Issues
echo ========================================
echo.

echo Step 1: Clearing Vite cache...
if exist node_modules\.vite (
    rmdir /s /q node_modules\.vite
    echo Vite cache cleared.
) else (
    echo No Vite cache found.
)

echo.
echo Step 2: Clearing Laravel caches...
php artisan view:clear
php artisan config:clear
php artisan route:clear
php artisan cache:clear

echo.
echo ========================================
echo IMPORTANT: You need to run TWO terminals
echo ========================================
echo.
echo TERMINAL 1: Run this command and KEEP IT RUNNING:
echo   npm run dev
echo.
echo TERMINAL 2: Run this command and KEEP IT RUNNING:
echo   php artisan serve
echo.
echo Then visit: http://localhost:8000
echo Press Ctrl+Shift+R to hard refresh browser
echo.
pause

