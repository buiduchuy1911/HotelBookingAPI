from app import ma
from app.models.hotel import Hotel
from app.models.room_type import RoomType
from app.models.room import Room
from app.models.amenity import Amenity
from marshmallow import fields

class AmenitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Amenity
        load_instance = True

class RoomTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RoomType
        load_instance = True

class RoomSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Room
        load_instance = True
    
    room_type = fields.Nested(RoomTypeSchema)

class HotelSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hotel
        load_instance = True
    
    rooms = fields.List(fields.Nested(RoomSchema(only=("id", "room_number", "is_available", "room_type"))))
    # We can also add amenities if we fetch from HotelAmenity, but let's keep it simple for now or custom map it.
