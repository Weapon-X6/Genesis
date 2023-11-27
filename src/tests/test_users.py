import json


def test_add_user(test_app, test_database):
    client = test_app.test_client()

    resp = client.post(
        "/users",
        data=json.dumps({"username": "ed", "email": "new@rdriven.de"}),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())

    assert resp.status_code == 201
    assert "new@rdriven.de was added!" in data["message"]


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
