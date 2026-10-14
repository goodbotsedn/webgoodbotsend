from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

# Configura aquí la clave secreta con la que tus clientes descargan los archivos
CLAVE_ACCESSO = "1234" # Cambia esto por la clave que usas actualmente

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        ingreso = request.form.get('clave')
        if ingreso == CLAVE_ACCESSO:
            # Si la clave es correcta, descarga el archivo de clientes o muestra el panel de descarga
            return send_from_directory(directory='.', path='clientes.xlsx', as_attachment=True)
        else:
            error = "Clave incorrecta. Inténtalo de nuevo."
            
    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
