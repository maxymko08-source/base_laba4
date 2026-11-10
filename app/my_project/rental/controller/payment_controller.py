from flask import request, jsonify
from my_project.rental.service.payment_service import PaymentService

_svc = PaymentService()

REQUIRED = ["amount", "payment_date", "rentals_id"]


def get_all_payments():
    return jsonify(_svc.get_all()), 200


def get_payment(pay_id: int):
    result = _svc.get_by_id(pay_id)
    if result is None:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify(result), 200


def get_payments_by_rental(rental_id: int):
    """1:M — GET /api/rentals/<id>/payments"""
    return jsonify(_svc.get_by_rental(rental_id)), 200


def create_payment():
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    return jsonify(_svc.create(data)), 201


def update_payment(pay_id: int):
    data = request.get_json()
    if not data or not all(k in data for k in REQUIRED):
        return jsonify({"error": f"Required fields: {REQUIRED}"}), 400
    result = _svc.update(pay_id, data)
    if result is None:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify(result), 200


def delete_payment(pay_id: int):
    if not _svc.delete(pay_id):
        return jsonify({"error": "Payment not found"}), 404
    return jsonify({"message": "Deleted successfully"}), 200
