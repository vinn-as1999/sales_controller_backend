from app import create_app
from os import getenv
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

#env
load_dotenv()
app = create_app()

CORS(app, origins=["https://salescontrollerbr.netlify.app", "http://localhost:5173"])


if __name__ == "__main__":
    app.run(debug=True, port=int(getenv("FLASK_RUN_PORT", 5001)))
