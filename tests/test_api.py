from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"Status": "OK"}


def test_stats_endpoint():
    response = client.post("/stats", json={"text": "go Go go stop", "top_n": 1})
    assert response.status_code == 200
    body = response.json()
    assert body["words"] == 4
    assert body["characters"] == 13
    assert body["top_words"][0] == ["go", 3]


def test_stats_rejects_missing_text():
    response = client.post("/stats", json={})
    assert response.status_code == 422
