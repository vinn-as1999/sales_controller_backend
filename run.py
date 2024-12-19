from app import create_app
from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()
app = create_app()

CORS(app, resources={r"/*": {"origins": ["https://salescontrollerbr.netlify.app", "https://salescontrollerbr.netlify./shopping", "http://localhost:5173", "http://localhost:5173/shopping"]}})


if __name__ == "__main__":
    app.run(debug=True, port=int(getenv("FLASK_RUN_PORT", 5001)))
