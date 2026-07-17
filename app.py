import streamlit as st
import zipfile
import io
import os

# Configuración básica
st.set_page_config(page_title="Descarga", layout="centered")

st.title("GOOD BOT SEND")

# --- CORRECCIÓN DE IMAGEN ---
# Verificamos si existe la imagen en la ruta que usamos anteriormente
ruta_imagen = "static/imagenes/promocion.jpg"
if os.path.exists(ruta_imagen):
    st.image(ruta_imagen, use_container_width=True)
else:
    st.warning(f"La imagen no se encontró en: {ruta_imagen}. Verifica si está ahí o si el nombre es diferente.")

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

# Validación
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
