import json


def test_ping(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.get("/ping")
    data = json.loads(resp.data.decode())

    # Then
    assert resp.status_code == 200
    assert "Urantia" in data["message"]
    assert "success" in data["status"]


def test_add_user_invalid_json(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        "/users",
        data=json.dumps({}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]
