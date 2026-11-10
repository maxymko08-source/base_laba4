from my_project import db


class Location(db.Model):
    __tablename__ = "locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city = db.Column(db.String(45), nullable=False)
    street_address = db.Column(db.String(100), nullable=False)

    cars = db.relationship("Car", back_populates="location", lazy=True)
    pickup_rentals = db.relationship(
        "Rental", foreign_keys="Rental.pickup_location_id",
        back_populates="pickup_location", lazy=True
    )
    dropoff_rentals = db.relationship(
        "Rental", foreign_keys="Rental.dropoff_location_id",
        back_populates="dropoff_location", lazy=True
    )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "city": self.city,
            "street_address": self.street_address,
        }
