from flask import g

class Sales:
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

        try:
            g.db["sales"].insert_one({
                "user_id": user_id,
                "username": username,
                "client": client,
                "product": product,
                "price": price,
                "quantity": quantity,
                "day": day,
                "hour": hour,
                "status": status
            })

            return {
                "message": "Sale successfully registered"
            }

        except Exception as e:
            return {"error": str(e)}
        
        