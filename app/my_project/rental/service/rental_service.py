from my_project.rental.dao.rental_dao import RentalDAO


class RentalService:
    def get_all(self) -> list[dict]:
        return [r.to_dict() for r in RentalDAO.get_all()]

    def get_by_id(self, rental_id: int) -> dict | None:
        r = RentalDAO.get_by_id(rental_id)
        return r.to_dict() if r else None

    def get_by_user(self, user_id: int) -> list[dict]:
        return [r.to_dict() for r in RentalDAO.get_by_user(user_id)]

    def get_by_car(self, car_id: int) -> list[dict]:
        return [r.to_dict() for r in RentalDAO.get_by_car(car_id)]

    def create(self, data: dict) -> dict:
        r = RentalDAO.create(
            start_date=data["start_date"],
            end_date=data["end_date"],
            users_id=data["users_id"],
            cars_id=data["cars_id"],
            rental_statuses_id=data["rental_statuses_id"],
            pickup_location_id=data["pickup_location_id"],
            dropoff_location_id=data["dropoff_location_id"],
        )
        return r.to_dict()

    def update(self, rental_id: int, data: dict) -> dict | None:
        r = RentalDAO.get_by_id(rental_id)
        if not r:
            return None
        r = RentalDAO.update(r,
            start_date=data["start_date"],
            end_date=data["end_date"],
            users_id=data["users_id"],
            cars_id=data["cars_id"],
            rental_statuses_id=data["rental_statuses_id"],
            pickup_location_id=data["pickup_location_id"],
            dropoff_location_id=data["dropoff_location_id"],
        )
        return r.to_dict()

    def delete(self, rental_id: int) -> bool:
        r = RentalDAO.get_by_id(rental_id)
        if not r:
            return False
        RentalDAO.delete(r)
        return True

    def get_rental_summary(self, rental_id: int) -> dict:
        """Call stored procedure get_rental_summary."""
        return RentalDAO.call_get_rental_summary(rental_id)
