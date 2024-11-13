from flask import Blueprint, jsonify, request
from ..models.inventory_models import Inventory

inventory_bp = Blueprint('Inventory', __name__)

FALSY_DATA_ERROR = 'Dados inválidos! Insira dados válidos'
NO_DATA_ERROR = 'Dados inexistentes! Preencha os campos'
SUCESS_MESSAGE = 'Programa executado com sucesso!'

@inventory_bp.route('/api/inventory/<string:user_id>', methods=["GET"])
def get_inventory(user_id):
    pass

@inventory_bp.route('/api/inventory', methods=["POST"])
def insert_inventory():
    data = request.get_json()
    if not data:
        return jsonify({"error": NO_DATA_ERROR})
    
    response = Inventory.insert(data)
    if "error" in response:
        return jsonify(response), response.get("status", 400)
    
    return jsonify(response), 201

@inventory_bp.route('/api/inventory', methods=["PATCH"])
def update_inventory():
    pass

@inventory_bp.route('/api/inventory', methods=["DELETE"])
def delete_inventory():
    pass