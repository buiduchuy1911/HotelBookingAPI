from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import jsonify

def role_required(required_role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("role") == required_role or claims.get("role") == "admin":
                # Admin has access to everything
                return fn(*args, **kwargs)
            else:
                return jsonify({"msg": "Admins or specific roles only!"}), 403
        return decorator
    return wrapper
