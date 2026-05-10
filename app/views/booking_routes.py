from flask import Blueprint
from app.controllers.booking_controller import create_booking, get_user_bookings, delete_booking
from flask_jwt_extended import jwt_required

booking_bp = Blueprint('booking_bp', __name__)

@booking_bp.route('', methods=['POST'])
@jwt_required()
def create_booking_route():
    """
    Create a new booking
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - room_id
            - check_in_date
            - check_out_date
          properties:
            room_id:
              type: integer
            check_in_date:
              type: string
              format: date
              example: "2026-06-15"
            check_out_date:
              type: string
              format: date
              example: "2026-06-20"
    responses:
      201:
        description: Booking created successfully
      400:
        description: Room is not available or validation error
    """
    return create_booking()

@booking_bp.route('/me', methods=['GET'])
@jwt_required()
def get_user_bookings_route():
    """
    Get bookings of current user
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    responses:
      200:
        description: List of bookings
    """
    return get_user_bookings()

@booking_bp.route('/<int:booking_id>', methods=['DELETE'])
@jwt_required()
def delete_booking_route(booking_id):
    """
    Cancel a booking
    ---
    tags:
      - Bookings
    security:
      - Bearer: []
    parameters:
      - in: path
        name: booking_id
        type: integer
        required: true
    responses:
      200:
        description: Booking cancelled
    """
    return delete_booking(booking_id)
