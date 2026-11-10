from my_project import db
from my_project.rental.domain.user import User


class UserDAO:
    @staticmethod
    def get_all() -> list[User]:
        return User.query.all()

    @staticmethod
    def get_by_id(user_id: int) -> User | None:
        return User.query.get(user_id)

    @staticmethod
    def create(first_name: str, last_name: str, email: str,
               phone: str | None, driver_license: str | None) -> User:
        user = User(first_name=first_name, last_name=last_name,
                    email=email, phone=phone, driver_license=driver_license)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update(user: User, first_name: str, last_name: str, email: str,
               phone: str | None, driver_license: str | None) -> User:
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.phone = phone
        user.driver_license = driver_license
        db.session.commit()
        return user

    @staticmethod
    def delete(user: User) -> None:
        db.session.delete(user)
        db.session.commit()
