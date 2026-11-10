from my_project import db
from my_project.rental.domain.payment import Payment


class PaymentDAO:
    @staticmethod
    def get_all() -> list[Payment]:
        return Payment.query.all()

    @staticmethod
    def get_by_id(pay_id: int) -> Payment | None:
        return Payment.query.get(pay_id)

    @staticmethod
    def get_by_rental(rental_id: int) -> list[Payment]:
        """1:M — all payments for a given rental."""
        return Payment.query.filter_by(rentals_id=rental_id).all()

    @staticmethod
    def create(amount, payment_date, rentals_id: int) -> Payment:
        payment = Payment(amount=amount, payment_date=payment_date,
                          rentals_id=rentals_id)
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def update(payment: Payment, amount, payment_date, rentals_id: int) -> Payment:
        payment.amount = amount
        payment.payment_date = payment_date
        payment.rentals_id = rentals_id
        db.session.commit()
        return payment

    @staticmethod
    def delete(payment: Payment) -> None:
        db.session.delete(payment)
        db.session.commit()
