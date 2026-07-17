import pandas as pd
import pywhatkit as kit
import time
import pyautogui
import os
from datetime import datetime

# CONFIGURACIÓN DE RUTAS AUTOMÁTICAS
DIRECTORIO_ACTUAL = os.path.dirname(os.path.abspath(__file__))
RUTA_EXCEL = os.path.join(DIRECTORIO_ACTUAL, "clientes.xlsx")
RUTA_REPORTE = os.path.join(DIRECTORIO_ACTUAL, "reporte_envio_texto.txt")

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

print("===============================================================")
print("🤖 ¡SISTEMA SEGURO DE ENVÍO DE TEXTO!")
print("MODO: SOLO TEXTO (TIEMPOS ROTATIVOS: 20s, 25s, 30s)")
print("===============================================================")

# 2. El robot revisa la lista fila por fila
for indice, fila in datos.iterrows():
    numero = str(fila['Telefono']).split(".")[0].strip()
    mensaje = str(fila['Mensaje']).strip()
    
    numero_final = "+" + numero if not numero.startswith("+") else numero

    print(f"\n[{indice + 1}] Abriendo WhatsApp para: {numero_final}")

    try:
        # 3. Abre el navegador con un tiempo inicial seguro de 25 segundos
        kit.sendwhatmsg_instantly(
            phone_no=numero_final, 
            message=mensaje, 
            wait_time=25,       # Tiempo base súper estable para cargar el chat
            tab_close=False,    
            close_time=0
        )
        
        # 4. Tiempo de estabilización corto
        print("Estabilizando pantalla...")
        time.sleep(5)
        
        # 5. ENVIAR TEXTO
        print("Enviando mensaje de texto...")
        pyautogui.press('enter')
        time.sleep(5) # Espera para que el mensaje realmente se envíe
        
        # Registramos el éxito en el reporte
        print("✅ ¡Mensaje procesado!")
        registrar_en_reporte(numero_final, "ENVIADO", "Mensaje enviado correctamente.")
        
        # 6. Limpieza rápida de pestaña
        print("Cerrando pestaña...")
        pyautogui.hotkey('ctrl', 'w') 
        
        # 7. CÁLCULO DEL TIEMPO ROTATIVO SUCESIVO (20s, 25s, 30s)
        # El operador % hace que si vamos en el envío 1, use 20. Envío 2, 25. Envío 3, 30. Envío 4, 20...
        tiempo_espera = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        
        print(f"⏳ Descanso rotativo: Esperando {tiempo_espera} segundos antes del siguiente...")
        time.sleep(tiempo_espera)

    except KeyboardInterrupt:
        print("\n🛑 Proceso detenido manualmente por el usuario.")
        break
    except Exception as e:
        # Si el número no existe o se traba la página, entra aquí
        print(f"❌ Número sin WhatsApp o error en la carga: {numero_final}")
        registrar_en_reporte(numero_final, "FALLADO", "El número no está registrado en WhatsApp o la página tardó demasiado en cargar.")
        
        # Cerramos la pestaña de todas formas para limpiar pantalla
        try:
            pyautogui.hotkey('ctrl', 'w')
        except:
            pass
        
        # Si falla, igual le damos el tiempo de espera que le tocaba en el ciclo para no romper el patrón
        tiempo_espera_fallo = TIEMPOS_ESPERA[indice % len(TIEMPOS_ESPERA)]
        print(f"⏳ Esperando {tiempo_espera_fallo} segundos antes de continuar con el siguiente número...")
        time.sleep(tiempo_espera_fallo)

print("\n🏁 ¡Proceso terminado por completo!")
print(f"📄 Reporte actualizado en: {RUTA_REPORTE}")
input("Presiona Enter para cerrar esta ventana...")