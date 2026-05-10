from app import db

class Room(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), nullable=False)
    room_type_id = db.Column(db.Integer, db.ForeignKey('room_types.id'), nullable=False)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    # Relationships
    bookings = db.relationship('Booking', backref='room', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Room {self.room_number}>'
