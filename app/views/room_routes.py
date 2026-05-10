from flask import Blueprint
from app.controllers.room_controller import get_room_types, create_room_type, get_rooms, create_room, get_available_rooms
from app.utils.decorators import role_required

room_bp = Blueprint('room_bp', __name__)

@room_bp.route('/types', methods=['GET'])
def get_room_types_route():
    """
    Get all room types
    ---
    tags:
      - Rooms
    responses:
      200:
        description: List of room types
    """
    return get_room_types()

@room_bp.route('/types', methods=['POST'])
@role_required('admin')
def create_room_type_route():
    """
    Create a new room type (Admin only)
    ---
    tags:
      - Rooms
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - max_occupancy
            - base_price
          properties:
            name:
              type: string
            max_occupancy:
              type: integer
            base_price:
              type: number
            description:
              type: string
    responses:
      201:
        description: Room type created
    """
    return create_room_type()

@room_bp.route('', methods=['GET'])
@role_required('admin')
def get_rooms_route():
    """
    Get all rooms (Admin only)
    ---
    tags:
      - Rooms
    security:
      - Bearer: []
    responses:
      200:
        description: List of all rooms
    """
    return get_rooms()

@room_bp.route('', methods=['POST'])
@role_required('admin')
def create_room_route():
    """
    Create a new room (Admin only)
    ---
    tags:
      - Rooms
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - room_number
            - room_type_id
            - hotel_id
          properties:
            room_number:
              type: string
            room_type_id:
              type: integer
            hotel_id:
              type: integer
            is_available:
              type: boolean
    responses:
      201:
        description: Room created
    """
    return create_room()

@room_bp.route('/availability', methods=['GET'])
def get_available_rooms_route():
    """
    Find available rooms
    ---
    tags:
      - Rooms
    parameters:
      - in: query
        name: hotel_id
        type: integer
        required: true
      - in: query
        name: check_in
        type: string
        format: date
        required: true
        description: YYYY-MM-DD
      - in: query
        name: check_out
        type: string
        format: date
        required: true
        description: YYYY-MM-DD
    responses:
      200:
        description: List of available rooms
    """
    return get_available_rooms()
