from datetime import datetime
from app import db

class Hotel(db.Model):
    __tablename__ = 'hotels'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    star_rating = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    rooms = db.relationship('Room', backref='hotel', lazy=True, cascade="all, delete-orphan")
    reviews = db.relationship('Review', backref='hotel', lazy=True, cascade="all, delete-orphan")
    hotel_amenities = db.relationship('HotelAmenity', backref='hotel', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Hotel {self.name}>'
