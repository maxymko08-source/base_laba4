from my_project.rental.dao.rental_status_dao import RentalStatusDAO


class RentalStatusService:
    def get_all(self) -> list[dict]:
        return [s.to_dict() for s in RentalStatusDAO.get_all()]

    def get_by_id(self, status_id: int) -> dict | None:
        s = RentalStatusDAO.get_by_id(status_id)
        return s.to_dict() if s else None

    def create(self, data: dict) -> dict:
        s = RentalStatusDAO.create(status_name=data["status_name"])
        return s.to_dict()

    def update(self, status_id: int, data: dict) -> dict | None:
        s = RentalStatusDAO.get_by_id(status_id)
        if not s:
            return None
        s = RentalStatusDAO.update(s, status_name=data["status_name"])
        return s.to_dict()

    def delete(self, status_id: int) -> bool:
        s = RentalStatusDAO.get_by_id(status_id)
        if not s:
            return False
        RentalStatusDAO.delete(s)
        return True
