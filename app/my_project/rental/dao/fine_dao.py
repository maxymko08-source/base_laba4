from my_project import db
from my_project.rental.domain.fine import Fine


class FineDAO:
    @staticmethod
    def get_all() -> list[Fine]:
        return Fine.query.all()

    @staticmethod
    def get_by_id(fine_id: int) -> Fine | None:
        return Fine.query.get(fine_id)

    @staticmethod
    def get_by_rental(rental_id: int) -> list[Fine]:
        """1:M — all fines for a given rental."""
        return Fine.query.filter_by(rentals_id=rental_id).all()

    @staticmethod
    def create(issue_date, actual_amount, rentals_id: int, fine_types_id: int) -> Fine:
        fine = Fine(
            issue_date=issue_date,
            actual_amount=actual_amount,
            rentals_id=rentals_id,
            fine_types_id=fine_types_id,
        )
        db.session.add(fine)
        db.session.commit()
        return fine

    @staticmethod
    def update(fine: Fine, issue_date, actual_amount,
               rentals_id: int, fine_types_id: int) -> Fine:
        fine.issue_date = issue_date
        fine.actual_amount = actual_amount
        fine.rentals_id = rentals_id
        fine.fine_types_id = fine_types_id
        db.session.commit()
        return fine

    @staticmethod
    def delete(fine: Fine) -> None:
        db.session.delete(fine)
        db.session.commit()
