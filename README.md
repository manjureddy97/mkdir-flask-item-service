# Flask Item Service

Small Flask microservice refactoring exercise based on an intentionally flawed snippet.

## Features

- `POST /save`
  - Accepts JSON body with `id` and `text`.
  - Validates input (both must be non-empty strings).
  - Persists data into SQLite using SQLAlchemy.
  - Returns JSON with created/updated item.
  - Uses `201 Created` for new items and `200 OK` for updates.

- `GET /item/<id>`
  - Returns the item in JSON form.
  - Returns `404 Not Found` with a JSON error if missing.

## Design Decisions

1. **SQLite + SQLAlchemy instead of global dict**

   - The original `DATA = {}` was not safe across processes and would lose data on restart.
   - SQLite is a lightweight, file-based database well suited to a small exercise.
   - SQLAlchemy gives a clean ORM and is a realistic production-like persistence layer.

2. **Application Factory**

   - `create_app()` pattern allows easier testing and configuration.
   - Tests use `TestConfig` and an in-memory SQLite database.

3. **Separation of Concerns**

   - `routes.py` handles HTTP specifics only.
   - `services.py` contains business logic and validation.
   - `models.py` defines database models.
   - `errors.py` centralizes error types and JSON error responses.

4. **Error Handling**

   - Custom `APIError`, `ValidationError`, and `NotFoundError`.
   - Global handlers convert both custom and `HTTPException` into consistent JSON responses.

## Requirements

- Python 3.10+ (any modern Python 3 is fine)
- `pip`

## Installation

```bash
git clone <your-repo-url>.git
cd flask-item-service

python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
