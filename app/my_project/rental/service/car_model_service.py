from my_project.rental.dao.car_model_dao import CarModelDAO


class CarModelService:
    def get_all(self) -> list[dict]:
        return [m.to_dict() for m in CarModelDAO.get_all()]

    def get_by_id(self, model_id: int) -> dict | None:
        m = CarModelDAO.get_by_id(model_id)
        return m.to_dict() if m else None

    def get_by_brand(self, brand_id: int) -> list[dict]:
        return [m.to_dict() for m in CarModelDAO.get_by_brand(brand_id)]

    def create(self, data: dict) -> dict:
        m = CarModelDAO.create(
            model_name=data["model_name"],
            car_brands_id=data["car_brands_id"],
        )
        return m.to_dict()

    def update(self, model_id: int, data: dict) -> dict | None:
        m = CarModelDAO.get_by_id(model_id)
        if not m:
            return None
        m = CarModelDAO.update(m,
            model_name=data["model_name"],
            car_brands_id=data["car_brands_id"],
        )
        return m.to_dict()

    def delete(self, model_id: int) -> bool:
        m = CarModelDAO.get_by_id(model_id)
        if not m:
            return False
        CarModelDAO.delete(m)
        return True
