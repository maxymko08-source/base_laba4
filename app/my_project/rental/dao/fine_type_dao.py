from my_project import db
from my_project.rental.domain.fine_type import FineType


class FineTypeDAO:
    @staticmethod
    def get_all() -> list[FineType]:
        return FineType.query.all()

    @staticmethod
    def get_by_id(ft_id: int) -> FineType | None:
        return FineType.query.get(ft_id)

    @staticmethod
    def create(name: str, standard_amount) -> FineType:
        ft = FineType(name=name, standard_amount=standard_amount)
        db.session.add(ft)
        db.session.commit()
        return ft

    @staticmethod
    def update(ft: FineType, name: str, standard_amount) -> FineType:
        ft.name = name
        ft.standard_amount = standard_amount
        db.session.commit()
        return ft

    @staticmethod
    def delete(ft: FineType) -> None:
        db.session.delete(ft)
        db.session.commit()
