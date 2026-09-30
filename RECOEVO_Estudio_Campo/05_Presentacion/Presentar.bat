@echo off
REM Abre la presentacion RECOEVO con servidor local (mapa sin internet y audios al minuto exacto).
cd /d "%~dp0"
python servidor.py
if errorlevel 1 (
  echo No se encontro Python. Abriendo el archivo directamente: el mapa necesitara internet.
  start "" "%~dp0index.html"
  pause
)
