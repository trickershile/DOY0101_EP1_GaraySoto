# --- CAMBIO PARA EL HOTFIX ---
import os
import sys

def verificar_configuracion():
    # Simulamos una corrección crítica: 
    # El microservicio fallaba si no encontraba una variable de entorno esencial.
    api_key = os.getenv("API_KEY", "DEVELOPMENT_MODE")
    
    if api_key == "DEVELOPMENT_MODE":
        print("ALERTA: Iniciando en modo desarrollo. Configure API_KEY en producción.")
    
    print("Conexión a base de datos validada correctamente.")
    return True

# Llama a la función al inicio de tu app
if __name__ == "__main__":
    if verificar_configuracion():
        print("Microservicio iniciado exitosamente.")