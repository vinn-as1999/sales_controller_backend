from flask import Blueprint, jsonify, request
from ..models.products_models import Products

product_bp = Blueprint('product', __name__)

@product_bp.route('/api/products', method=["GET"])
def get_products():
    pass