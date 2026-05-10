from app import ma
from app.models.user import User
from marshmallow import fields, validate

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ('password_hash',) # Never serialize password_hash

class UserRegistrationSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    full_name = fields.String(required=True, validate=validate.Length(min=2))

class UserLoginSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True)
