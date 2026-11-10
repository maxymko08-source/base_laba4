from my_project import db
from my_project.rental.domain.car import Car


class CarDAO:
    @staticmethod
    def get_all() -> list[Car]:
        return Car.query.all()

    @staticmethod
    def get_by_id(car_id: int) -> Car | None:
        return Car.query.get(car_id)

    @staticmethod
    def get_by_location(location_id: int) -> list[Car]:
        """1:M — all cars at a given location."""
        return Car.query.filter_by(locations_id=location_id).all()

    @staticmethod
    def create(license_plate: str, year: int, car_models_id: int,
               car_categories_id: int, locations_id: int) -> Car:
        car = Car(
            license_plate=license_plate,
            year=year,
            car_models_id=car_models_id,
            car_categories_id=car_categories_id,
            locations_id=locations_id,
        )
        db.session.add(car)
        db.session.commit()
        return car

    @staticmethod
    def update(car: Car, license_plate: str, year: int, car_models_id: int,
               car_categories_id: int, locations_id: int) -> Car:
        car.license_plate = license_plate
        car.year = year
        car.car_models_id = car_models_id
        car.car_categories_id = car_categories_id
        car.locations_id = locations_id
        db.session.commit()
        return car

    @staticmethod
    def delete(car: Car) -> None:
        db.session.delete(car)
        db.session.commit()
