from flask import Blueprint
from my_project.rental.controller import fine_type_controller as ctrl

fine_type_bp = Blueprint("fine_types", __name__, url_prefix="/api/fine-types")

fine_type_bp.get("")(ctrl.get_all_fine_types)
fine_type_bp.get("/<int:ft_id>")(ctrl.get_fine_type)
fine_type_bp.post("")(ctrl.create_fine_type)
fine_type_bp.put("/<int:ft_id>")(ctrl.update_fine_type)
fine_type_bp.delete("/<int:ft_id>")(ctrl.delete_fine_type)
