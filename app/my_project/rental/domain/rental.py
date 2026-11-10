from my_project import db


class Rental(db.Model):
    __tablename__ = "rentals"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cars_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    rental_statuses_id = db.Column(db.Integer, db.ForeignKey("rental_statuses.id"), nullable=False)
    pickup_location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    dropoff_location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    user = db.relationship("User", back_populates="rentals")
    car = db.relationship("Car", back_populates="rentals")
    status = db.relationship("RentalStatus", back_populates="rentals")
    pickup_location = db.relationship(
        "Location", foreign_keys=[pickup_location_id],
        back_populates="pickup_rentals"
    )
    dropoff_location = db.relationship(
        "Location", foreign_keys=[dropoff_location_id],
        back_populates="dropoff_rentals"
    )
    fines = db.relationship("Fine", back_populates="rental", lazy=True)
    payments = db.relationship("Payment", back_populates="rental", lazy=True)
    rental_services = db.relationship("RentalService", back_populates="rental", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "start_date": str(self.start_date),
            "end_date": str(self.end_date),
            "users_id": self.users_id,
            "cars_id": self.cars_id,
            "rental_statuses_id": self.rental_statuses_id,
            "pickup_location_id": self.pickup_location_id,
            "dropoff_location_id": self.dropoff_location_id,
        }
