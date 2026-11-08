from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_accueil():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur mon API"}


def test_addition_api():
    response = client.get("/addition?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"resultat": 8.0}


def test_multiplication_api():
    response = client.get("/multiplication?a=4&b=3")
    assert response.status_code == 200
    assert response.json() == {"resultat": 12.0}


def test_parametre_invalide():
    response = client.get("/addition?a=abc&b=3")
    assert response.status_code == 422
