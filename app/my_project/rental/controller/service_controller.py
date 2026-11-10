from flask import request, jsonify
from my_project.rental.service.service_service import ServiceService

_svc = ServiceService()


def get_all_services():
    return jsonify(_svc.get_all()), 200


def get_service(svc_id: int):
    result = _svc.get_by_id(svc_id)
    if result is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(result), 200


def create_service():
    data = request.get_json()
    if not data or "services_name" not in data or "price" not in data:
        return jsonify({"error": "services_name and price are required"}), 400
    return jsonify(_svc.create(data)), 201


def update_service(svc_id: int):
    data = request.get_json()
    if not data or "services_name" not in data or "price" not in data:
        return jsonify({"error": "services_name and price are required"}), 400
    result = _svc.update(svc_id, data)
    if result is None:
        return jsonify({"error": "Service not found"}), 404
    return jsonify(result), 200


def delete_service(svc_id: int):
    if not _svc.delete(svc_id):
        return jsonify({"error": "Service not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
