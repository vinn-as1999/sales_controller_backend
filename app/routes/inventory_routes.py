from flask import Blueprint, jsonify, request
from ..models.inventory_models import Inventory

inventory_bp = Blueprint('Inventory', __name__)

FALSY_DATA_ERROR = 'Dados inválidos! Insira dados válidos'
NO_DATA_ERROR = 'Dados inexistentes! Preencha os campos'
SUCESS_MESSAGE = 'Programa executado com sucesso!'

@inventory_bp.route('/api/inventory', methods=['GET'])
def get_inventory():
    pass