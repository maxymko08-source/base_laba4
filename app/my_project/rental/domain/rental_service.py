from my_project import db


class RentalService(db.Model):
    """M:M junction table between rentals and services."""
    __tablename__ = "rental_services"

    rentals_id = db.Column(db.Integer, db.ForeignKey("rentals.id"), primary_key=True)
    services_id = db.Column(db.Integer, db.ForeignKey("services.id"), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    fixed_price = db.Column(db.Numeric(10, 2), nullable=False)

    rental = db.relationship("Rental", back_populates="rental_services")
    service = db.relationship("Service", back_populates="rental_services")

    def to_dict(self) -> dict:
        return {
            "rentals_id": self.rentals_id,
            "services_id": self.services_id,
            "quantity": self.quantity,
            "fixed_price": float(self.fixed_price),
        }
