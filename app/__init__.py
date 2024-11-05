from flask import Flask, g
from .routes.user_routes import user_bp
from .routes.clients_routes import clients_bp
from .routes.products_routes import products_bp
from pymongo import MongoClient
from config import MONGO_URI

def create_app():
    app = Flask(__name__)

    try:
        # DB INITIALIZATION
        client = MongoClient(MONGO_URI)
        db = client["salles1"]
        print("Conectado ao MongoDB")

    except Exception as error:
        print(f"Erro ao conectar ao MongoDB: {error}")
        print("URI usada para conexão: ", MONGO_URI)

    # ROUTES REGISTER
    app.register_blueprint(user_bp)
    app.register_blueprint(clients_bp)
    app.register_blueprint(products_bp)

    @app.before_request
    def before_request():
        g.db = db

    return app
