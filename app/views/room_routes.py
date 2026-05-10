from flask import Blueprint
from app.controllers.room_controller import get_room_types, create_room_type, get_rooms, create_room, get_available_rooms
from app.utils.decorators import role_required

room_bp = Blueprint('room_bp', __name__)

# --- Room Types ---
room_bp.route('/types', methods=['GET'])(get_room_types) # public
room_bp.route('/types', methods=['POST'])(role_required('admin')(create_room_type))

# --- Rooms ---
room_bp.route('', methods=['GET'])(role_required('admin')(get_rooms)) # Admin can see all rooms
room_bp.route('', methods=['POST'])(role_required('admin')(create_room))

# --- Guest Availability Route ---
room_bp.route('/availability', methods=['GET'])(get_available_rooms)
