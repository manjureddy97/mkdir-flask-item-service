from typing import Optional

from flask import jsonify, Flask
from werkzeug.exceptions import HTTPException


class APIError(Exception):
    status_code = 400
    error = "bad_request"

    def __init__(
        self,
        message: str,
        status_code: Optional[int] = None,
        error: Optional[str] = None,
    ):
        super().__init__(message)
        if status_code is not None:
            self.status_code = status_code
        if error is not None:
            self.error = error
        self.message = message

    def to_response(self):
        return jsonify(
            {
                "error": self.error,
                "message": self.message,
            }
        ), self.status_code


class ValidationError(APIError):
    def __init__(self, message: str):
        super().__init__(message, status_code=400, error="validation_error")


class NotFoundError(APIError):
    def __init__(self, message: str):
        super().__init__(message, status_code=404, error="not_found")


def register_error_handlers(app: Flask) -> None:
    @app.errorhandler(APIError)
    def handle_api_error(exc: APIError):
        return exc.to_response()

    @app.errorhandler(HTTPException)
    def handle_http_exception(exc: HTTPException):
        response = jsonify(
            {
                "error": exc.name.replace(" ", "_").lower(),
                "message": exc.description,
            }
        )
        return response, exc.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(exc: Exception):
        # In a real app we'd log the exception here
        response = jsonify(
            {
                "error": "internal_server_error",
                "message": "An unexpected error occurred.",
            }
        )
        return response, 500
