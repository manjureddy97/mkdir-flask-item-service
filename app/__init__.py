from typing import Type

from flask import Flask
from .config import Config
from .extensions import db
from .routes import items_bp
from .errors import register_error_handlers


def create_app(config_object: Type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Init extensions
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(items_bp)

    # Register global error handlers
    register_error_handlers(app)

    # Create tables (for this exercise; in real life use migrations)
    with app.app_context():
        from .models import Item  # noqa: F401
        db.create_all()

    return app
