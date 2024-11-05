from flask import Blueprint, jsonify, request
from ..models.user_models import User


user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users', methods=['GET'])
def get_users():
    result = User.get_all()
    if "error" in result:
        return jsonify(result), result.get("status", 400)
    
    return jsonify(result), 200


@user_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"})
    
    result = User.create(data)
    if "error" in result:
        return jsonify(result), result.get("status", 400)
    
    return jsonify(result), 201


@user_bp.route('/api/login', methods=['POST'])
def log_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"})
    
    try:
        result = User.login(data)
        return jsonify(result), 200
    
    except Exception as error:
        return jsonify({
            "message": "Error",
            "error": error
        }), 400
