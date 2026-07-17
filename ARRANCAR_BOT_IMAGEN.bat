@echo off
title ROBOT - TEXTO E IMAGEN (VERSION ESTABLE)
color 0B
cls
echo ===================================================
echo   INICIANDO BOT DE ENVIO: TEXTO + IMAGEN
echo ===================================================
echo.
echo   RECUERDE EL PROTOCOLO DE SEGURIDAD:
echo   1. WhatsApp Web debe estar abierto en Google Chrome.
echo   2. El archivo 'clientes.xlsx' DEBE ESTAR CERRADO.
echo   3. La foto en la carpeta debe llamarse exactamente 'foto.jpg'.
echo   4. NUEVO: El bot esperara 5s extras entre texto e imagen.
echo   5. NO TOQUE EL MOUSE NI EL TECLADO durante el envio.
echo.
echo ===================================================
echo   Ejecutando script de enfoque optimizado...
echo ===================================================
echo.

python "%~dp0envio_imagen.py"

echo.
echo ===================================================
echo   PROCESO TERMINADO POR COMPLETO
echo ===================================================
pause