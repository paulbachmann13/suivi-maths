@echo off
title Suivi maths
cd /d "%~dp0"

rem Premiere utilisation : cree l'environnement Python et installe Flask
if not exist ".venv\Scripts\python.exe" (
    echo Premiere installation, patiente quelques secondes...
    py -3.12 -m venv .venv || py -3 -m venv .venv
    ".venv\Scripts\python.exe" -m pip install -q -r requirements.txt
)

rem Cree la base et charge le programme si besoin (ne touche pas a tes donnees)
".venv\Scripts\python.exe" seed.py >nul

rem Si une ancienne version de l'appli tourne encore, on l'arrete pour repartir sur la derniere version
for /f "tokens=5" %%p in ('netstat -ano ^| findstr ":5000" ^| findstr "LISTENING"') do taskkill /PID %%p /F /T >nul 2>&1
timeout /t 1 /nobreak >nul

start "" /b cmd /c "timeout /t 2 /nobreak >nul & start http://127.0.0.1:5000"
echo.
echo   Suivi maths tourne sur http://127.0.0.1:5000
echo   Ferme cette fenetre pour arreter l'appli.
echo.
".venv\Scripts\python.exe" app.py
