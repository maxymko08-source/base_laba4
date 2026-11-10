from flask import request, jsonify
from my_project.rental.service.user_service import UserService

_svc = UserService()

REQUIRED = ["first_name", "last_name", "email"]


def get_all_users():
    return jsonify(_svc.get_all()), 200


def get_user(user_id: int):
    result = _svc.get_by_id(user_id)
    if result is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(result), 200


def create_user():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_user(user_id: int):
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    result = _svc.update(user_id, data)
    if result is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(result), 200


def delete_user(user_id: int):
    if not _svc.delete(user_id):
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
