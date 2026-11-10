from flask import request, jsonify
from my_project.rental.service.user_passport_service import UserPassportService

_svc = UserPassportService()


def get_all_passports():
    return jsonify(_svc.get_all()), 200


def get_passport(passport_id: int):
    result = _svc.get_by_id(passport_id)
    if result is None:
        return jsonify({"error": "UserPassport not found"}), 404
    return jsonify(result), 200


def get_passports_by_user(user_id: int):
    """1:M — GET /api/users/<id>/passports"""
    return jsonify(_svc.get_by_user(user_id)), 200


def create_passport():
    data = request.get_json()
    if not data or "passport_number" not in data or "users_id" not in data:
        return jsonify({"error": "passport_number and users_id are required"}), 400
    return jsonify(_svc.create(data)), 201


def update_passport(passport_id: int):
    data = request.get_json()
    if not data or "passport_number" not in data:
        return jsonify({"error": "passport_number is required"}), 400
    result = _svc.update(passport_id, data)
    if result is None:
        return jsonify({"error": "UserPassport not found"}), 404
    return jsonify(result), 200


def delete_passport(passport_id: int):
    if not _svc.delete(passport_id):
        return jsonify({"error": "UserPassport not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
