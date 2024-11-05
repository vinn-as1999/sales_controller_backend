from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g

class Clients:
    @staticmethod
    def insert(data):
        if not data.get("user_id") or not data.get("client") or not data.get("contact") or not data.get("address"):
            return {
                "message": "Dados inválidos ou ausentes"
            }, 400
        
        existing_clients = g.db["clients"].find_one({"contact": data.get("contact")})

        if existing_clients:
            return {
                "message": "Cliente já existente"
            }, 403
        
        new_client = {
            "user_id": data.get("user_id"),
            "client": data.get("client"),
            "contact": data.get("contact"),
            "address": data.get("address"),
            "observations": data.get("observations")
        }
        
        try:
            g.db["clients"].insert_one(new_client)
            return {
                "message": "Cliente inserido com sucesso!",
                "client": data.get("client"),
                "contact": data.get("contact"),
                "address": data.get("address"),
                "observations": data.get("observations")
            }, 201
    
        except Exception as error:
            print("Erro ao inserir cliente")
            return {
                "message": "Erro ao inserir cliente",
                "error": str(error)
            }, 400


    @staticmethod
    def update():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def get():
        pass