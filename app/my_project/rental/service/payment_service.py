from my_project.rental.dao.payment_dao import PaymentDAO


class PaymentService:
    def get_all(self) -> list[dict]:
        return [p.to_dict() for p in PaymentDAO.get_all()]

    def get_by_id(self, pay_id: int) -> dict | None:
        p = PaymentDAO.get_by_id(pay_id)
        return p.to_dict() if p else None

    def get_by_rental(self, rental_id: int) -> list[dict]:
        return [p.to_dict() for p in PaymentDAO.get_by_rental(rental_id)]

    def create(self, data: dict) -> dict:
        p = PaymentDAO.create(
            amount=data["amount"],
            payment_date=data["payment_date"],
            rentals_id=data["rentals_id"],
        )
        return p.to_dict()

    def update(self, pay_id: int, data: dict) -> dict | None:
        p = PaymentDAO.get_by_id(pay_id)
        if not p:
            return None
        p = PaymentDAO.update(p,
            amount=data["amount"],
            payment_date=data["payment_date"],
            rentals_id=data["rentals_id"],
        )
        return p.to_dict()

    def delete(self, pay_id: int) -> bool:
        p = PaymentDAO.get_by_id(pay_id)
        if not p:
            return False
        PaymentDAO.delete(p)
        return True
