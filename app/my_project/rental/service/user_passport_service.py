from my_project.rental.dao.user_passport_dao import UserPassportDAO


class UserPassportService:
    def get_all(self) -> list[dict]:
        return [up.to_dict() for up in UserPassportDAO.get_all()]

    def get_by_id(self, passport_id: int) -> dict | None:
        up = UserPassportDAO.get_by_id(passport_id)
        return up.to_dict() if up else None

    def get_by_user(self, user_id: int) -> list[dict]:
        return [up.to_dict() for up in UserPassportDAO.get_by_user(user_id)]

    def create(self, data: dict) -> dict:
        up = UserPassportDAO.create(
            passport_number=data["passport_number"],
            users_id=data["users_id"],
        )
        return up.to_dict()

    def update(self, passport_id: int, data: dict) -> dict | None:
        up = UserPassportDAO.get_by_id(passport_id)
        if not up:
            return None
        up = UserPassportDAO.update(up, passport_number=data["passport_number"])
        return up.to_dict()

    def delete(self, passport_id: int) -> bool:
        up = UserPassportDAO.get_by_id(passport_id)
        if not up:
            return False
        UserPassportDAO.delete(up)
        return True
