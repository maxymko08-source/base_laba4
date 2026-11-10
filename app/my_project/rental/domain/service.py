from my_project import db


class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    services_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    rental_services = db.relationship("RentalService", back_populates="service", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "services_name": self.services_name,
            "price": float(self.price),
        }
