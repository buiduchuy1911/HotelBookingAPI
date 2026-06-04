from flask import request, jsonify
from app import db
from app.models.review import Review
from app.models.booking import Booking
from app.schemas.review_schema import ReviewSchema, CreateReviewSchema
from flask_jwt_extended import get_jwt_identity
from marshmallow import ValidationError

review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

def create_review(hotel_id):
    user_id = get_jwt_identity()
    try:
        data = CreateReviewSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user has a booking at this hotel
    has_booked = Booking.query.join(Booking.room).filter(
        Booking.user_id == user_id,
        Booking.room.has(hotel_id=hotel_id)
    ).first()

    if not has_booked:
        return jsonify({"message": "You can only review hotels you have booked."}), 403

    new_review = Review(
        user_id=user_id,
        hotel_id=hotel_id,
        rating=data['rating'],
        comment=data.get('comment')
    )

    db.session.add(new_review)
    db.session.commit()

    return jsonify(review_schema.dump(new_review)), 201

def get_reviews(hotel_id):
    reviews = Review.query.filter_by(hotel_id=hotel_id).all()
    
    # Calculate average rating
    total_rating = sum(r.rating for r in reviews)
    avg_rating = (total_rating / len(reviews)) if reviews else 0

    return jsonify({
        "average_rating": round(avg_rating, 1),
        "total_reviews": len(reviews),
        "reviews": reviews_schema.dump(reviews)
    }), 200

def delete_review(review_id):
    from app.models.user import User
    
    user_id = int(get_jwt_identity())
    user = User.query.get(user_id)
    review = Review.query.get(review_id)
    
    if not review:
        return jsonify({"message": "Review not found."}), 404
        
    if review.user_id != user_id and user.role != 'admin':
        return jsonify({"message": "You do not have permission to delete this review."}), 403
        
    db.session.delete(review)
    db.session.commit()
    return jsonify({"message": "Review deleted successfully."}), 200
