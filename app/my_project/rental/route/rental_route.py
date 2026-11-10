from flask import Blueprint
from my_project.rental.controller import rental_controller as ctrl

rental_bp = Blueprint("rentals", __name__, url_prefix="/api")

# CRUD
rental_bp.get("/rentals")(ctrl.get_all_rentals)
rental_bp.get("/rentals/<int:rental_id>")(ctrl.get_rental)
rental_bp.post("/rentals")(ctrl.create_rental)
rental_bp.put("/rentals/<int:rental_id>")(ctrl.update_rental)
rental_bp.delete("/rentals/<int:rental_id>")(ctrl.delete_rental)

# 1:M relations
rental_bp.get("/users/<int:user_id>/rentals")(ctrl.get_rentals_by_user)
rental_bp.get("/cars/<int:car_id>/rentals")(ctrl.get_rentals_by_car)

# Stored procedure
rental_bp.get("/rentals/<int:rental_id>/summary")(ctrl.rental_summary)
