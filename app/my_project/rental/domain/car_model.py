from my_project import db


class CarModel(db.Model):
    __tablename__ = "car_models"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_name = db.Column(db.String(45), nullable=False)
    car_brands_id = db.Column(db.Integer, db.ForeignKey("car_brands.id"), nullable=False)

    brand = db.relationship("CarBrand", back_populates="models")
    cars = db.relationship("Car", back_populates="model", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "model_name": self.model_name,
            "car_brands_id": self.car_brands_id,
        }
