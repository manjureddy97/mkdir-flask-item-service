from flask import Blueprint, request, jsonify

from .services import validate_item_payload, save_item, get_item

items_bp = Blueprint("items", __name__)


@items_bp.route("/save", methods=["POST"])
def save():
    """
    POST /save
    Body JSON:
    {
        "id": "<string>",
        "text": "<string>"
    }
    """
    json_data = request.get_json(silent=False)
    validated = validate_item_payload(json_data)
    item, created = save_item(validated)

    status_code = 201 if created else 200
    return jsonify({"status": "ok", "item": item.to_dict()}), status_code


@items_bp.route("/item/<string:item_id>", methods=["GET"])
def get_item_route(item_id: str):
    """
    GET /item/<id>
    """
    item = get_item(item_id)
    return jsonify(item.to_dict()), 200
