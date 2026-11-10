from my_project import db
from my_project.rental.domain.car_category import CarCategory


class CarCategoryDAO:
    @staticmethod
    def get_all() -> list[CarCategory]:
        return CarCategory.query.all()

    @staticmethod
    def get_by_id(cat_id: int) -> CarCategory | None:
        return CarCategory.query.get(cat_id)

    @staticmethod
    def create(category_name: str, daily_price: int) -> CarCategory:
        cat = CarCategory(category_name=category_name, daily_price=daily_price)
        db.session.add(cat)
        db.session.commit()
        return cat

    @staticmethod
    def update(cat: CarCategory, category_name: str, daily_price: int) -> CarCategory:
        cat.category_name = category_name
        cat.daily_price = daily_price
        db.session.commit()
        return cat

    @staticmethod
    def delete(cat: CarCategory) -> None:
        db.session.delete(cat)
        db.session.commit()
