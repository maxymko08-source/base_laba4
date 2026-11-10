from my_project import db
from my_project.rental.domain.rental_status import RentalStatus


class RentalStatusDAO:
    @staticmethod
    def get_all() -> list[RentalStatus]:
        return RentalStatus.query.all()

    @staticmethod
    def get_by_id(status_id: int) -> RentalStatus | None:
        return RentalStatus.query.get(status_id)

    @staticmethod
    def create(status_name: str) -> RentalStatus:
        status = RentalStatus(status_name=status_name)
        db.session.add(status)
        db.session.commit()
        return status

    @staticmethod
    def update(status: RentalStatus, status_name: str) -> RentalStatus:
        status.status_name = status_name
        db.session.commit()
        return status

    @staticmethod
    def delete(status: RentalStatus) -> None:
        db.session.delete(status)
        db.session.commit()
