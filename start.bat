@echo off
echo :::: FLOWER-IDENTIFICATION-WEBAPP  Setting up services..... 
echo.
echo.
set FLASK_APP=flower.py
set FLASK_ENV=development
start cmd /k open.bat
flask run --host=0.0.0.0
pause