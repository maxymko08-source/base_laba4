from my_project import db
from my_project.rental.domain.location import Location


class LocationDAO:
    @staticmethod
    def get_all() -> list[Location]:
        return Location.query.all()

    @staticmethod
    def get_by_id(loc_id: int) -> Location | None:
        return Location.query.get(loc_id)

    @staticmethod
    def create(city: str, street_address: str) -> Location:
        loc = Location(city=city, street_address=street_address)
        db.session.add(loc)
        db.session.commit()
        return loc

    @staticmethod
    def update(loc: Location, city: str, street_address: str) -> Location:
        loc.city = city
        loc.street_address = street_address
        db.session.commit()
        return loc

    @staticmethod
    def delete(loc: Location) -> None:
        db.session.delete(loc)
        db.session.commit()
