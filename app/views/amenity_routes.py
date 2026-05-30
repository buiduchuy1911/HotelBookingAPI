from flask import Blueprint
from app.controllers.amenity_controller import (
    get_amenities, create_amenity, add_amenity_to_hotel, 
    delete_amenity, remove_amenity_from_hotel
)
from app.utils.decorators import role_required

amenity_bp = Blueprint('amenity_bp', __name__)

@amenity_bp.route('', methods=['GET'])
def get_amenities_route():
    """
    Get all amenities
    ---
    tags:
      - Amenities
    responses:
      200:
        description: List of amenities
    """
    return get_amenities()

@amenity_bp.route('', methods=['POST'])
@role_required('admin')
def create_amenity_route():
    """
    Create a new amenity (Admin only)
    ---
    tags:
      - Amenities
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
              example: "Sauna"
            description:
              type: string
    responses:
      201:
        description: Amenity created
    """
    return create_amenity()

@amenity_bp.route('/hotel/<int:hotel_id>/<int:amenity_id>', methods=['POST'])
@role_required('admin')
def add_amenity_to_hotel_route(hotel_id, amenity_id):
    """
    Add amenity to a hotel (Admin only)
    ---
    tags:
      - Amenities
    security:
      - Bearer: []
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
      - in: path
        name: amenity_id
        type: integer
        required: true
    responses:
      201:
        description: Amenity added to hotel
    """
    return add_amenity_to_hotel(hotel_id, amenity_id)

@amenity_bp.route('/<int:amenity_id>', methods=['DELETE'])
@role_required('admin')
def delete_amenity_route(amenity_id):
    """
    Delete an amenity globally (Admin only)
    ---
    tags:
      - Amenities
    security:
      - Bearer: []
    parameters:
      - in: path
        name: amenity_id
        type: integer
        required: true
    responses:
      200:
        description: Amenity deleted
      404:
        description: Amenity not found
    """
    return delete_amenity(amenity_id)

@amenity_bp.route('/hotel/<int:hotel_id>/<int:amenity_id>', methods=['DELETE'])
@role_required('admin')
def remove_amenity_from_hotel_route(hotel_id, amenity_id):
    """
    Remove an amenity from a hotel (Admin only)
    ---
    tags:
      - Amenities
    security:
      - Bearer: []
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
      - in: path
        name: amenity_id
        type: integer
        required: true
    responses:
      200:
        description: Amenity removed from hotel
      404:
        description: Hotel or Amenity not found
    """
    return remove_amenity_from_hotel(hotel_id, amenity_id)
