from flask import g
from bson.objectid import ObjectId

class Sales:
    @staticmethod
    def get(user_id):
        if not user_id:
            return {"error": "ID inválido ou não fornecido"}
        
        try:
            existing_data = g.db["sales"].find({"user_id": user_id})
            existing_history = g.db["history"].find({"user_id": user_id})
            data_list = list(existing_data)
            history_list = list(existing_history)

            for doc in data_list:
                doc["_id"] = str(doc["_id"])
            for doc in history_list:
                doc["_id"] = str(doc["_id"])

            return {
                "message": "Programa executado com sucesso",
                "sales": data_list,
                "history": history_list
            }

        except Exception as e:
            print("trycatch error, /salesmodel/get")
            return {"error": str(e)}


    @staticmethod
    def insert(data):
        from ..routes.sales_routes import validation
        checked_data = validation(data)
        if not checked_data:
            print('Dados errados: ', checked_data)
            return { "error": "Dado não fornecido ou inválido" }, 400
        
        user_id = data.get("user_id")
        username = data.get("username")
        client = data.get("client")
        product = data.get("product")
        price = data.get("price")
        quantity = data.get("quantity")
        day = data.get("day")
        hour = data.get("hour")
        status = data.get("status")

        sale_obj = {
            "user_id": user_id,
            "username": username,
            "client": client,
            "product": product,
            "price": price,
            "quantity": quantity,
            "day": day,
            "hour": hour,
            "status": status
        }

        try:
            if status == "pending":
                g.db["sales"].insert_one(sale_obj)

            g.db["history"].insert_one(sale_obj)

            return {
                "message": "Sale successfully registered"
            }

        except Exception as e:
            return {"error": str(e)}
        

    @staticmethod
    def delete(sale_id):
        if not sale_id:
            return {"error": "Dado não fornecido ou inválido"}
        
        try:
            g.db["sales"].delete_one({"_id": ObjectId(sale_id)})
            att_data = g.db["sales"].find()
            att_data_list = list(att_data)

            for doc in att_data_list:
                doc["_id"] = str(doc["_id"])

            return att_data_list
        
        except Exception as error:
            return {"error": str(error)}

        