from flask import Blueprint
from my_project.rental.controller import rental_service_controller as ctrl

rental_service_bp = Blueprint("rental_services", __name__, url_prefix="/api")

# CRUD on junction
rental_service_bp.get("/rental-services")(ctrl.get_all_rental_services)
rental_service_bp.get("/rental-services/<int:rentals_id>/<int:services_id>")(ctrl.get_rental_service)
rental_service_bp.post("/rental-services")(ctrl.create_rental_service)
rental_service_bp.put("/rental-services/<int:rentals_id>/<int:services_id>")(ctrl.update_rental_service)
rental_service_bp.delete("/rental-services/<int:rentals_id>/<int:services_id>")(ctrl.delete_rental_service)

# M:M endpoints
rental_service_bp.get("/rentals/<int:rental_id>/services")(ctrl.get_services_for_rental)
rental_service_bp.get("/services/<int:service_id>/rentals")(ctrl.get_rentals_for_service)
