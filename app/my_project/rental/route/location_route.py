from flask import Blueprint
from my_project.rental.controller import location_controller as ctrl

location_bp = Blueprint("locations", __name__, url_prefix="/api/locations")

location_bp.get("")(ctrl.get_all_locations)
location_bp.get("/<int:loc_id>")(ctrl.get_location)
location_bp.post("")(ctrl.create_location)
location_bp.put("/<int:loc_id>")(ctrl.update_location)
location_bp.delete("/<int:loc_id>")(ctrl.delete_location)
