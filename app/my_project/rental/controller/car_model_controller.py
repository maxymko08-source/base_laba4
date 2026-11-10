from flask import request, jsonify
from my_project.rental.service.car_model_service import CarModelService

_svc = CarModelService()


def get_all_models():
    return jsonify(_svc.get_all()), 200


def get_model(model_id: int):
    result = _svc.get_by_id(model_id)
    if result is None:
        return jsonify({"error": "CarModel not found"}), 404
    return jsonify(result), 200


def get_models_by_brand(brand_id: int):
    """1:M — GET /api/car-brands/<id>/models"""
    return jsonify(_svc.get_by_brand(brand_id)), 200


def create_model():
    data = request.get_json()
    if not data or "model_name" not in data or "car_brands_id" not in data:
        return jsonify({"error": "model_name and car_brands_id are required"}), 400
    return jsonify(_svc.create(data)), 201


def update_model(model_id: int):
    data = request.get_json()
    if not data or "model_name" not in data or "car_brands_id" not in data:
        return jsonify({"error": "model_name and car_brands_id are required"}), 400
    result = _svc.update(model_id, data)
    if result is None:
        return jsonify({"error": "CarModel not found"}), 404
    return jsonify(result), 200


def delete_model(model_id: int):
    if not _svc.delete(model_id):
        return jsonify({"error": "CarModel not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
