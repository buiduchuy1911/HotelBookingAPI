from flask import Blueprint
from app.controllers.review_controller import create_review, get_reviews
from flask_jwt_extended import jwt_required

review_bp = Blueprint('review_bp', __name__)

review_bp.route('/hotels/<int:hotel_id>/reviews', methods=['POST'])(jwt_required()(create_review))
review_bp.route('/hotels/<int:hotel_id>/reviews', methods=['GET'])(get_reviews)
