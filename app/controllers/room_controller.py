from flask import request, jsonify
from app import db
from app.models.room import Room
from app.models.room_type import RoomType
from app.models.booking import Booking
from app.schemas.hotel_schema import RoomSchema, RoomTypeSchema
from marshmallow import ValidationError
from datetime import datetime

room_schema = RoomSchema()
rooms_schema = RoomSchema(many=True)
room_type_schema = RoomTypeSchema()
room_types_schema = RoomTypeSchema(many=True)

# --- Room Types ---
def get_room_types():
    room_types = RoomType.query.all()
    return jsonify(room_types_schema.dump(room_types)), 200

def create_room_type():
    try:
        data = room_type_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    new_room_type = RoomType(**data)
    db.session.add(new_room_type)
    db.session.commit()
    return jsonify(room_type_schema.dump(new_room_type)), 201

# --- Rooms ---
def get_rooms():
    rooms = Room.query.all()
    return jsonify(rooms_schema.dump(rooms)), 200

def create_room():
    try:
        data = room_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Check if room_number exists in hotel
    if Room.query.filter_by(room_number=data['room_number'], hotel_id=data['hotel_id']).first():
        return jsonify({"message": "Room number already exists in this hotel"}), 400

    new_room = Room(**data)
    db.session.add(new_room)
    db.session.commit()
    return jsonify(room_schema.dump(new_room)), 201

# --- Availability Logic ---
def get_available_rooms():
    check_in_str = request.args.get('check_in')
    check_out_str = request.args.get('check_out')
    hotel_id = request.args.get('hotel_id', type=int)

    if not check_in_str or not check_out_str or not hotel_id:
        return jsonify({"message": "check_in, check_out, and hotel_id are required"}), 400

    try:
        check_in = datetime.strptime(check_in_str, '%Y-%m-%d').date()
        check_out = datetime.strptime(check_out_str, '%Y-%m-%d').date()
    except ValueError:
        return jsonify({"message": "Dates must be in YYYY-MM-DD format"}), 400

    if check_in >= check_out:
        return jsonify({"message": "check_out must be after check_in"}), 400

    # Find conflicting bookings
    conflicting_bookings = db.session.query(Booking.room_id).filter(
        Booking.status != 'cancelled',
        Booking.check_in_date < check_out,
        Booking.check_out_date > check_in
    ).subquery()

    # Find available rooms
    available_rooms = Room.query.filter(
        Room.hotel_id == hotel_id,
        Room.is_available == True,
        ~Room.id.in_(conflicting_bookings)
    ).all()

    return jsonify(rooms_schema.dump(available_rooms)), 200
