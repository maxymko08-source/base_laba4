from flask import request, jsonify
from my_project.rental.service.car_category_service import CarCategoryService

_svc = CarCategoryService()


def get_all_categories():
    return jsonify(_svc.get_all()), 200


def get_category(cat_id: int):
    result = _svc.get_by_id(cat_id)
    if result is None:
        return jsonify({"error": "CarCategory not found"}), 404
    return jsonify(result), 200


def create_category():
    data = request.get_json()
    if not data or "category_name" not in data or "daily_price" not in data:
        return jsonify({"error": "category_name and daily_price are required"}), 400
    return jsonify(_svc.create(data)), 201


def update_category(cat_id: int):
    data = request.get_json()
    if not data or "category_name" not in data or "daily_price" not in data:
        return jsonify({"error": "category_name and daily_price are required"}), 400
    result = _svc.update(cat_id, data)
    if result is None:
        return jsonify({"error": "CarCategory not found"}), 404
    return jsonify(result), 200


def delete_category(cat_id: int):
    if not _svc.delete(cat_id):
        return jsonify({"error": "CarCategory not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
