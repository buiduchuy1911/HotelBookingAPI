from flask import request, jsonify
from app import db
from app.models.amenity import Amenity, HotelAmenity
from app.models.hotel import Hotel
from app.schemas.hotel_schema import AmenitySchema
from marshmallow import ValidationError

amenity_schema = AmenitySchema()
amenities_schema = AmenitySchema(many=True)

def get_amenities():
    amenities = Amenity.query.all()
    return jsonify(amenities_schema.dump(amenities)), 200

def create_amenity():
    try:
        data = amenity_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if Amenity.query.filter_by(name=data['name']).first():
        return jsonify({"message": "Amenity already exists"}), 400

    new_amenity = Amenity(**data)
    db.session.add(new_amenity)
    db.session.commit()
    return jsonify(amenity_schema.dump(new_amenity)), 201

def add_amenity_to_hotel(hotel_id, amenity_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    amenity = Amenity.query.get_or_404(amenity_id)

    if HotelAmenity.query.filter_by(hotel_id=hotel_id, amenity_id=amenity_id).first():
        return jsonify({"message": "Hotel already has this amenity"}), 400

    hotel_amenity = HotelAmenity(hotel_id=hotel_id, amenity_id=amenity_id)
    db.session.add(hotel_amenity)
    db.session.commit()

    return jsonify({"message": f"Added {amenity.name} to {hotel.name}"}), 201
