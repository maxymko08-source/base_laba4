from my_project import db


class Fine(db.Model):
    __tablename__ = "fines"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    issue_date = db.Column(db.DateTime, nullable=False)
    actual_amount = db.Column(db.Numeric(10, 2), nullable=False)
    rentals_id = db.Column(db.Integer, db.ForeignKey("rentals.id"), nullable=False)
    fine_types_id = db.Column(db.Integer, db.ForeignKey("fine_types.id"), nullable=False)

    rental = db.relationship("Rental", back_populates="fines")
    fine_type = db.relationship("FineType", back_populates="fines")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "issue_date": str(self.issue_date),
            "actual_amount": float(self.actual_amount),
            "rentals_id": self.rentals_id,
            "fine_types_id": self.fine_types_id,
        }
