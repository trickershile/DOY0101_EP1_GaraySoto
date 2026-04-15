from fastapi import FastAPI
import os

app = FastAPI()

# --- CONFIGURACIÓN (HOTFIX) ---
def verificar_configuracion():
    """Simulamos una corrección crítica para producción."""
    api_key = os.getenv("API_KEY", "DEVELOPMENT_MODE")
    if api_key == "DEVELOPMENT_MODE":
        print("ALERTA: Iniciando en modo desarrollo. Configure API_KEY en producción.")
    return True

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Microservicio funcionando para Evaluación Parcial 1"}

@app.get("/status")
def get_status():
    return {"status": "online", "version": "1.0.0"}

# --- SEGUNDA FEATURE ---
@app.get("/health")
def health_check():
    """Endpoint de salud del microservicio."""
    return {
        "status": "UP",
        "version": "1.0.1",
        "environment": "production"
    }

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    verificar_configuracion()
    print("Microservicio listo para ser ejecutado.")