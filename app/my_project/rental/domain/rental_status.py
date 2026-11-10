from my_project import db


class RentalStatus(db.Model):
    __tablename__ = "rental_statuses"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(45), nullable=False)

    rentals = db.relationship("Rental", back_populates="status", lazy=True)

    def to_dict(self) -> dict:
        return {"id": self.id, "status_name": self.status_name}
