from flask import Blueprint
from my_project.rental.controller import car_brand_controller as ctrl

car_brand_bp = Blueprint("car_brands", __name__, url_prefix="/api/car-brands")

car_brand_bp.get("")(ctrl.get_all_brands)
car_brand_bp.get("/<int:brand_id>")(ctrl.get_brand)
car_brand_bp.post("")(ctrl.create_brand)
car_brand_bp.put("/<int:brand_id>")(ctrl.update_brand)
car_brand_bp.delete("/<int:brand_id>")(ctrl.delete_brand)
