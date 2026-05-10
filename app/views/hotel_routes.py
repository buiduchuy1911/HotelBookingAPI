from flask import Blueprint
from app.controllers.hotel_controller import get_hotels, get_hotel, create_hotel, update_hotel, delete_hotel
from app.utils.decorators import role_required

hotel_bp = Blueprint('hotel_bp', __name__)

@hotel_bp.route('', methods=['GET'])
def get_hotels_route():
    """
    Get list of hotels
    ---
    tags:
      - Hotels
    parameters:
      - in: query
        name: page
        type: integer
        default: 1
      - in: query
        name: per_page
        type: integer
        default: 10
      - in: query
        name: name
        type: string
      - in: query
        name: address
        type: string
      - in: query
        name: star_rating
        type: integer
    responses:
      200:
        description: List of hotels
    """
    return get_hotels()

@hotel_bp.route('/<int:hotel_id>', methods=['GET'])
def get_hotel_route(hotel_id):
    """
    Get hotel details
    ---
    tags:
      - Hotels
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
    responses:
      200:
        description: Hotel details
      404:
        description: Hotel not found
    """
    return get_hotel(hotel_id)

@hotel_bp.route('', methods=['POST'])
@role_required('admin')
def create_hotel_route():
    """
    Create a new hotel (Admin only)
    ---
    tags:
      - Hotels
    security:
      - Bearer: []
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
            description:
              type: string
            star_rating:
              type: integer
    responses:
      201:
        description: Hotel created
      403:
        description: Unauthorized
    """
    return create_hotel()

@hotel_bp.route('/<int:hotel_id>', methods=['PUT'])
@role_required('admin')
def update_hotel_route(hotel_id):
    """
    Update a hotel (Admin only)
    ---
    tags:
      - Hotels
    security:
      - Bearer: []
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            address:
              type: string
            description:
              type: string
            star_rating:
              type: integer
    responses:
      200:
        description: Hotel updated
    """
    return update_hotel(hotel_id)

@hotel_bp.route('/<int:hotel_id>', methods=['DELETE'])
@role_required('admin')
def delete_hotel_route(hotel_id):
    """
    Delete a hotel (Admin only)
    ---
    tags:
      - Hotels
    security:
      - Bearer: []
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
    responses:
      200:
        description: Hotel deleted
    """
    return delete_hotel(hotel_id)
