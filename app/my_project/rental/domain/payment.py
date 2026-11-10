from my_project import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    rentals_id = db.Column(db.Integer, db.ForeignKey("rentals.id"), nullable=False)

    rental = db.relationship("Rental", back_populates="payments")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "amount": float(self.amount),
            "payment_date": str(self.payment_date),
            "rentals_id": self.rentals_id,
        }
