from flask import request, jsonify
from my_project.rental.service.location_service import LocationService

_svc = LocationService()


def get_all_locations():
    return jsonify(_svc.get_all()), 200


def get_location(loc_id: int):
    result = _svc.get_by_id(loc_id)
    if result is None:
        return jsonify({"error": "Location not found"}), 404
    return jsonify(result), 200


def create_location():
    data = request.get_json()
    if not data or "city" not in data or "street_address" not in data:
        return jsonify({"error": "city and street_address are required"}), 400
    return jsonify(_svc.create(data)), 201


def update_location(loc_id: int):
    data = request.get_json()
    if not data or "city" not in data or "street_address" not in data:
        return jsonify({"error": "city and street_address are required"}), 400
    result = _svc.update(loc_id, data)
    if result is None:
        return jsonify({"error": "Location not found"}), 404
    return jsonify(result), 200


def delete_location(loc_id: int):
    if not _svc.delete(loc_id):
        return jsonify({"error": "Location not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
