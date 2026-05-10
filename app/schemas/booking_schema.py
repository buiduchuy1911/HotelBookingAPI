from app import ma
from app.models.booking import Booking
from marshmallow import fields

class BookingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Booking
        load_instance = True
        include_fk = True

class CreateBookingSchema(ma.Schema):
    room_id = fields.Integer(required=True)
    check_in_date = fields.Date(required=True)
    check_out_date = fields.Date(required=True)
