from flask import Blueprint
from my_project.rental.controller import payment_controller as ctrl

payment_bp = Blueprint("payments", __name__, url_prefix="/api")

# CRUD
payment_bp.get("/payments")(ctrl.get_all_payments)
payment_bp.get("/payments/<int:pay_id>")(ctrl.get_payment)
payment_bp.post("/payments")(ctrl.create_payment)
payment_bp.put("/payments/<int:pay_id>")(ctrl.update_payment)
payment_bp.delete("/payments/<int:pay_id>")(ctrl.delete_payment)

# 1:M
payment_bp.get("/rentals/<int:rental_id>/payments")(ctrl.get_payments_by_rental)
