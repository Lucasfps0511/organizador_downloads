@echo off
:: Navega até a pasta do projeto
cd /d "%~dp0"

:: Ativa o ambiente virtual e roda o script
call venv\Scripts\activate
python project.py

:: Fecha a janela após terminar
exit