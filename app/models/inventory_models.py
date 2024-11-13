from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import g


class Inventory:
    FALSY_DATA_ERROR = 'Dados inválidos! Insira dados válidos'
    NO_DATA_ERROR = 'Dados inexistentes! Preencha os campos'
    SUCESS_MESSAGE = 'Programa executado com sucesso!'

    @staticmethod
    def validation(data):
        if not data.get("user_id") or not data.get("username") or not data.get("inventory"):
            print([
                data.get("user_id"),
                data.get("username"),
                data.get("inventory")
            ])
            return { "error": Inventory.NO_DATA_ERROR }
        else:
            return data

    @staticmethod
    def insert(data):
        existing_data = Inventory.validation(data)
        print('o data do insert models', data)

        if "error" in existing_data:
            return existing_data, 400
        
        filt = {
            "user_id": data.get("user_id"),
            "username": data.get("username"),
        }

        try:
            for key, value in data.get("inventory").items():
                if value is not None:
                    g.db["inventories"].update_one(
                        filt,
                        {
                            "$set": {
                                f"inventory.{key}": value
                            }
                        },
                        upsert=True
                    )

            return {
                "message": Inventory.SUCESS_MESSAGE
            }

        except Exception as error:
            print("caiu aqui")
            return {
                "error": str(error)
            }

    @staticmethod
    def update(data):
        existing_data = Inventory.validation(data)

    @staticmethod
    def delete(data):
        existing_data = Inventory.validation(data)

    @staticmethod
    def get(data):
        existing_data = Inventory.validation(data)