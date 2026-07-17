import streamlit as st
import zipfile
import io
import os

# Configuración básica
st.set_page_config(page_title="Descarga", layout="centered")

st.title("GOOD BOT SEND")

# Lógica de creación de ZIP
def crear_zip():
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        archivos = [
            "clientes.xlsx", "envio_imagen.py", "envio_masivo.py", "foto.jpg", 
            "MANUAL DE INSTALACIÓN Y CONFIGURACIÓN DESDE CERO.pdf", 
            "ARRANCAR_BOT.bat", "ARRANCAR_BOT_IMAGEN.bat"
        ]
        for archivo in archivos:
            if os.path.exists(archivo):
                zf.write(archivo)
    return zip_buffer.getvalue()

# Entrada de clave
clave = st.text_input("Ingresa la clave:", type="password")

# Validación estricta
if clave == "Modulo10":
    st.success("Acceso concedido")
    st.download_button(
        label="DESCARGAR ARCHIVOS",
        data=crear_zip(),
        file_name="GoodBotSend.zip",
        mime="application/zip"
    )
elif clave != "":
    st.error("Clave incorrecta")
