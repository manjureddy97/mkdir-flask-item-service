from .extensions import db


class Item(db.Model):
    """
    Simple key-value store item.
    """
    __tablename__ = "items"

    id = db.Column(db.String(255), primary_key=True)
    text = db.Column(db.Text, nullable=False)

    def to_dict(self) -> dict:
        return {"id": self.id, "text": self.text}
