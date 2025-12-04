import json

from app import create_app
from app.config import TestConfig
from app.extensions import db


def test_save_and_get_item():
    # Create app with test config (in-memory SQLite)
    app = create_app(TestConfig)

    # Setup DB
    with app.app_context():
        db.create_all()

    client = app.test_client()

    # 1) POST /save
    payload = {"id": "123", "text": "Hello world"}
    resp = client.post(
        "/save",
        data=json.dumps(payload),
        content_type="application/json",
    )

    assert resp.status_code == 201
    data = resp.get_json()
    assert data["status"] == "ok"
    assert data["item"]["id"] == "123"
    assert data["item"]["text"] == "Hello world"

    # 2) GET /item/123
    resp2 = client.get("/item/123")
    assert resp2.status_code == 200
    item_data = resp2.get_json()
    assert item_data["id"] == "123"
    assert item_data["text"] == "Hello world"
