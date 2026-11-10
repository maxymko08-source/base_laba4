from my_project import db
from my_project.rental.domain.car_model import CarModel


class CarModelDAO:
    @staticmethod
    def get_all() -> list[CarModel]:
        return CarModel.query.all()

    @staticmethod
    def get_by_id(model_id: int) -> CarModel | None:
        return CarModel.query.get(model_id)

    @staticmethod
    def get_by_brand(brand_id: int) -> list[CarModel]:
        """1:M — all models for a given brand."""
        return CarModel.query.filter_by(car_brands_id=brand_id).all()

    @staticmethod
    def create(model_name: str, car_brands_id: int) -> CarModel:
        model = CarModel(model_name=model_name, car_brands_id=car_brands_id)
        db.session.add(model)
        db.session.commit()
        return model

    @staticmethod
    def update(model: CarModel, model_name: str, car_brands_id: int) -> CarModel:
        model.model_name = model_name
        model.car_brands_id = car_brands_id
        db.session.commit()
        return model

    @staticmethod
    def delete(model: CarModel) -> None:
        db.session.delete(model)
        db.session.commit()
