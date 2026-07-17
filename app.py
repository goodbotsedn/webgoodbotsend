import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="GoodBotSend | Descarga", page_icon="🤖", layout="centered")

# --- ESTILOS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .btn-descarga>button { 
        background-color: #00ff41 !important; color: black !important; 
        font-weight: bold !important; width: 100% !important; height: 50px !important;
        border-radius: 8px !important;
    }
    .titulo { color: #00ff41; text-align: center; font-size: 2.5em; margin-bottom: 20px; }
    .info-text { text-align: center; color: #cccccc; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA ---
st.markdown("<h1 class='titulo'>GOOD BOT SEND</h1>", unsafe_allow_html=True)
st.markdown("<p class='info-text'>Sistema profesional de mensajería inteligente.</p>", unsafe_allow_html=True)

# --- IMAGEN (CORREGIDO PARA EVITAR EL TEXTO) ---
st.image("static/imagenes/promocion.jpg", use_container_width=True)

# --- SEGURIDAD ---
st.markdown("<hr>", unsafe_allow_html=True)
clave_usuario = st.text_input("🔑 Ingresa tu clave de acceso:", type="password")

# --- LÓGICA DE DESCARGA ---
if clave_usuario == "TU_CLAVE": # CAMBIA ESTO
    st.success("✅ Acceso autorizado. Iniciando descarga...")
    try:
        with open("GoodBotSend.zip", "rb") as file:
            st.download_button(
                label="🚀 DESCARGAR ARCHIVO",
                data=file,
                file_name="GoodBotSend.zip",
                mime="application/zip"
            )
    except FileNotFoundError:
        st.error("⚠️ El archivo de descarga no está disponible.")
elif clave_usuario != "":
    st.error("❌ Clave incorrecta. Acceso denegado.")
