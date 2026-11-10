from flask import Blueprint
from my_project.rental.controller import car_controller as ctrl

car_bp = Blueprint("cars", __name__, url_prefix="/api")

# CRUD
car_bp.get("/cars")(ctrl.get_all_cars)
car_bp.get("/cars/<int:car_id>")(ctrl.get_car)
car_bp.post("/cars")(ctrl.create_car)
car_bp.put("/cars/<int:car_id>")(ctrl.update_car)
car_bp.delete("/cars/<int:car_id>")(ctrl.delete_car)

# 1:M — all cars at a location
car_bp.get("/locations/<int:location_id>/cars")(ctrl.get_cars_by_location)
