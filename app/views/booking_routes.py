from flask import Blueprint
from app.controllers.booking_controller import create_booking, get_user_bookings, delete_booking
from app.utils.decorators import role_required
from flask_jwt_extended import jwt_required

booking_bp = Blueprint('booking_bp', __name__)

booking_bp.route('', methods=['POST'])(jwt_required()(create_booking))
booking_bp.route('/me', methods=['GET'])(jwt_required()(get_user_bookings))
booking_bp.route('/<int:booking_id>', methods=['DELETE'])(jwt_required()(delete_booking))
