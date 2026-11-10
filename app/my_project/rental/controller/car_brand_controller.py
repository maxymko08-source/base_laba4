from flask import request, jsonify
from my_project.rental.service.car_brand_service import CarBrandService

_svc = CarBrandService()


def get_all_brands():
    return jsonify(_svc.get_all()), 200


def get_brand(brand_id: int):
    result = _svc.get_by_id(brand_id)
    if result is None:
        return jsonify({"error": "CarBrand not found"}), 404
    return jsonify(result), 200


def create_brand():
    data = request.get_json()
    if not data or "brand_name" not in data:
        return jsonify({"error": "brand_name is required"}), 400
    return jsonify(_svc.create(data)), 201


def update_brand(brand_id: int):
    data = request.get_json()
    if not data or "brand_name" not in data:
        return jsonify({"error": "brand_name is required"}), 400
    result = _svc.update(brand_id, data)
    if result is None:
        return jsonify({"error": "CarBrand not found"}), 404
    return jsonify(result), 200


def delete_brand(brand_id: int):
    if not _svc.delete(brand_id):
        return jsonify({"error": "CarBrand not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
