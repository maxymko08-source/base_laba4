from my_project import db


class UserPassport(db.Model):
    __tablename__ = "user_passports"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    passport_number = db.Column(db.String(20), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="passports")

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "passport_number": self.passport_number,
            "users_id": self.users_id,
        }
