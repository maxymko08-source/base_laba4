from flask import Blueprint
from my_project.rental.controller import rental_status_controller as ctrl

rental_status_bp = Blueprint("rental_statuses", __name__, url_prefix="/api/rental-statuses")

rental_status_bp.get("")(ctrl.get_all_statuses)
rental_status_bp.get("/<int:status_id>")(ctrl.get_status)
rental_status_bp.post("")(ctrl.create_status)
rental_status_bp.put("/<int:status_id>")(ctrl.update_status)
rental_status_bp.delete("/<int:status_id>")(ctrl.delete_status)
