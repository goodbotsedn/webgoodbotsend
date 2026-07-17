import streamlit as st
import pandas as pd
import zipfile
import io
import os

# Configuración de la página web
st.set_page_config(page_title="Generador de Campañas - WhatsApp Masivo", page_icon="🤖", layout="centered")

st.title("🤖 Generador de Campañas WhatsApp")
st.write("Sube tu lista de contactos, escribe tu mensaje y descarga tu robot listo para usar en tu computadora.")

st.markdown("---")

# 1. Entrada de datos por el usuario
mensaje_usuario = st.text_area("✍️ Escribe el mensaje que enviarás a tus clientes:", placeholder="Hola {Nombre}, mira nuestra oferta de hoy...")

# Subida de Excel
archivo_excel = st.file_uploader("📊 Sube tu archivo Excel (.xlsx)", type=["xlsx"])

# Subida opcional de imagen
archivo_imagen = st.file_uploader("🖼️ Sube tu foto (Opcional - Solo si enviarás Imagen + Texto)", type=["jpg", "jpeg", "png"])

st.markdown("---")

# Botón para procesar y generar el ZIP
if st.button("🚀 Generar Carpeta del Robot"):
    if not mensaje_usuario:
        st.error("⚠️ Por favor, escribe un mensaje antes de continuar.")
    elif archivo_excel is None:
        st.error("⚠️ Por favor, sube un archivo Excel con tus contactos.")
    else:
        with st.spinner("Procesando datos y preparando tu descarga..."):
            try:
                # Leer el Excel que subió el usuario para verificar que esté correcto
                df = pd.read_excel(archivo_excel)
                
                # Crear un buffer en memoria para almacenar el archivo ZIP sin escribir en el disco del servidor
                zip_buffer = io.BytesIO()
                
                with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
                    
                    # 1. Guardar el archivo Excel tal cual dentro del ZIP
                    excel_data = archivo_excel.getvalue()
                    zip_file.writestr("envio masivo/clientes.xlsx", excel_data)
                    
                    # 2. Guardar la imagen si fue subida
                    if archivo_imagen is not None:
                        imagen_data = archivo_imagen.getvalue()
                        zip_file.writestr("envio masivo/foto.jpg", imagen_data)
                    
                    # 3. Escribir el script 'envio_masivo.py' (Solo Texto)
                    codigo_texto = """import pandas as pd
import pywhatkit as kit
import time
import os
from datetime import datetime

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EXCEL = os.path.join(DIRECTORIO_ACTUAL, "clientes.xlsx")
RUTA_REPORTE = os.path.join(DIRECTORIO_ACTUAL, "reporte_envio_texto.txt")
TIEMPOS_ESPERA = [20, 25, 30]

def registrar_en_reporte(numero, estado, detail):
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linea = f"[{fecha_hora}] | Número: {numero} | Estado: {estado} | Detalle: {detail}\\n"
    with open(RUTA_REPORTE, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

try:
    datos = pd.read_excel(RUTA_EXCEL)
except Exception as e:
    print("❌ Error al leer 'clientes.xlsx'")
    exit()

print("🤖 ¡ROBOT INICIADO - MODO SOLO TEXTO!")
for indice, fila in datos.iterrows():
    numero = str(fila['Telefono']).split(".")[0].strip()
    mensaje = str(fila['Mensaje']).strip()
    numero_final = "+" + numero if not numero.startswith("+") else numero
    print(f"\\n[{indice + 1}] Enviando a: {numero_final}")
    try:
        kit.sendwhatmsg_instantly(phone_no=numero_final, message=mensaje, wait_time=25, tab_close=True, close_time=5)
        print("✅ ¡Mensaje procesado!")
        registrar_en_reporte(numero_final, "ENVIADO", "Mensaje de texto enviado correctamente.")
        tiempo_espera = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        print(f"⏳ Esperando {tiempo_espera} segundos...")
        time.sleep(tiempo_espera)
    except Exception as e:
        print(f"❌ Error en el envío: {numero_final}")
        registrar_en_reporte(numero_final, "FALLADO", "Error en el envío.")
        time.sleep(20)
"""
                    zip_file.writestr("envio masivo/envio_masivo.py", codigo_texto)

                    # 4. Escribir el script 'envio_imagen.py' (Texto + Imagen)
                    codigo_imagen = """import pandas as pd
import pywhatkit as kit
import time
import os
from datetime import datetime

DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EXCEL = os.path.join(DIRECTORIO_ACTUAL, "clientes.xlsx")
RUTA_IMAGEN = os.path.join(DIRECTORIO_ACTUAL, "foto.jpg")
RUTA_REPORTE = os.path.join(DIRECTORIO_ACTUAL, "reporte_envio_imagen.txt")
TIEMPOS_ESPERA = [20, 25, 30]

def registrar_en_reporte(numero, estado, detail):
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linea = f"[{fecha_hora}] | Número: {numero} | Estado: {estado} | Detalle: {detail}\\n"
    with open(RUTA_REPORTE, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

try:
    datos = pd.read_excel(RUTA_EXCEL)
except Exception as e:
    print("❌ Error al leer 'clientes.xlsx'")
    exit()

print("🤖 ¡ROBOT INICIADO - MODO IMAGEN + TEXTO!")
for indice, fila in datos.iterrows():
    numero = str(fila['Telefono']).split(".")[0].strip()
    mensaje = str(fila['Mensaje']).strip()
    numero_final = "+" + numero if not numero.startswith("+") else numero
    print(f"\\n[{indice + 1}] Enviando Imagen a: {numero_final}")
    try:
        kit.sendwhats_image(receiver=numero_final, img_path=RUTA_IMAGEN, caption=mensaje, wait_time=25, tab_close=True, close_time=5)
        print("✅ ¡Mensaje e Imagen procesados!")
        registrar_en_reporte(numero_final, "ENVIADO", "Enviado con éxito.")
        tiempo_espera = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        print(f"⏳ Esperando {tiempo_espera} segundos...")
        time.sleep(tiempo_espera)
    except Exception as e:
        print(f"❌ Error en el envío: {numero_final}")
        registrar_en_reporte(numero_final, "FALLADO", "Error en el envío.")
        time.sleep(20)
"""
                    zip_file.writestr("envio masivo/envio_imagen.py", codigo_imagen)

                    # 5. Escribir el ejecutable 'ARRANCAR_BOT.bat'
                    bat_texto = """@echo off
color 0A
title ROBOT DE ENVIO MASIVO - TEXTO
python "%~dp0envio_masivo.py"
pause"""
                    zip_file.writestr("envio masivo/ARRANCAR_BOT.bat", bat_texto)

                    # 6. Escribir el ejecutable 'ARRANCAR_BOT_IMAGEN.bat'
                    bat_imagen = """@echo off
color 0A
title ROBOT DE ENVIO MASIVO - IMAGEN
python "%~dp0envio_imagen.py"
pause"""
                    zip_file.writestr("envio masivo/ARRANCAR_BOT_IMAGEN.bat", bat_imagen)

                # Resetear el puntero del buffer para que pueda ser leído para la descarga
                zip_buffer.seek(0)
                
                st.success("🎉 ¡Carpeta del Robot generada con éxito!")
                
                # Botón de descarga para el usuario
                st.download_button(
                    label="💾 Descargar Carpeta del Robot (.zip)",
                    data=zip_buffer,
                    file_name="campana_whatsapp_listo.zip",
                    mime="application/zip"
                )
                
            except Exception as error_global:
                st.error(f"❌ Ocurrió un error al procesar el archivo: {error_global}")
