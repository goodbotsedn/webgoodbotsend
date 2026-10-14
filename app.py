from flask import Flask, render_template, request, send_file, flash
import os

app = Flask(__name__)
app.secret_key = 'godbotsend_secret_key_2026'

# Define aquí la clave para tus clientes
CLAVE_ACCESO = "1234"  # Cambia esta clave por la que entregas a tus clientes

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        clave_ingresada = request.form.get('clave', '').strip()
        
        if clave_ingresada == CLAVE_ACCESO:
            # Archivo objetivo a descargar (debe estar en la raíz de tu proyecto)
            archivo_path = 'clientes.xlsx'
            
            if os.path.exists(archivo_path):
                return send_file(
                    archivo_path,
                    as_attachment=True,
                    download_name='clientes.xlsx'
                )
            else:
                return render_template('index.html', error="El archivo no se encuentra disponible en el servidor.")
        else:
            return render_template('index.html', error="Clave incorrecta. Por favor, verifica e intenta nuevamente.")
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
