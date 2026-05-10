from flask import Blueprint
from app.controllers.review_controller import create_review, get_reviews
from flask_jwt_extended import jwt_required

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/hotels/<int:hotel_id>/reviews', methods=['POST'])
@jwt_required()
def create_review_route(hotel_id):
    """
    Create a review for a hotel
    ---
    tags:
      - Reviews
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
          required:
            - rating
          properties:
            rating:
              type: integer
              example: 5
            comment:
              type: string
              example: "Great hotel!"
    responses:
      201:
        description: Review created
      403:
        description: Must have booked this hotel to review
    """
    return create_review(hotel_id)

@review_bp.route('/hotels/<int:hotel_id>/reviews', methods=['GET'])
def get_reviews_route(hotel_id):
    """
    Get reviews for a hotel
    ---
    tags:
      - Reviews
    parameters:
      - in: path
        name: hotel_id
        type: integer
        required: true
    responses:
      200:
        description: List of reviews
    """
    return get_reviews(hotel_id)
