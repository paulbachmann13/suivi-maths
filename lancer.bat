@echo off
cd /d "%~dp0"
if not exist .venv ( py -3.12 -m venv .venv && .venv\Scripts\python -m pip install -q -r requirements.txt )
.venv\Scripts\python seed.py
start "" http://127.0.0.1:5000
.venv\Scripts\python app.py
