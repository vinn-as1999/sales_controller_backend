from flask import Blueprint, jsonify, request
from ..models.products_models import Products

products_bp = Blueprint('product', __name__)

NO_DATA_PROVIDED = "Dados não fornecidos"

@products_bp.route('/api/products', methods=["GET"])
def get_products():
    # get all products
    data = request.args.get("user_id")
    if not data:
        return jsonify({"error": NO_DATA_PROVIDED})
    
    result = Products.get(data)
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result), 200
    

@products_bp.route('/api/products', methods=["POST"])
def insert_products():
    # insert products
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados não fornecidos"})
    
    result = Products.insert(data)
    if "error" in result:
        return jsonify(result), result.get("status", 400)
    
    return jsonify(result), 201


@products_bp.route('/api/products', methods=["DELETE"])
def delete_products():
    data = request.get_json()
    if not data:
        return jsonify({"error": NO_DATA_PROVIDED})
    
    result = Products.delete(data)
    if "error" in result:
        return jsonify(result), 400
    
    return jsonify(result), 200

