import json


def test_alive_001_test_alive(test_app):
    client = test_app.test_client()
    resp = client.get("/alive")
    data = resp.json()
    assert resp.status_code == 200
    assert "alive" in data["message"]
