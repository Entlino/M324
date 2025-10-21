from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_items_end_to_end_flow():
    # Start: Liste holen
    r = client.get("/items")
    assert r.status_code == 200
    start_len = len(r.json())

    # Neues Item anlegen
    r = client.post("/items", json={"text": "Testtodo"})
    assert r.status_code == 201
    created = r.json()
    assert "id" in created and created["text"] == "Testtodo"

    # Liste erneut: Länge +1
    r = client.get("/items")
    assert r.status_code == 200
    assert len(r.json()) == start_len + 1
