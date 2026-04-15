from fastapi import FastAPI

app = FastAPI()

@get("/")
def read_root():
    return {"message": "Microservicio funcionando para Evaluación Parcial 1"}

@get("/status")
def get_status():
    return {"status": "online", "version": "1.0.0"}