from flask import Blueprint, jsonify, request
from ..models.inventory_models import Inventory

inventory_bp = Blueprint('Inventory', __name__)

FALSY_DATA_ERROR = 'Dados inválidos! Insira dados válidos'
NO_DATA_ERROR = 'Dados inexistentes! Preencha os campos'
SUCESS_MESSAGE = 'Programa executado com sucesso!'

@inventory_bp.route('/api/inventory/<string:user_id>', methods=["GET"])
def get_inventory(user_id):
    if not user_id:
        print('Erro no get inventory')
        return jsonify({"error": NO_DATA_ERROR})
    
    response = Inventory.get(user_id)
    if "error" in response:
        print("Erro no response do get inventory: ", response["error"])
        return jsonify(response), response.get("status", 400)
    
    return jsonify(response), 200


@inventory_bp.route('/api/inventory', methods=["POST"])
def insert_inventory():
    data = request.get_json()
    if not data:
        print('Erro no insert')
        return jsonify({"error": NO_DATA_ERROR})
    
    response = Inventory.insert(data)
    if "error" in response:
        print("error no response do insert", response["error"])
        return jsonify(response), response.get("status", 400)
    
    return jsonify(response), 201


@inventory_bp.route('/api/inventory', methods=["PATCH"])
def update_inventory():
    pass


@inventory_bp.route('/api/inventory', methods=["DELETE"])
def delete_inventory():
    pass