from app import app

def test_health_status():
    app.testing = True
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
