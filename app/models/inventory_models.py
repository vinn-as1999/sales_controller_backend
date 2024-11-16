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
    def get(data):
        if not data:
            return { "error": Inventory.NO_DATA_ERROR }
        
        try:
            inv_data = g.db["inventories"].find({"user_id": data})
            inv_list = list(inv_data)
            for c in inv_list:
                c["_id"] = str(c["_id"])

            return inv_list
        
        except Exception as error:
            print('Some error occurred: ', error)
            return {
                "error": str(error)
            }


    @staticmethod
    def insert(data):
        existing_data = Inventory.validation(data)
        print('o data do insert', data)
        if "error" in existing_data:
            return existing_data, 400
        
        filt = {
            "user_id": data.get("user_id"),
            "username": data.get("username"),
        }

        try:
            # Inicializa dicionários para operações de $set e $unset
            set_data = {}
            unset_data = {}

            # Itera sobre as categorias do inventário atualizado
            for key, value in data.get("inventory").items():
                if value:
                    # Se a categoria tem conteúdo, prepare para atualizar ($set)
                    set_data[f"inventory.{key}"] = value
                else:
                    # Se a categoria está vazia, prepare para remover ($unset)
                    unset_data[f"inventory.{key}"] = ""

            # Executa o update com $set se houver dados para atualizar
            if set_data:
                g.db["inventories"].update_one(
                    filt,
                    {
                        "$set": set_data
                    },
                    upsert=True
                )

            # Executa o update com $unset se houver dados para remover
            if unset_data:
                g.db["inventories"].update_one(
                    filt,
                    {
                        "$unset": unset_data
                    }
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
