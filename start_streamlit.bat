@echo off
echo ========================================================
echo   ZYROO Ride Analytics & Revenue Intelligence Platform
echo   Launching Streamlit BI Dashboard (Port 8502)...
echo ========================================================
cd /d "%~dp0"
start "" "http://localhost:8502"
.\.venv\Scripts\streamlit.exe run app.py --server.port 8502 --server.headless false
pause
