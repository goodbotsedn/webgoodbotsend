from flask import Flask, render_template, request, send_file
import os
import zipfile

app = Flask(__name__)

# Clave de acceso exacta
CLAVE_ACCESO = "Modulo.10"

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        clave_ingresada = request.form.get('clave', '').strip()
        
        if clave_ingresada == CLAVE_ACCESO:
            zip_filename = 'GODBOTSEND_PAQUETE_COMPLETO.zip'
            
            # Lista exacta de archivos del bot a empaquetar para el cliente
            archivos_a_incluir = [
                'ARRANCAR_BOT.bat',
                'ARRANCAR_BOT_IMAGEN.bat',
                'envio_masivo.py',
                'envio_imagen.py',
                'clientes.xlsx',
                'foto.jpg',
                'MANUAL DE INSTALACIÓN Y USO.txt'
            ]
            
            # Crea el archivo ZIP incluyendo solo los archivos existentes
            with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for archivo in archivos_a_incluir:
                    if os.path.exists(archivo):
                        zipf.write(archivo)
            
            if os.path.exists(zip_filename):
                return send_file(
                    zip_filename,
                    as_attachment=True,
                    download_name='GODBOTSEND_PAQUETE_COMPLETO.zip'
                )
            else:
                error = "No se pudieron encontrar los archivos en el servidor."
        else:
            error = "Clave incorrecta. Por favor, verifica e intenta nuevamente."
            
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
