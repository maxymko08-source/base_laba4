from flask import request, jsonify
from my_project.rental.service.fine_type_service import FineTypeService

_svc = FineTypeService()


def get_all_fine_types():
    return jsonify(_svc.get_all()), 200


def get_fine_type(ft_id: int):
    result = _svc.get_by_id(ft_id)
    if result is None:
        return jsonify({"error": "FineType not found"}), 404
    return jsonify(result), 200


def create_fine_type():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400
    return jsonify(_svc.create(data)), 201


def update_fine_type(ft_id: int):
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "name is required"}), 400
    result = _svc.update(ft_id, data)
    if result is None:
        return jsonify({"error": "FineType not found"}), 404
    return jsonify(result), 200


def delete_fine_type(ft_id: int):
    if not _svc.delete(ft_id):
        return jsonify({"error": "FineType not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
