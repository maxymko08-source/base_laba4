from flask import Blueprint
from my_project.rental.controller import user_passport_controller as ctrl

user_passport_bp = Blueprint("user_passports", __name__, url_prefix="/api")

# CRUD
user_passport_bp.get("/passports")(ctrl.get_all_passports)
user_passport_bp.get("/passports/<int:passport_id>")(ctrl.get_passport)
user_passport_bp.post("/passports")(ctrl.create_passport)
user_passport_bp.put("/passports/<int:passport_id>")(ctrl.update_passport)
user_passport_bp.delete("/passports/<int:passport_id>")(ctrl.delete_passport)

# 1:M — passports for user
user_passport_bp.get("/users/<int:user_id>/passports")(ctrl.get_passports_by_user)
