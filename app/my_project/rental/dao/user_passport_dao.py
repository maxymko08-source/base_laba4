from my_project import db
from my_project.rental.domain.user_passport import UserPassport


class UserPassportDAO:
    @staticmethod
    def get_all() -> list[UserPassport]:
        return UserPassport.query.all()

    @staticmethod
    def get_by_id(passport_id: int) -> UserPassport | None:
        return UserPassport.query.get(passport_id)

    @staticmethod
    def get_by_user(user_id: int) -> list[UserPassport]:
        """1:M — passports for a user."""
        return UserPassport.query.filter_by(users_id=user_id).all()

    @staticmethod
    def create(passport_number: str, users_id: int) -> UserPassport:
        up = UserPassport(passport_number=passport_number, users_id=users_id)
        db.session.add(up)
        db.session.commit()
        return up

    @staticmethod
    def update(up: UserPassport, passport_number: str) -> UserPassport:
        up.passport_number = passport_number
        db.session.commit()
        return up

    @staticmethod
    def delete(up: UserPassport) -> None:
        db.session.delete(up)
        db.session.commit()
