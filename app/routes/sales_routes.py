from flask import Blueprint, jsonify, request
from ..models.sales_models import Sales

sales_bp = Blueprint('sales', __name__)
NO_DATA_ERROR = "Dados não fornecidos"
FALSY_DATA_ERROR = "Dados inválidos ou ausentes"


def validation(data):
    if not data:
        return { "error": NO_DATA_ERROR }
    
    user_id = data.get("user_id")
    username = data.get("username")
    client = data.get("client")
    product = data.get("product")
    price = data.get("price")
    quantity = data.get("quantity")
    day = data.get("day")
    hour = data.get("hour")
    status = data.get("status")

    if any(not value for value in [user_id, username, client, product, price, quantity, day, hour, status]):
        print("caiu no validation: ", data)
        return { "error": FALSY_DATA_ERROR }
    
    return data

    
@sales_bp.route('/api/sales', methods=['POST'])
def insert_sales():
    data = request.get_json()
    checked_data = validation(data)
    if not checked_data:
        return jsonify({"error": NO_DATA_ERROR}), 400
    if "error" in checked_data:
        print("caiu aqui")
        return jsonify({"error": FALSY_DATA_ERROR}), 400
    
    response = Sales.insert(data)
    if "error" in response:
        return jsonify(response), response.get("status")
    
    return jsonify(response), 201


@sales_bp.route('/api/sales/<string:user_id>', methods=['GET'])
def get_sales(user_id):
    pass