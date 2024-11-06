from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g

class Products:
    TRY_EXCEPT_ERROR = "Erro ao executar programa"
    NO_DATA_ERROR = "Campos vazios! Insira dados válidos!"
    EXISTING_DATA_ERROR = "Dados já existentes"
    DATA_SUCCESS_MESSAGE = "Programa executado com sucesso!"

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
        # verifica se o produto existe no banco de dados
        existing_product = g.db["products"].find_one({
            "category": data.get("category"), 
            "products": {
                "$elemMatch": {
                    "name": data.get("product")
                }
            }
        })
        # se o produto existir, atualiza a quantidade de produtos
        if existing_product:
            g.db["products"].update_one({
                "category": data.get("category"),
                "products.name": data.get("product")
                },
                {"$inc": {
                    "products.$.quantity": int(data.get("quantity"))
                }
            })
        # se não, adiciona um novo produto
        else:
            try:
                g.db["products"].update_one({
                    "user_id": data.get("user_id"),
                    "username": data.get("username"),
                    "category": data.get("category")
                }, {"$push": {
                    "products": {
                        "name": data.get("product"),
                        "price": float(data.get("price").replace(',', '.')),
                        "quantity": int(data.get("quantity"))
                    }
                }}, upsert=True)

                return {
                    "success": Products.DATA_SUCCESS_MESSAGE
                }
            except Exception as error:
                return {
                    "message": Products.TRY_EXCEPT_ERROR,
                    "error": str(error)
                }


    @staticmethod
    def update():
        # update products
        pass

    @staticmethod
    def delete(data):
        if not data.get("user_id") or not data.get("username") or not data.get("category") or not data.get("product"):
            return {
                "error": Products.NO_DATA_ERROR
            }
        
        try:
            g.db["products"].update_one(
                {
                    "user_id": data.get("user_id"),
                    "username": data.get("username"),
                    "category": data.get("category")
                },
                {
                    "$pull": {
                        "products": {"name": data.get("product")}
                    }
                }
            )

            return {
                "success": Products.DATA_SUCCESS_MESSAGE
            }

        except Exception as error:
            return {
                "message": Products.TRY_EXCEPT_ERROR,
                "error": str(error)
            }