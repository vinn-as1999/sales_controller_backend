from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g

class Products:
    NO_DATA_ERROR = "Campos vazios! Insira dados válidos!"
    EXISTING_DATA_ERROR = "Dados já existentes"
    DATA_SUCCESS_MESSAGE = "Dados inseridos com sucesso!"

    @staticmethod
    def get():
        # get all products
        pass

    @staticmethod
    def insert(data):
        # insert products 
        if not data.get("user_id") or not data.get("username") or not data.get("category") or not data.get("product"):
            return {
                "error": Products.NO_DATA_ERROR
            }
        
        existing_product = g.db["products"].find_one({
            "category": data.get("category"), 
            "products": {
                "$elemMatch": {
                    "name": data.get("product")
                }
            }
        })

        if existing_product:
            g.db["products"].update_one({
                "category": data.get("category"),
                "products.name": data.get("product")
                },
                {"$inc": {
                    "products.$.quantity": data.get("quantity")
                }
            })

        else:
            g.db["products"].update_one({
                "user_id": data.get("user_id"),
                "username": data.get("username"),
                "category": data.get("category")
            }, {"$push": {
                "products": {
                    "name": data.get("product"),
                    "price": data.get("price"),
                    "quantity": data.get("quantity")
                }
            }}, upsert=True)

            return {
                "success": Products.DATA_SUCCESS_MESSAGE
            }


    @staticmethod
    def update():
        # update products
        pass

    @staticmethod
    def delete():
        # delete products
        pass