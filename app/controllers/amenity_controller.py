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
        new_amenity = amenity_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    if Amenity.query.filter_by(name=new_amenity.name).first():
        return jsonify({"message": "Amenity already exists"}), 400

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

def delete_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        return jsonify({"message": "Amenity not found"}), 404
        
    db.session.delete(amenity)
    db.session.commit()
    return jsonify({"message": "Amenity deleted successfully"}), 200

def remove_amenity_from_hotel(hotel_id, amenity_id):
    hotel_amenity = HotelAmenity.query.filter_by(hotel_id=hotel_id, amenity_id=amenity_id).first()
    
    if not hotel_amenity:
        return jsonify({"message": "Hotel does not have this amenity"}), 404
        
    db.session.delete(hotel_amenity)
    db.session.commit()
    return jsonify({"message": "Amenity removed from hotel"}), 200
