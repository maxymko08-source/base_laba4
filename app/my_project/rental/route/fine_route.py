from flask import Blueprint
from my_project.rental.controller import fine_controller as ctrl

fine_bp = Blueprint("fines", __name__, url_prefix="/api")

# CRUD
fine_bp.get("/fines")(ctrl.get_all_fines)
fine_bp.get("/fines/<int:fine_id>")(ctrl.get_fine)
fine_bp.post("/fines")(ctrl.create_fine)
fine_bp.put("/fines/<int:fine_id>")(ctrl.update_fine)
fine_bp.delete("/fines/<int:fine_id>")(ctrl.delete_fine)

# 1:M
fine_bp.get("/rentals/<int:rental_id>/fines")(ctrl.get_fines_by_rental)
