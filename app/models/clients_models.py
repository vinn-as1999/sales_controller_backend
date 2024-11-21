from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g

class Clients:
    @staticmethod
    def get(id):
        if not id:
            return {
                "error": "Dado não fornecido"
            }
        
        try:
            clients = g.db["clients"].find({"user_id": id})
            clients_list = list(clients)
            for doc in clients_list:
                doc["_id"] = str(doc["_id"])

            return clients_list
        
        except Exception as error:
            print("trycatch error")
            return {
                "error": str(error)
            }

    @staticmethod
    def insert(data):
        if not data.get("user_id") or not data.get("client") or not data.get("contact") or not data.get("address"):
            return {
                "error": "Dados inválidos ou ausentes"
            }, 400
        
        existing_clients = g.db["clients"].find_one({"contact": data.get("contact")})

        if existing_clients:
            return {
                "error": "Cliente já existente"
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
                "client": new_client
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
