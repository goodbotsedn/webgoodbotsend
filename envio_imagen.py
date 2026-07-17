import pandas as pd
import pywhatkit as kit
import time
import os
from datetime import datetime

# CONFIGURACIÓN DE RUTAS AUTOMÁTICAS
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EXCEL = os.path.join(DIRECTORIO_ACTUAL, "clientes.xlsx")
RUTA_IMAGEN = os.path.join(DIRECTORIO_ACTUAL, "foto.jpg")
RUTA_REPORTE = os.path.join(DIRECTORIO_ACTUAL, "reporte_envio_imagen.txt")

# LISTA DE TIEMPOS ROTATIVOS (Se repite: 20s, 25s, 30s)
TIEMPOS_ESPERA = [20, 25, 30]

# Función para escribir en el reporte de texto (.txt)
def registrar_en_reporte(numero, estado, detail):
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linea = f"[{fecha_hora}] | Número: {numero} | Estado: {estado} | Detalle: {detail}\n"
    with open(RUTA_REPORTE, "a", encoding="utf-8") as archivo:
        archivo.write(linea)

# 1. El robot lee tu base de datos
try:
    datos = pd.read_excel(RUTA_EXCEL)
except Exception as e:
    print(f"❌ ¡Error! No encontré el archivo 'clientes.xlsx' en: {RUTA_EXCEL}")
    input("\nPresiona Enter para salir...")
    exit()

# Verificar de forma estricta si la imagen existe
if not os.path.exists(RUTA_IMAGEN):
    print(f"❌ ¡Error crítico! No encontré la imagen 'foto.jpg' en: {RUTA_IMAGEN}")
    input("\nPresiona Enter para salir...")
    exit()

print("===============================================================")
print("🤖 ¡SISTEMA SEGURO DE ENVÍO DE IMAGEN!")
print("MODO: TEXTO + IMAGEN (MÉTODO NATIVO SIN EXTRAS)")
print("===============================================================")

# 2. El robot revisa la lista fila por fila
for indice, fila in datos.iterrows():
    numero = str(fila['Telefono']).split(".")[0].strip()
    mensaje = str(fila['Mensaje']).strip()
    
    numero_final = "+" + numero if not numero.startswith("+") else numero

    print(f"\n[{indice + 1}] Enviando Imagen + Texto a: {numero_final}")

    try:
        # 3. Envío directo usando la función nativa de pywhatkit para imágenes
        # Esta función abre el chat, adjunta la imagen y escribe el mensaje automáticamente.
        kit.sendwhats_image(
            receiver=numero_final,
            img_path=RUTA_IMAGEN,
            caption=mensaje,
            wait_time=25,       # Tiempo base seguro para que cargue la interfaz
            tab_close=True,     # Que cierre la pestaña automáticamente al terminar
            close_time=5        # Espera 5 segundos antes de cerrar para asegurar el envío
        )
        
        print("✅ ¡Mensaje e Imagen procesados!")
        registrar_en_reporte(numero_final, "ENVIADO", "Mensaje de texto y foto enviados con éxito.")
        
        # 4. CÁLCULO DEL TIEMPO ROTATIVO SUCESIVO (20s, 25s, 30s)
        tiempo_espera = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        print(f"⏳ Descanso rotativo: Esperando {tiempo_espera} segundos antes del siguiente...")
        time.sleep(tiempo_espera)

    except KeyboardInterrupt:
        print("\n🛑 Proceso detenido manualmente por el usuario.")
        break
    except Exception as e:
        print(f"❌ Error en el envío: {numero_final}")
        registrar_en_reporte(numero_final, "FALLADO", "El número no existe en WhatsApp o la página tardó demasiado en cargar.")
        
        # Si falla, igual respetamos el tiempo de espera para proteger la cuenta
        tiempo_espera_fallo = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        print(f"⏳ Esperando {tiempo_espera_fallo} segundos antes del siguiente...")
        time.sleep(tiempo_espera_fallo)

print("\n🏁 ¡Proceso terminado por completo!")
print(f"📄 Reporte actualizado en: {RUTA_REPORTE}")
input("Presiona Enter para cerrar esta ventana...")