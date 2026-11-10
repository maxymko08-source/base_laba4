from my_project import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(45), nullable=False)
    last_name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    driver_license = db.Column(db.String(50), nullable=True)

    rentals = db.relationship("Rental", back_populates="user", lazy=True)
    passports = db.relationship("UserPassport", back_populates="user", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "driver_license": self.driver_license,
        }
