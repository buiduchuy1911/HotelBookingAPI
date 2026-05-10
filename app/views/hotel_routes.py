from flask import Blueprint
from app.controllers.hotel_controller import get_hotels, get_hotel, create_hotel, update_hotel, delete_hotel
from app.utils.decorators import role_required

hotel_bp = Blueprint('hotel_bp', __name__)

# Guest routes (public)
hotel_bp.route('', methods=['GET'])(get_hotels)
hotel_bp.route('/<int:hotel_id>', methods=['GET'])(get_hotel)

# Admin routes
hotel_bp.route('', methods=['POST'])(role_required('admin')(create_hotel))
hotel_bp.route('/<int:hotel_id>', methods=['PUT'])(role_required('admin')(update_hotel))
hotel_bp.route('/<int:hotel_id>', methods=['DELETE'])(role_required('admin')(delete_hotel))
