import streamlit as st
import pandas as pd
import zipfile
import io
import os

# --- DISEÑO ---
st.set_page_config(page_title="WebGoodBot", page_icon="🤖", layout="centered")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    .stButton>button { background-color: #00ff41; color: black; font-weight: bold; }
    h1 { color: #00ff41; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 WebGoodBot | Centro de control")
st.markdown("<p style='text-align: center; color: #888;'>Plataforma de despliegue para robots.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- ELEMENTOS QUE FALTABAN ---
mensaje_usuario = st.text_area("✍️ Escribe el mensaje:")
archivo_excel = st.file_uploader("📊 Sube tu Excel", type=["xlsx"])
archivo_imagen = st.file_uploader("🖼️ Sube tu imagen", type=["jpg", "jpeg", "png"])

if st.button("🚀 Generar Carpeta del Robot"):
    if mensaje_usuario and archivo_excel:
        st.success("✅ ¡Todo listo! Procesando...")
        # AQUÍ IRÍA LA LÓGICA DE TU ZIP QUE YA TENÍAS
    else:
        st.error("⚠️ Por favor completa los campos.")
