from my_project.rental.dao.user_dao import UserDAO


class UserService:
    def get_all(self) -> list[dict]:
        return [u.to_dict() for u in UserDAO.get_all()]

    def get_by_id(self, user_id: int) -> dict | None:
        u = UserDAO.get_by_id(user_id)
        return u.to_dict() if u else None

    def create(self, data: dict) -> dict:
        u = UserDAO.create(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data.get("phone"),
            driver_license=data.get("driver_license"),
        )
        return u.to_dict()

    def update(self, user_id: int, data: dict) -> dict | None:
        u = UserDAO.get_by_id(user_id)
        if not u:
            return None
        u = UserDAO.update(u,
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone=data.get("phone"),
            driver_license=data.get("driver_license"),
        )
        return u.to_dict()

    def delete(self, user_id: int) -> bool:
        u = UserDAO.get_by_id(user_id)
        if not u:
            return False
        UserDAO.delete(u)
        return True
