from my_project.rental.dao.rental_service_dao import RentalServiceDAO


class RentalServiceService:
    def get_all(self) -> list[dict]:
        return [rs.to_dict() for rs in RentalServiceDAO.get_all()]

    def get_by_pk(self, rentals_id: int, services_id: int) -> dict | None:
        rs = RentalServiceDAO.get_by_pk(rentals_id, services_id)
        return rs.to_dict() if rs else None

    def get_services_for_rental(self, rental_id: int) -> list[dict]:
        """M:M — services for a given rental."""
        return [s.to_dict() for s in RentalServiceDAO.get_services_for_rental(rental_id)]

    def get_rentals_for_service(self, service_id: int) -> list[dict]:
        """M:M — rental_service rows for a given service."""
        return [rs.to_dict() for rs in RentalServiceDAO.get_rentals_for_service(service_id)]

    def create(self, data: dict) -> dict:
        rs = RentalServiceDAO.create(
            rentals_id=data["rentals_id"],
            services_id=data["services_id"],
            quantity=data["quantity"],
            fixed_price=data["fixed_price"],
        )
        return rs.to_dict()

    def update(self, rentals_id: int, services_id: int, data: dict) -> dict | None:
        rs = RentalServiceDAO.get_by_pk(rentals_id, services_id)
        if not rs:
            return None
        rs = RentalServiceDAO.update(rs,
            quantity=data["quantity"],
            fixed_price=data["fixed_price"],
        )
        return rs.to_dict()

    def delete(self, rentals_id: int, services_id: int) -> bool:
        rs = RentalServiceDAO.get_by_pk(rentals_id, services_id)
        if not rs:
            return False
        RentalServiceDAO.delete(rs)
        return True
