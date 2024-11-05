from flask import Blueprint, jsonify, request
from ..models.clients_model import Clients

clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/api/clients', methods=['GET'])
def get_clients():
    pass

@clients_bp.route('/api/add_clients', methods=['POST'])
def insert_clients():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data not provided"}), 400
    
    try:
        result = Clients.insert(data)
        return jsonify(result), 201

    except Exception as error:
        print('Error inserting clients', error)
        return jsonify({
            "message": "Error trying insert new clients",
            "error": error
        }), 400