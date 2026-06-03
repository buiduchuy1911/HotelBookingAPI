# pyrefly: ignore [missing-import]
from flask import request, jsonify
from app import db, bcrypt
from app.models.user import User
from app.schemas.user_schema import UserRegistrationSchema, UserLoginSchema
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError

def register_user():
    schema = UserRegistrationSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Check if user exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"message": "Email already exists"}), 400

    # Hash password
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    # Create new user
    new_user = User(
        email=data['email'],
        password_hash=hashed_password,
        full_name=data['full_name'],
        role='registered' # Default role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

def login_user():
    schema = UserLoginSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password_hash, data['password']):
        # Include role in JWT claims
        additional_claims = {"role": user.role}
        access_token = create_access_token(identity=str(user.id), additional_claims=additional_claims)
        
        return jsonify({
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "email": user.email,
                "full_name": user.full_name,
                "role": user.role
            }
        }), 200
    else:
        return jsonify({"message": "Invalid email or password"}), 401
