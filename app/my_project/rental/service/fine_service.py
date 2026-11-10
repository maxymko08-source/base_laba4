from my_project.rental.dao.fine_dao import FineDAO


class FineService:
    def get_all(self) -> list[dict]:
        return [f.to_dict() for f in FineDAO.get_all()]

    def get_by_id(self, fine_id: int) -> dict | None:
        f = FineDAO.get_by_id(fine_id)
        return f.to_dict() if f else None

    def get_by_rental(self, rental_id: int) -> list[dict]:
        return [f.to_dict() for f in FineDAO.get_by_rental(rental_id)]

    def create(self, data: dict) -> dict:
        f = FineDAO.create(
            issue_date=data["issue_date"],
            actual_amount=data["actual_amount"],
            rentals_id=data["rentals_id"],
            fine_types_id=data["fine_types_id"],
        )
        return f.to_dict()

    def update(self, fine_id: int, data: dict) -> dict | None:
        f = FineDAO.get_by_id(fine_id)
        if not f:
            return None
        f = FineDAO.update(f,
            issue_date=data["issue_date"],
            actual_amount=data["actual_amount"],
            rentals_id=data["rentals_id"],
            fine_types_id=data["fine_types_id"],
        )
        return f.to_dict()

    def delete(self, fine_id: int) -> bool:
        f = FineDAO.get_by_id(fine_id)
        if not f:
            return False
        FineDAO.delete(f)
        return True
