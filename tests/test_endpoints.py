from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_siembra_endpoint():
    response = client.post(
        "/api/v1/recomendaciones/siembra/",
        json={"lote_id": "1", "cliente_id": "1", "cultivo": "trigo"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "fecha_recomendada" in data
    assert "confianza" in data

def test_clima_endpoint():
    response = client.post(
        "/api/v1/recomendaciones/clima/",
        json={"region": "pamapa"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "precipitacion_mm" in data
    assert "temperatura_max" in data
    assert "temperatura_min" in data
