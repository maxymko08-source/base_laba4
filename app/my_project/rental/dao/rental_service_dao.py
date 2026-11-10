from my_project import db
from my_project.rental.domain.rental_service import RentalService
from my_project.rental.domain.service import Service


class RentalServiceDAO:
    @staticmethod
    def get_all() -> list[RentalService]:
        return RentalService.query.all()

    @staticmethod
    def get_by_pk(rentals_id: int, services_id: int) -> RentalService | None:
        return RentalService.query.get((rentals_id, services_id))

    @staticmethod
    def get_services_for_rental(rental_id: int) -> list[Service]:
        """M:M — all services attached to a rental."""
        return (
            Service.query
            .join(RentalService, RentalService.services_id == Service.id)
            .filter(RentalService.rentals_id == rental_id)
            .all()
        )

    @staticmethod
    def get_rentals_for_service(service_id: int) -> list[RentalService]:
        """M:M — all rental_service rows for a service."""
        return RentalService.query.filter_by(services_id=service_id).all()

    @staticmethod
    def create(rentals_id: int, services_id: int,
               quantity: int, fixed_price) -> RentalService:
        rs = RentalService(rentals_id=rentals_id, services_id=services_id,
                           quantity=quantity, fixed_price=fixed_price)
        db.session.add(rs)
        db.session.commit()
        return rs

    @staticmethod
    def update(rs: RentalService, quantity: int, fixed_price) -> RentalService:
        rs.quantity = quantity
        rs.fixed_price = fixed_price
        db.session.commit()
        return rs

    @staticmethod
    def delete(rs: RentalService) -> None:
        db.session.delete(rs)
        db.session.commit()
