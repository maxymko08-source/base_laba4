from my_project import db
from my_project.rental.domain.service import Service


class ServiceDAO:
    @staticmethod
    def get_all() -> list[Service]:
        return Service.query.all()

    @staticmethod
    def get_by_id(svc_id: int) -> Service | None:
        return Service.query.get(svc_id)

    @staticmethod
    def create(services_name: str, price) -> Service:
        svc = Service(services_name=services_name, price=price)
        db.session.add(svc)
        db.session.commit()
        return svc

    @staticmethod
    def update(svc: Service, services_name: str, price) -> Service:
        svc.services_name = services_name
        svc.price = price
        db.session.commit()
        return svc

    @staticmethod
    def delete(svc: Service) -> None:
        db.session.delete(svc)
        db.session.commit()
