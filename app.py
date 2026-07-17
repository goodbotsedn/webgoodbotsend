import streamlit as st
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="GoodBotSend | Descarga", page_icon="🤖", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .btn-descarga>button { 
        background-color: #00ff41 !important; color: black !important; 
        font-weight: bold !important; width: 100% !important; height: 50px !important;
    }
    .titulo { color: #00ff41; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA Y LOGO ---
st.markdown("<h1 class='titulo'>GOOD BOT SEND</h1>", unsafe_allow_html=True)

# Aquí debes asegurarte de tener la imagen en tu GitHub o usar una URL pública
# st.image("https://tu-url-de-la-imagen.com/goodbotsend.jpg", use_column_width=True)
st.image("https://i.imgur.com/TuCodigoDeImagen.jpg", use_column_width=True) # Reemplaza esto con tu URL de imagen real

# --- SEGURIDAD ---
clave_correcta = "TU_CLAVE_AQUI" # CAMBIA ESTO POR TU CLAVE SECRETA
clave_usuario = st.text_input("🔑 Ingresa tu clave de acceso para descargar:", type="password")

# --- LÓGICA DE DESCARGA ---
if clave_usuario == clave_correcta:
    st.success("✅ ¡Clave correcta! Ya puedes descargar.")
    
    # Aquí irá la ruta del archivo que subas a tu GitHub
    with open("GoodBotSend.zip", "rb") as file:
        btn = st.download_button(
            label="🚀 DESCARGAR GOODBOTSEND AHORA",
            data=file,
            file_name="GoodBotSend.zip",
            mime="application/zip",
            key="btn-descarga"
        )
elif clave_usuario != "":
    st.error("❌ Clave incorrecta. Contacta con el administrador.")
