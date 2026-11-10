from flask import request, jsonify
from my_project.rental.service.rental_service import RentalService

_svc = RentalService()

REQUIRED = [
    "start_date", "end_date", "users_id", "cars_id",
    "rental_statuses_id", "pickup_location_id", "dropoff_location_id",
]


def get_all_rentals():
    return jsonify(_svc.get_all()), 200


def get_rental(rental_id: int):
    result = _svc.get_by_id(rental_id)
    if result is None:
        return jsonify({"error": "Rental not found"}), 404
    return jsonify(result), 200


def get_rentals_by_user(user_id: int):
    """1:M — GET /api/users/<id>/rentals"""
    return jsonify(_svc.get_by_user(user_id)), 200


def get_rentals_by_car(car_id: int):
    """1:M — GET /api/cars/<id>/rentals"""
    return jsonify(_svc.get_by_car(car_id)), 200


def create_rental():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_rental(rental_id: int):
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    result = _svc.update(rental_id, data)
    if result is None:
        return jsonify({"error": "Rental not found"}), 404
    return jsonify(result), 200


def delete_rental(rental_id: int):
    if not _svc.delete(rental_id):
        return jsonify({"error": "Rental not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200


def rental_summary(rental_id: int):
    """Call stored procedure get_rental_summary."""
    result = _svc.get_rental_summary(rental_id)
    if not result:
        return jsonify({"error": "No data for this rental"}), 404
    return jsonify(result), 200
