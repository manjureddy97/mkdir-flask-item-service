from typing import Optional, Tuple

from .extensions import db
from .models import Item
from .errors import NotFoundError, ValidationError


def validate_item_payload(payload: dict) -> dict:
    """
    Validate JSON for creating/updating an Item.
    Expected:
    {
        "id": "<non-empty string>",
        "text": "<non-empty string>"
    }
    """
    if not isinstance(payload, dict):
        raise ValidationError("Request body must be a JSON object.")

    raw_id = payload.get("id")
    text = payload.get("text")

    if raw_id is None:
        raise ValidationError("Field 'id' is required.")
    if text is None:
        raise ValidationError("Field 'text' is required.")

    if not isinstance(raw_id, str) or not raw_id.strip():
        raise ValidationError("Field 'id' must be a non-empty string.")

    if not isinstance(text, str) or not text.strip():
        raise ValidationError("Field 'text' must be a non-empty string.")

    return {"id": raw_id.strip(), "text": text.strip()}


def save_item(data: dict) -> Tuple[Item, bool]:
    """
    Create or update an item.
    Returns (item, created_flag)
    """
    item_id = data["id"]
    text = data["text"]

    item = Item.query.get(item_id)  # type: Optional[Item]
    created = False

    if item is None:
        item = Item(id=item_id, text=text)
        db.session.add(item)
        created = True
    else:
        item.text = text

    db.session.commit()
    return item, created


def get_item(item_id: str) -> Item:
    if not item_id or not isinstance(item_id, str):
        raise ValidationError("Item id must be a non-empty string.")

    item = Item.query.get(item_id)
    if item is None:
        raise NotFoundError("Item with id '{}' not found.".format(item_id))
    return item
