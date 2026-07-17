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
    }
    .titulo { color: #00ff41; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- CABECERA E IMAGEN ---
st.markdown("<h1 class='titulo'>GOOD BOT SEND</h1>", unsafe_allow_html=True)

# Esta ruta es exacta a la que confirmamos en tu carpeta
st.image("static/imagenes/promocion.jpg", use_column_width=True)

# --- SEGURIDAD ---
# CAMBIA "TU_CLAVE" POR LA CONTRASEÑA QUE QUIERAS DARLES
clave_correcta = "TU_CLAVE" 

st.subheader("Acceso a Descargas")
clave_usuario = st.text_input("🔑 Ingresa tu clave:", type="password")

# --- LÓGICA DE DESCARGA ---
if clave_usuario == clave_correcta:
    st.success("✅ ¡Clave correcta! Ya puedes descargar.")
    
    # Asegúrate de que el archivo 'GoodBotSend.zip' esté en la carpeta raíz de tu GitHub
    try:
        with open("GoodBotSend.zip", "rb") as file:
            st.download_button(
                label="🚀 DESCARGAR GOODBOTSEND AHORA",
                data=file,
                file_name="GoodBotSend.zip",
                mime="application/zip"
            )
    except FileNotFoundError:
        st.error("Error: El archivo de descarga no se encuentra en el servidor.")
        
elif clave_usuario != "":
    st.error("❌ Clave incorrecta. Intenta de nuevo.")
