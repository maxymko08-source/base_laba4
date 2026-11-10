from my_project.rental.dao.car_category_dao import CarCategoryDAO


class CarCategoryService:
    def get_all(self) -> list[dict]:
        return [c.to_dict() for c in CarCategoryDAO.get_all()]

    def get_by_id(self, cat_id: int) -> dict | None:
        cat = CarCategoryDAO.get_by_id(cat_id)
        return cat.to_dict() if cat else None

    def create(self, data: dict) -> dict:
        cat = CarCategoryDAO.create(
            category_name=data["category_name"],
            daily_price=data["daily_price"],
        )
        return cat.to_dict()

    def update(self, cat_id: int, data: dict) -> dict | None:
        cat = CarCategoryDAO.get_by_id(cat_id)
        if not cat:
            return None
        cat = CarCategoryDAO.update(cat,
            category_name=data["category_name"],
            daily_price=data["daily_price"],
        )
        return cat.to_dict()

    def delete(self, cat_id: int) -> bool:
        cat = CarCategoryDAO.get_by_id(cat_id)
        if not cat:
            return False
        CarCategoryDAO.delete(cat)
        return True
