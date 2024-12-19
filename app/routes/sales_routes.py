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
        return jsonify({"error": FALSY_DATA_ERROR}), 400
    
    response = Sales.insert(data)
    if "error" in response:
        return jsonify(response), 400
    
    return jsonify(response), 201


@sales_bp.route('/api/sales/<string:sale_id>', methods=['DELETE'])
def delete_sales(sale_id):
    if not sale_id:
        return jsonify({"error": NO_DATA_ERROR}), 400
    
    result = Sales.delete(sale_id)
    if "error" in result:
        return jsonify(result), 404
    
    return jsonify(result), 200
    


@sales_bp.route('/api/sales/<string:user_id>', methods=['GET'])
def get_sales(user_id):
    if not user_id:
        return jsonify({"error": NO_DATA_ERROR}), 400
    
    result = Sales.get(user_id)
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result), 200
    