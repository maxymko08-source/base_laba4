from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask) -> None:
    """Initialize extensions and register all blueprints."""
    db.init_app(app)

    from my_project.rental.route.car_brand_route import car_brand_bp
    from my_project.rental.route.car_category_route import car_category_bp
    from my_project.rental.route.car_model_route import car_model_bp
    from my_project.rental.route.location_route import location_bp
    from my_project.rental.route.car_route import car_bp
    from my_project.rental.route.user_route import user_bp
    from my_project.rental.route.rental_status_route import rental_status_bp
    from my_project.rental.route.rental_route import rental_bp
    from my_project.rental.route.fine_type_route import fine_type_bp
    from my_project.rental.route.fine_route import fine_bp
    from my_project.rental.route.payment_route import payment_bp
    from my_project.rental.route.service_route import service_bp
    from my_project.rental.route.rental_service_route import rental_service_bp
    from my_project.rental.route.user_passport_route import user_passport_bp
    from my_project.rental.route.procedure_route import procedure_bp

    for bp in [
        car_brand_bp, car_category_bp, car_model_bp, location_bp,
        car_bp, user_bp, rental_status_bp, rental_bp,
        fine_type_bp, fine_bp, payment_bp, service_bp,
        rental_service_bp, user_passport_bp, procedure_bp,
    ]:
        app.register_blueprint(bp)
