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


def test_add_user_invalid_json_keys(test_app, test_database):
    client = test_app.test_client()

    resp = client.post(
        "/users",
        data=json.dumps({"email": "itfeels@like.de"}),
        content_type="application/json",
    )

    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Input payload validation failed" in data["message"]


def test_add_user_duplicate_email(test_app, test_database):
    client = test_app.test_client()

    client.post(
        "/users",
        data=json.dumps(
            {"username": "mf", "email": 'email": "whatmakesyouthink@imcoming.de'}
        ),
        content_type="application/json",
    )
    res = client.post(
        "/users",
        data=json.dumps(
            {"username": "mf", "email": 'email": "whatmakesyouthink@imcoming.de'}
        ),
        content_type="application/json",
    )

    data = json.loads(res.data.decode())
    assert res.status_code == 400
    assert "Sorry. That email already exists." in data["message"]
