from app import db

class Amenity(db.Model):
    __tablename__ = 'amenities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    # Relationships
    hotel_amenities = db.relationship('HotelAmenity', backref='amenity', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Amenity {self.name}>'

class HotelAmenity(db.Model):
    __tablename__ = 'hotel_amenities'

    hotel_id = db.Column(db.Integer, db.ForeignKey('hotels.id'), primary_key=True)
    amenity_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), primary_key=True)
