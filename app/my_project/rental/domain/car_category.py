from my_project import db


class CarCategory(db.Model):
    __tablename__ = "car_categories"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(45), nullable=False)
    daily_price = db.Column(db.Integer, nullable=False)

    cars = db.relationship("Car", back_populates="category", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "category_name": self.category_name,
            "daily_price": self.daily_price,
        }
