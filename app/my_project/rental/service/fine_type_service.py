from my_project.rental.dao.fine_type_dao import FineTypeDAO


class FineTypeService:
    def get_all(self) -> list[dict]:
        return [ft.to_dict() for ft in FineTypeDAO.get_all()]

    def get_by_id(self, ft_id: int) -> dict | None:
        ft = FineTypeDAO.get_by_id(ft_id)
        return ft.to_dict() if ft else None

    def create(self, data: dict) -> dict:
        ft = FineTypeDAO.create(
            name=data["name"],
            standard_amount=data.get("standard_amount"),
        )
        return ft.to_dict()

    def update(self, ft_id: int, data: dict) -> dict | None:
        ft = FineTypeDAO.get_by_id(ft_id)
        if not ft:
            return None
        ft = FineTypeDAO.update(ft,
            name=data["name"],
            standard_amount=data.get("standard_amount"),
        )
        return ft.to_dict()

    def delete(self, ft_id: int) -> bool:
        ft = FineTypeDAO.get_by_id(ft_id)
        if not ft:
            return False
        FineTypeDAO.delete(ft)
        return True
