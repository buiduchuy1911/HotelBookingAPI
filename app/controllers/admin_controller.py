from flask import request, jsonify
from app import db
from app.models.user import User
from app.schemas.user_schema import UserSchema

user_schema = UserSchema()
users_schema = UserSchema(many=True)

def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200

def update_user_role(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    
    if 'role' in data and data['role'] in ['admin', 'registered']:
        user.role = data['role']
        db.session.commit()
        return jsonify(user_schema.dump(user)), 200
    
    return jsonify({"message": "Invalid role"}), 400

def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 200
