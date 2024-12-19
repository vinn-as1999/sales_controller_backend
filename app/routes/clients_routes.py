from flask import Blueprint, jsonify, request
from ..models.clients_models import Clients

clients_bp = Blueprint('clients', __name__)


@clients_bp.route('/api/clients/<string:user_id>', methods=['GET'])
def get_clients(user_id):
    if not user_id:
        return jsonify({"error": "Data not provided"}), 400
    
    result = Clients.get(user_id)
    if "error" in result:
        return jsonify(result), 400

    return jsonify(result), 200


@clients_bp.route('/api/add_clients', methods=['POST'])
def insert_clients():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not provided"}), 400
    
    try:
        result = Clients.insert(data)
        if "error" in result:
            return jsonify(result), 400
        
        return jsonify(result), 201

    except Exception as error:
        print('Error inserting clients', error)
        return jsonify({
            "message": "Error trying insert new clients",
            "error": error
        }), 400