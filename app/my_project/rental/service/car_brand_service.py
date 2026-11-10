from my_project.rental.dao.car_brand_dao import CarBrandDAO
from my_project.rental.domain.car_brand import CarBrand


class CarBrandService:
    def get_all(self) -> list[dict]:
        return [b.to_dict() for b in CarBrandDAO.get_all()]

    def get_by_id(self, brand_id: int) -> dict | None:
        brand = CarBrandDAO.get_by_id(brand_id)
        return brand.to_dict() if brand else None

    def create(self, data: dict) -> dict:
        brand = CarBrandDAO.create(brand_name=data["brand_name"])
        return brand.to_dict()

    def update(self, brand_id: int, data: dict) -> dict | None:
        brand = CarBrandDAO.get_by_id(brand_id)
        if not brand:
            return None
        brand = CarBrandDAO.update(brand, brand_name=data["brand_name"])
        return brand.to_dict()

    def delete(self, brand_id: int) -> bool:
        brand = CarBrandDAO.get_by_id(brand_id)
        if not brand:
            return False
        CarBrandDAO.delete(brand)
        return True
