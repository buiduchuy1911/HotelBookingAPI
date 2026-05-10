from flask import request, jsonify
from app import db
from app.models.hotel import Hotel
from app.schemas.hotel_schema import HotelSchema
from marshmallow import ValidationError

hotel_schema = HotelSchema()
hotels_schema = HotelSchema(many=True)

def get_hotels():
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Filtering
    name = request.args.get('name', '')
    address = request.args.get('address', '')
    star_rating = request.args.get('star_rating', type=int)

    query = Hotel.query

    if name:
        query = query.filter(Hotel.name.ilike(f'%{name}%'))
    if address:
        query = query.filter(Hotel.address.ilike(f'%{address}%'))
    if star_rating:
        query = query.filter(Hotel.star_rating == star_rating)

    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    hotels = pagination.items

    return jsonify({
        "hotels": hotels_schema.dump(hotels),
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page
    }), 200

def get_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    return jsonify(hotel_schema.dump(hotel)), 200

def create_hotel():
    try:
        data = hotel_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_hotel = Hotel(
        name=data['name'],
        address=data['address'],
        description=data.get('description'),
        star_rating=data.get('star_rating')
    )
    db.session.add(new_hotel)
    db.session.commit()

    return jsonify(hotel_schema.dump(new_hotel)), 201

def update_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    data = request.json

    if 'name' in data:
        hotel.name = data['name']
    if 'address' in data:
        hotel.address = data['address']
    if 'description' in data:
        hotel.description = data['description']
    if 'star_rating' in data:
        hotel.star_rating = data['star_rating']

    db.session.commit()
    return jsonify(hotel_schema.dump(hotel)), 200

def delete_hotel(hotel_id):
    hotel = Hotel.query.get_or_404(hotel_id)
    db.session.delete(hotel)
    db.session.commit()
    return jsonify({"message": "Hotel deleted successfully"}), 200
