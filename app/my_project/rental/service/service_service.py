from my_project.rental.dao.service_dao import ServiceDAO


class ServiceService:
    def get_all(self) -> list[dict]:
        return [s.to_dict() for s in ServiceDAO.get_all()]

    def get_by_id(self, svc_id: int) -> dict | None:
        s = ServiceDAO.get_by_id(svc_id)
        return s.to_dict() if s else None

    def create(self, data: dict) -> dict:
        s = ServiceDAO.create(
            services_name=data["services_name"],
            price=data["price"],
        )
        return s.to_dict()

    def update(self, svc_id: int, data: dict) -> dict | None:
        s = ServiceDAO.get_by_id(svc_id)
        if not s:
            return None
        s = ServiceDAO.update(s,
            services_name=data["services_name"],
            price=data["price"],
        )
        return s.to_dict()

    def delete(self, svc_id: int) -> bool:
        s = ServiceDAO.get_by_id(svc_id)
        if not s:
            return False
        ServiceDAO.delete(s)
        return True
