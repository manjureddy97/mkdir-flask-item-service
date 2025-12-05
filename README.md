# Flask Item Service

I'm working on a small Flask microservice refactoring exercise based on a code snippet that was intentionally written with design issues.  
I rewrote it to fix the structure and make it behave more like a real-world backend service instead of everything being in one file with a global dictionary.


## Requirements

- Python 3.10+ 
- `pip`

# Clone the repository
git clone git@github.com:manjureddy97/mkdir-flask-item-service.git
cd flask-item-service

# Create a virtual environment
python -m venv .venv

# Activate the environment

# macOS / Linux
source .venv/bin/activate

# Windows
 .venv\Scripts\activate


# Install dependencies
pip install -r requirements.txt

# Start the service
python run.py


### POST /save
- Takes a JSON body with `id` and `text`
- I added simple validation to make sure both values are present and not empty
- Saves the item into an SQLite database through SQLAlchemy — if the item already exists, it updates it; if not, it creates a new one
- Returns the saved item back in JSON format
- Status codes used:
  - **201** for a new item
  - **200** when updating an existing one

Example response:

{
  "item": {
    "id": "item1",
    "text": "Hello from curl"
  },
  "status": "ok"
}


# GET /item/<id>
Fetches an item by its ID and returns it as JSON
If the item is not found, returns 404 with an error message
Example responses:

{
  "id": "item1",
  "text": "Hello from curl"
}


