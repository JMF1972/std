@echo off
echo Tancant ChatGPT si esta obert...

taskkill /IM ChatGPT.exe /F >nul 2>&1

echo Esperant 2 segons...
timeout /t 2 >nul

echo Obrint ChatGPT...
start "" "https://chat.openai.com"

echo Fet!
