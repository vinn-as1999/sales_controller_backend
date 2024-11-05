from flask import Blueprint, jsonify, request
from ..models.products_models import Products

products_bp = Blueprint('product', __name__)

@products_bp.route('/api/products', methods=["GET"])
def get_products():
    # get all products
    pass

@products_bp.route('/api/products', methods=["POST"])
def insert_products():
    # insert products
    pass