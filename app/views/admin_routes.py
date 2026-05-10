from flask import Blueprint
from app.controllers.admin_controller import get_users, update_user_role, delete_user
from app.utils.decorators import role_required

admin_bp = Blueprint('admin_bp', __name__)

@admin_bp.route('/users', methods=['GET'])
@role_required('admin')
def get_users_route():
    """
    Get all users (Admin only)
    ---
    tags:
      - Admin Users
    security:
      - Bearer: []
    responses:
      200:
        description: List of all users
    """
    return get_users()

@admin_bp.route('/users/<int:user_id>/role', methods=['PUT'])
@role_required('admin')
def update_user_role_route(user_id):
    """
    Update user role (Admin only)
    ---
    tags:
      - Admin Users
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            role:
              type: string
              enum: [admin, registered]
    responses:
      200:
        description: Role updated
    """
    return update_user_role(user_id)

@admin_bp.route('/users/<int:user_id>', methods=['DELETE'])
@role_required('admin')
def delete_user_route(user_id):
    """
    Delete a user (Admin only)
    ---
    tags:
      - Admin Users
    security:
      - Bearer: []
    parameters:
      - in: path
        name: user_id
        type: integer
        required: true
    responses:
      200:
        description: User deleted
    """
    return delete_user(user_id)
