from app import db

class RoomType(db.Model):
    __tablename__ = 'room_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    max_occupancy = db.Column(db.Integer, nullable=False)
    base_price = db.Column(db.Numeric(10, 2), nullable=False)
    description = db.Column(db.Text, nullable=True)

    # Relationships
    rooms = db.relationship('Room', backref='room_type', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<RoomType {self.name}>'
