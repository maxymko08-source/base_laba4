from flask import request, jsonify
from my_project.rental.service.rental_service_service import RentalServiceService

_svc = RentalServiceService()

REQUIRED = ["rentals_id", "services_id", "quantity", "fixed_price"]


def get_all_rental_services():
    return jsonify(_svc.get_all()), 200


def get_rental_service(rentals_id: int, services_id: int):
    result = _svc.get_by_pk(rentals_id, services_id)
    if result is None:
        return jsonify({"error": "RentalService not found"}), 404
    return jsonify(result), 200


def get_services_for_rental(rental_id: int):
    """M:M — GET /api/rentals/<id>/services"""
    return jsonify(_svc.get_services_for_rental(rental_id)), 200


def get_rentals_for_service(service_id: int):
    """M:M — GET /api/services/<id>/rentals"""
    return jsonify(_svc.get_rentals_for_service(service_id)), 200


def create_rental_service():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_rental_service(rentals_id: int, services_id: int):
    data = request.get_json()
    if not data or "quantity" not in data or "fixed_price" not in data:
        return jsonify({"error": "quantity and fixed_price are required"}), 400
    result = _svc.update(rentals_id, services_id, data)
    if result is None:
        return jsonify({"error": "RentalService not found"}), 404
    return jsonify(result), 200


def delete_rental_service(rentals_id: int, services_id: int):
    if not _svc.delete(rentals_id, services_id):
        return jsonify({"error": "RentalService not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
