@echo off

echo ==========================
echo      STD Builder
echo ==========================

pip install pyinstaller

pyinstaller --onefile --windowed std\main.py --name std

echo.
echo Build completat
echo Aquesta finestra es tancara en 30 segons

timeout /t 30