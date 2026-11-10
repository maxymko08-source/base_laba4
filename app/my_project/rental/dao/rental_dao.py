from sqlalchemy import text
from my_project import db
from my_project.rental.domain.rental import Rental


class RentalDAO:
    @staticmethod
    def get_all() -> list[Rental]:
        return Rental.query.all()

    @staticmethod
    def get_by_id(rental_id: int) -> Rental | None:
        return Rental.query.get(rental_id)

    @staticmethod
    def get_by_user(user_id: int) -> list[Rental]:
        """1:M — all rentals for a given user."""
        return Rental.query.filter_by(users_id=user_id).all()

    @staticmethod
    def get_by_car(car_id: int) -> list[Rental]:
        """1:M — all rentals for a given car."""
        return Rental.query.filter_by(cars_id=car_id).all()

    @staticmethod
    def create(start_date, end_date, users_id: int, cars_id: int,
               rental_statuses_id: int, pickup_location_id: int,
               dropoff_location_id: int) -> Rental:
        rental = Rental(
            start_date=start_date,
            end_date=end_date,
            users_id=users_id,
            cars_id=cars_id,
            rental_statuses_id=rental_statuses_id,
            pickup_location_id=pickup_location_id,
            dropoff_location_id=dropoff_location_id,
        )
        db.session.add(rental)
        db.session.commit()
        return rental

    @staticmethod
    def update(rental: Rental, start_date, end_date, users_id: int,
               cars_id: int, rental_statuses_id: int,
               pickup_location_id: int, dropoff_location_id: int) -> Rental:
        rental.start_date = start_date
        rental.end_date = end_date
        rental.users_id = users_id
        rental.cars_id = cars_id
        rental.rental_statuses_id = rental_statuses_id
        rental.pickup_location_id = pickup_location_id
        rental.dropoff_location_id = dropoff_location_id
        db.session.commit()
        return rental

    @staticmethod
    def delete(rental: Rental) -> None:
        db.session.delete(rental)
        db.session.commit()

    @staticmethod
    def call_get_rental_summary(rental_id: int) -> dict:
        """Call stored procedure get_rental_summary(rental_id)."""
        result = db.session.execute(
            text("CALL get_rental_summary(:rid)"),
            {"rid": rental_id}
        )
        row = result.fetchone()
        if row is None:
            return {}
        return dict(row._mapping)
