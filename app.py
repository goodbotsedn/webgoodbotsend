import streamlit as st
import zipfile
import io
import os

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="GoodBotSend | Descarga", page_icon="🤖", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .btn-descarga>button { background-color: #00ff41 !important; color: black !important; font-weight: bold !important; width: 100% !important; height: 50px !important; }
    .titulo { color: #00ff41; text-align: center; font-size: 2.5em; margin-bottom: 20px; }
    .info-text { text-align: center; color: #cccccc; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 class='titulo'>GOOD BOT SEND</h1>", unsafe_allow_html=True)
st.markdown("<p class='info-text'>Sistema profesional de mensajería inteligente.</p>", unsafe_allow_html=True)

# Imagen (usando la ruta que ya tienes)
st.image("static/imagenes/promocion.jpg", use_container_width=True)

# --- LÓGICA DE COMPRESIÓN ---
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

# --- SEGURIDAD ---
st.markdown("<hr>", unsafe_allow_html=True)
clave_usuario = st.text_input("🔑 Ingresa tu clave de acceso:", type="password")

# --- LÓGICA DE DESCARGA ---
if clave_usuario == "1234": # CAMBIA ESTO POR LA CLAVE QUE QUIERAS
    st.success("✅ Acceso autorizado. Iniciando descarga...")
    st.download_button(
        label="🚀 DESCARGAR ARCHIVOS",
        data=crear_zip(),
        file_name="GoodBotSend.zip",
        mime="application/zip"
    )
elif clave_usuario != "":
    st.error("❌ Clave incorrecta.")
