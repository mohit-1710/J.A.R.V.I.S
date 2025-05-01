@echo off
echo Starting J.A.R.V.I.S...
call .venv\Scripts\activate.bat

:loop
python Jarvis.py
echo J.A.R.V.I.S. stopped or crashed. Restarting...
timeout /t 3 >nul
goto loop 