from flask import request, jsonify
from my_project.rental.service.rental_status_service import RentalStatusService

_svc = RentalStatusService()


def get_all_statuses():
    return jsonify(_svc.get_all()), 200


def get_status(status_id: int):
    result = _svc.get_by_id(status_id)
    if result is None:
        return jsonify({"error": "RentalStatus not found"}), 404
    return jsonify(result), 200


def create_status():
    data = request.get_json()
    if not data or "status_name" not in data:
        return jsonify({"error": "status_name is required"}), 400
    return jsonify(_svc.create(data)), 201


def update_status(status_id: int):
    data = request.get_json()
    if not data or "status_name" not in data:
        return jsonify({"error": "status_name is required"}), 400
    result = _svc.update(status_id, data)
    if result is None:
        return jsonify({"error": "RentalStatus not found"}), 404
    return jsonify(result), 200


def delete_status(status_id: int):
    if not _svc.delete(status_id):
        return jsonify({"error": "RentalStatus not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
