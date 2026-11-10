from my_project.rental.dao.location_dao import LocationDAO


class LocationService:
    def get_all(self) -> list[dict]:
        return [l.to_dict() for l in LocationDAO.get_all()]

    def get_by_id(self, loc_id: int) -> dict | None:
        loc = LocationDAO.get_by_id(loc_id)
        return loc.to_dict() if loc else None

    def create(self, data: dict) -> dict:
        loc = LocationDAO.create(city=data["city"], street_address=data["street_address"])
        return loc.to_dict()

    def update(self, loc_id: int, data: dict) -> dict | None:
        loc = LocationDAO.get_by_id(loc_id)
        if not loc:
            return None
        loc = LocationDAO.update(loc, city=data["city"], street_address=data["street_address"])
        return loc.to_dict()

    def delete(self, loc_id: int) -> bool:
        loc = LocationDAO.get_by_id(loc_id)
        if not loc:
            return False
        LocationDAO.delete(loc)
        return True
