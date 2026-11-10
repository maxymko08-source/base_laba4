from flask import Blueprint
from my_project.rental.controller import car_model_controller as ctrl

car_model_bp = Blueprint("car_models", __name__, url_prefix="/api")

# CRUD for car models
car_model_bp.get("/car-models")(ctrl.get_all_models)
car_model_bp.get("/car-models/<int:model_id>")(ctrl.get_model)
car_model_bp.post("/car-models")(ctrl.create_model)
car_model_bp.put("/car-models/<int:model_id>")(ctrl.update_model)
car_model_bp.delete("/car-models/<int:model_id>")(ctrl.delete_model)

# 1:M — all models for a brand
car_model_bp.get("/car-brands/<int:brand_id>/models")(ctrl.get_models_by_brand)
