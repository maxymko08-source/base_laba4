from my_project import db


class FineType(db.Model):
    __tablename__ = "fine_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    standard_amount = db.Column(db.Numeric(10, 2), nullable=True)

    fines = db.relationship("Fine", back_populates="fine_type", lazy=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "standard_amount": float(self.standard_amount) if self.standard_amount else None,
        }
