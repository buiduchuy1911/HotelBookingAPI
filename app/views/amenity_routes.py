from flask import Blueprint
from app.controllers.amenity_controller import get_amenities, create_amenity, add_amenity_to_hotel
from app.utils.decorators import role_required

amenity_bp = Blueprint('amenity_bp', __name__)

# Admin routes
amenity_bp.route('', methods=['GET'])(get_amenities)
amenity_bp.route('', methods=['POST'])(role_required('admin')(create_amenity))
amenity_bp.route('/hotel/<int:hotel_id>/<int:amenity_id>', methods=['POST'])(role_required('admin')(add_amenity_to_hotel))
