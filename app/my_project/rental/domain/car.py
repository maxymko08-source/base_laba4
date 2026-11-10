from my_project import db


class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    license_plate = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    car_models_id = db.Column(db.Integer, db.ForeignKey("car_models.id"), nullable=False)
    car_categories_id = db.Column(db.Integer, db.ForeignKey("car_categories.id"), nullable=False)
    locations_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)

    model = db.relationship("CarModel", back_populates="cars")
    category = db.relationship("CarCategory", back_populates="cars")
    location = db.relationship("Location", back_populates="cars")
    rentals = db.relationship("Rental", back_populates="car", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "license_plate": self.license_plate,
            "year": self.year,
            "car_models_id": self.car_models_id,
            "car_categories_id": self.car_categories_id,
            "locations_id": self.locations_id,
        }
