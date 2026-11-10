from flask import Blueprint
from my_project.rental.controller import car_category_controller as ctrl

car_category_bp = Blueprint("car_categories", __name__, url_prefix="/api/car-categories")

car_category_bp.get("")(ctrl.get_all_categories)
car_category_bp.get("/<int:cat_id>")(ctrl.get_category)
car_category_bp.post("")(ctrl.create_category)
car_category_bp.put("/<int:cat_id>")(ctrl.update_category)
car_category_bp.delete("/<int:cat_id>")(ctrl.delete_category)
