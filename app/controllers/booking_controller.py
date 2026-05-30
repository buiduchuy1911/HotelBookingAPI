from flask import request, jsonify
from app import db
from app.models.booking import Booking
from app.models.room import Room
from app.schemas.booking_schema import BookingSchema, CreateBookingSchema
from flask_jwt_extended import get_jwt_identity, get_jwt
from marshmallow import ValidationError

booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)

def create_booking():
    user_id = get_jwt_identity()
    try:
        data = CreateBookingSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    room_id = data['room_id']
    check_in = data['check_in_date']
    check_out = data['check_out_date']

    if check_in >= check_out:
        return jsonify({"message": "check_out must be after check_in"}), 400

    room = Room.query.get_or_404(room_id)
    if not room.is_available:
        return jsonify({"message": "Room is not available"}), 400

    # Check for conflicting bookings
    conflict = Booking.query.filter(
        Booking.room_id == room_id,
        Booking.status != 'cancelled',
        Booking.check_in_date < check_out,
        Booking.check_out_date > check_in
    ).first()

    if conflict:
        return jsonify({"message": "Room is already booked for these dates"}), 400

    # Calculate total price
    nights = (check_out - check_in).days
    total_price = room.room_type.base_price * nights

    new_booking = Booking(
        user_id=user_id,
        room_id=room_id,
        check_in_date=check_in,
        check_out_date=check_out,
        total_price=total_price,
        status='confirmed'
    )

    db.session.add(new_booking)
    db.session.commit()

    return jsonify(booking_schema.dump(new_booking)), 201

def get_user_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify(bookings_schema.dump(bookings)), 200

def get_all_bookings():
    bookings = Booking.query.all()
    return jsonify(bookings_schema.dump(bookings)), 200

def delete_booking(booking_id):
    user_id = get_jwt_identity()
    claims = get_jwt()
    booking = Booking.query.get_or_404(booking_id)

    if str(booking.user_id) != str(user_id) and claims.get("role") != "admin":
        return jsonify({"message": "Unauthorized"}), 403

    booking.status = 'cancelled'
    db.session.commit()
    return jsonify({"message": "Booking cancelled successfully"}), 200
