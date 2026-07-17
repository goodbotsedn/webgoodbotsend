import streamlit as st
import pandas as pd
import zipfile
import io
import os

# --- DISEÑO TECNOLÓGICO Y AMIGABLE ---
st.set_page_config(
    page_title="WebGoodBot | Automatización",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo CSS para un look "Cyber/Tech"
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { 
        width: 100%; border-radius: 5px; height: 3em; 
        background-color: #00ff41; color: #000000; font-weight: bold; border: none;
    }
    .stButton>button:hover { background-color: #008f11; color: white; }
    h1 { color: #00ff41; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 WebGoodBot | Control Central")
st.markdown("<p style='text-align: center; color: #888;'>Plataforma de despliegue para robots de mensajería masiva.</p>", unsafe_allow_html=True)
st.markdown("---")

# ... (Aquí continúa todo tu código actual igual que antes) ...
