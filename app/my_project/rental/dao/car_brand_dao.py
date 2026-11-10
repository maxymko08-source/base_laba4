from my_project import db
from my_project.rental.domain.car_brand import CarBrand


class CarBrandDAO:
    @staticmethod
    def get_all() -> list[CarBrand]:
        return CarBrand.query.all()

    @staticmethod
    def get_by_id(brand_id: int) -> CarBrand | None:
        return CarBrand.query.get(brand_id)

    @staticmethod
    def create(brand_name: str) -> CarBrand:
        brand = CarBrand(brand_name=brand_name)
        db.session.add(brand)
        db.session.commit()
        return brand

    @staticmethod
    def update(brand: CarBrand, brand_name: str) -> CarBrand:
        brand.brand_name = brand_name
        db.session.commit()
        return brand

    @staticmethod
    def delete(brand: CarBrand) -> None:
        db.session.delete(brand)
        db.session.commit()
