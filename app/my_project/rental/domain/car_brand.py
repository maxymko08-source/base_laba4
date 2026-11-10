from my_project import db


class CarBrand(db.Model):
    __tablename__ = "car_brands"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    brand_name = db.Column(db.String(45), nullable=False)

    # relationships
    models = db.relationship("CarModel", back_populates="brand", lazy=True)

    def to_dict(self) -> dict:
        return {"id": self.id, "brand_name": self.brand_name}
