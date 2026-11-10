from flask import Blueprint
from my_project.rental.controller import user_controller as ctrl

user_bp = Blueprint("users", __name__, url_prefix="/api/users")

user_bp.get("")(ctrl.get_all_users)
user_bp.get("/<int:user_id>")(ctrl.get_user)
user_bp.post("")(ctrl.create_user)
user_bp.put("/<int:user_id>")(ctrl.update_user)
user_bp.delete("/<int:user_id>")(ctrl.delete_user)
