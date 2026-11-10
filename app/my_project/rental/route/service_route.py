from flask import Blueprint
from my_project.rental.controller import service_controller as ctrl

service_bp = Blueprint("services", __name__, url_prefix="/api/services")

service_bp.get("")(ctrl.get_all_services)
service_bp.get("/<int:svc_id>")(ctrl.get_service)
service_bp.post("")(ctrl.create_service)
service_bp.put("/<int:svc_id>")(ctrl.update_service)
service_bp.delete("/<int:svc_id>")(ctrl.delete_service)
