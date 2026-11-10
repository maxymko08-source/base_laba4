from my_project.rental.dao.car_dao import CarDAO


class CarService:
    def get_all(self) -> list[dict]:
        return [c.to_dict() for c in CarDAO.get_all()]

    def get_by_id(self, car_id: int) -> dict | None:
        c = CarDAO.get_by_id(car_id)
        return c.to_dict() if c else None

    def get_by_location(self, location_id: int) -> list[dict]:
        return [c.to_dict() for c in CarDAO.get_by_location(location_id)]

    def create(self, data: dict) -> dict:
        c = CarDAO.create(
            license_plate=data["license_plate"],
            year=data["year"],
            car_models_id=data["car_models_id"],
            car_categories_id=data["car_categories_id"],
            locations_id=data["locations_id"],
        )
        return c.to_dict()

    def update(self, car_id: int, data: dict) -> dict | None:
        c = CarDAO.get_by_id(car_id)
        if not c:
            return None
        c = CarDAO.update(c,
            license_plate=data["license_plate"],
            year=data["year"],
            car_models_id=data["car_models_id"],
            car_categories_id=data["car_categories_id"],
            locations_id=data["locations_id"],
        )
        return c.to_dict()

    def delete(self, car_id: int) -> bool:
        c = CarDAO.get_by_id(car_id)
        if not c:
            return False
        CarDAO.delete(c)
        return True
