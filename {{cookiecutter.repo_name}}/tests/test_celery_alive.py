def test_alive_002_test_celery_alive(test_app):
    test_app.config["CELERY_TASK_ALWAYS_EAGER"]=True
    client = test_app.test_client()
    resp = client.get("/alive/celery")
    assert resp.status_code == 200
    assert "celeryalive" in resp.json["message"]
    assert "task_id" in resp.json
