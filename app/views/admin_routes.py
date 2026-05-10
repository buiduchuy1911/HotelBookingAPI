from flask import Blueprint
from app.controllers.admin_controller import get_users, update_user_role, delete_user
from app.utils.decorators import role_required

admin_bp = Blueprint('admin_bp', __name__)

admin_bp.route('/users', methods=['GET'])(role_required('admin')(get_users))
admin_bp.route('/users/<int:user_id>/role', methods=['PUT'])(role_required('admin')(update_user_role))
admin_bp.route('/users/<int:user_id>', methods=['DELETE'])(role_required('admin')(delete_user))
