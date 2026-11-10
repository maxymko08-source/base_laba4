from flask import request, jsonify
from my_project.rental.service.car_service import CarService

_svc = CarService()

REQUIRED = ["license_plate", "year", "car_models_id", "car_categories_id", "locations_id"]


def get_all_cars():
    return jsonify(_svc.get_all()), 200


def get_car(car_id: int):
    result = _svc.get_by_id(car_id)
    if result is None:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(result), 200


def get_cars_by_location(location_id: int):
    """1:M — GET /api/locations/<id>/cars"""
    return jsonify(_svc.get_by_location(location_id)), 200


def create_car():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_car(car_id: int):
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    result = _svc.update(car_id, data)
    if result is None:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(result), 200


def delete_car(car_id: int):
    if not _svc.delete(car_id):
        return jsonify({"error": "Car not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
