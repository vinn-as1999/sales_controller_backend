from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app, g
from ..middlewares.token_middleware import generate_token


class User:
    @staticmethod
    def create(data):
        if not data.get("name") or not data.get("email") or not data.get("password"):
            return {
                "error": "Campos não preenchidos"
            }, 400
        
        existing_users = g.db["users"].find_one({"email": data.get("email")})
        if existing_users:
            return {
                "error": "Email já cadastrado"
            }, 400
        
        hashed_password = generate_password_hash(data.get("password"))

        new_user = {
            "name": data.get("name"),
            "email": data.get("email"),
            "password": hashed_password
        }
        try:
            g.db["users"].insert_one(new_user)
            print('Usuário criado')
            return {
                "message": "User successfully registered!",
                "name": data.get("name")
            }, 201
        except Exception as error:
            print('erro ao criar usuário')
            return {
                "message": "Network error occurred",
                "error": str(error)
            }, 500

    @staticmethod
    def login(data):
        existing_user = g.db["users"].find_one({"email": data.get("email")})

        if not existing_user:
            return {"error": "Email não encontrado"}, 404
        
        hashed_password = existing_user["password"]
        password = check_password_hash(hashed_password, data.get("password"))

        if not password:
            return {"error": "Senha incorreta"}, 401
        try:
            user_id = str(existing_user["_id"])
            token = generate_token(user_id)

            return {
                "message": "Login bem sucedido!",
                "id": user_id,
                "name": existing_user["name"],
                "token": token
            }, 200
        except Exception as error:
            return {
                "message": "Some error occured",
                "error": error
            }
        
    
    @staticmethod
    def set_user_goal(data):
        try:
            user_id = ObjectId(data["user_id"]) if isinstance(data["user_id"], str) else data["user_id"]
            user = g.db["users"].find_one({"_id": user_id})
            if user:
                g.db["users"].update_one(
                    {"_id": user_id},
                    {"$set": {
                        "goal": data["goal"]
                    }}
                )

                return {
                    "Success": "Projeção mensal atualizada com sucesso!"
                }
            
            else:
                return {
                    "error": "Usuário não encontrado"
                }
        
        except Exception as error:
            print("Error: ", str(error))
            return {
                "error": str(error)
            }
    

    @staticmethod
    def get_all():
        try:
            result = g.db["users"].find()
            users = list(result)
            for user in users:
                user["_id"] = str(user["_id"])

            return users
        
        except Exception as error:
            return {
                "message": "Network error occurred",
                "error": str(error)
            }, 500
        
    