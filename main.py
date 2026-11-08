from fastapi import FastAPI

from calculatrice import addition, multiplication

app = FastAPI(title="API Calculatrice")


@app.get("/")
def accueil():
    return {"message": "Bienvenue sur mon API"}


@app.get("/addition")
def calculer_addition(a: float, b: float):
    return {"resultat": addition(a, b)}


@app.get("/multiplication")
def calculer_multiplication(a: float, b: float):
    return {"resultat": multiplication(a, b)}
