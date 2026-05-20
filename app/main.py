# app/main.py

from fastapi import FastAPI

app = FastAPI(
    title="Tontine API",
    description="Système de gestion de tontines",
    version="1.0.0"
)

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API Tontine 🎉"}

@app.get("/health")
def health_check():
    return {"status": "ok"}