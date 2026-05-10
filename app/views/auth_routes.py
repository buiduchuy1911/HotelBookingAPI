from flask import Blueprint
from app.controllers.auth_controller import register_user, login_user

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
            - full_name
          properties:
            email:
              type: string
              example: user@example.com
            password:
              type: string
              example: secret123
            full_name:
              type: string
              example: John Doe
    responses:
      201:
        description: User registered successfully
      400:
        description: Validation Error or Email already exists
    """
    return register_user()

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login user and get access token
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: user@example.com
            password:
              type: string
              example: secret123
    responses:
      200:
        description: Login successful
        schema:
          type: object
          properties:
            message:
              type: string
            access_token:
              type: string
            user:
              type: object
      401:
        description: Invalid email or password
    """
    return login_user()
