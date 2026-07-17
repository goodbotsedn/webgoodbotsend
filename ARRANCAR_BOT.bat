@echo off
title ROBOT DE ENVIO MASIVO - WHATSAPP
color 0A
cls
echo ===================================================
echo   INICIANDO BOT DE ENVIO MASIVO... 
echo ===================================================
echo.
echo   RECUERDE:
echo   1. WhatsApp Web debe estar abierto en Chrome.
echo   2. El archivo 'clientes.xlsx' debe estar cerrado.
echo   3. NO toque el mouse ni el teclado durante el envio.
echo.
echo ===================================================
echo   Ejecutando script de Python...
echo ===================================================
echo.

python "%~dp0envio_masivo.py"

echo.
echo ===================================================
echo   PROCESO TERMINADO POR COMPLETO
echo ===================================================
echo   Puedes cerrar esta ventana de forma segura.
echo ===================================================
pause