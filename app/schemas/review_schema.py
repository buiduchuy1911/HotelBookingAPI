from app import ma
from app.models.review import Review
from marshmallow import fields, validate

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True

class CreateReviewSchema(ma.Schema):
    rating = fields.Integer(required=True, validate=validate.Range(min=1, max=5))
    comment = fields.String(required=False)
