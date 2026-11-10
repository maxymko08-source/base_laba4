from flask import Blueprint, jsonify
from my_project.rental.controller.rental_controller import rental_summary

procedure_bp = Blueprint("procedures", __name__, url_prefix="/api/procedures")


@procedure_bp.get("/rental-summary/<int:rental_id>")
def call_rental_summary(rental_id: int):
    """
    Calls the stored procedure get_rental_summary(rental_id).
    The procedure must exist in MySQL before calling this endpoint.

    CREATE PROCEDURE get_rental_summary(IN p_rental_id INT)
    BEGIN
        SELECT
            r.id AS rental_id,
            CONCAT(u.first_name, ' ', u.last_name) AS client_name,
            CONCAT(cb.brand_name, ' ', cm.model_name) AS car,
            r.start_date,
            r.end_date,
            DATEDIFF(r.end_date, r.start_date) AS rental_days,
            cc.daily_price * DATEDIFF(r.end_date, r.start_date) AS total_cost,
            rs.status_name AS status
        FROM rentals r
        JOIN users u ON r.users_id = u.id
        JOIN cars c ON r.cars_id = c.id
        JOIN car_models cm ON c.car_models_id = cm.id
        JOIN car_brands cb ON cm.car_brands_id = cb.id
        JOIN car_categories cc ON c.car_categories_id = cc.id
        JOIN rental_statuses rs ON r.rental_statuses_id = rs.id
        WHERE r.id = p_rental_id;
    END;
    """
    return rental_summary(rental_id)
