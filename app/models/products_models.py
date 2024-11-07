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
        
        product = data["product"]
        # verifica se o produto existe no banco de dados
        existing_product = g.db["products"].find_one({
            "category": data.get("category"), 
            "products": {
                "$elemMatch": {
                    "name": product["name"]
                }
            }
        })
        # se o produto existir, atualiza a quantidade de produtos
        if existing_product:
            g.db["products"].update_one({
                "category": data.get("category"),
                "products.name": product["name"]
                },
                {"$inc": {
                    "products.$.quantity": int(product["quantity"])
                }
            })

            return {
                    "success": Products.DATA_SUCCESS_MESSAGE
                }
        # se não, adiciona um novo produto
        else:
            try:
                g.db["products"].update_one({
                    "user_id": data.get("user_id"),
                    "username": data.get("username"),
                    "category": data.get("category")
                }, {"$push": {
                    "products": {
                        "name": product["name"],
                        "price": float(product["price"]),
                        "quantity": int(product["quantity"])
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
        
        product = data["product"]
        filt = {
            "user_id": data.get("user_id"),
            "username": data.get("username"),
            "category": data.get("category"),
            "products.name": product["name"]
        }

        if product["deleteOne"]:
            try:
                g.db["products"].update_one(
                    filt,
                    {
                        "$inc": {
                            "products.$.quantity": -int(product["quantity"])
                        }
                    }
                )

                updated_product = g.db["products"].find_one(filt, {"products.$": 1})

                print('o updated ', updated_product)

                if updated_product and updated_product["products"][0]["quantity"] <= 0:
                    print('é menor que zero')
                    g.db["products"].update_one(
                        filt,
                        {
                            "$pull": {
                                "products": {"name": product["name"]}
                            }
                        }
                    )

                    return {
                        "sucess": Products.DATA_SUCCESS_MESSAGE,
                        "message": f"Produto {product['name']} removido"
                    }

                return {
                    "success": Products.DATA_SUCCESS_MESSAGE
                }
            
            except Exception as error:
                print(error)
                return {
                    "error": str(error)
                }

        try:
            g.db["products"].update_one(
                filt,
                {
                    "$pull": {
                        "products": {"name": product["name"]}
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