from flask import request, jsonify
from my_project.rental.service.fine_service import FineService

_svc = FineService()

REQUIRED = ["issue_date", "actual_amount", "rentals_id", "fine_types_id"]


def get_all_fines():
    return jsonify(_svc.get_all()), 200


def get_fine(fine_id: int):
    result = _svc.get_by_id(fine_id)
    if result is None:
        return jsonify({"error": "Fine not found"}), 404
    return jsonify(result), 200


def get_fines_by_rental(rental_id: int):
    """1:M — GET /api/rentals/<id>/fines"""
    return jsonify(_svc.get_by_rental(rental_id)), 200


def create_fine():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_fine(fine_id: int):
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    result = _svc.update(fine_id, data)
    if result is None:
        return jsonify({"error": "Fine not found"}), 404
    return jsonify(result), 200


def delete_fine(fine_id: int):
    if not _svc.delete(fine_id):
        return jsonify({"error": "Fine not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
