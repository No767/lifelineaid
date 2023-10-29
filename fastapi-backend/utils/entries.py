from shapely.wkt import loads

from .structs import PinDict


class PinInfo:
    __slots__ = ("point", "title", "description")

    def __init__(self, entry: PinDict):
        self.point = entry["point"]
        self.title = entry["title"]
        self.description = entry["description"]

    def to_dict(self):
        parsed_point = loads(self.point)
        return {
            "point": (parsed_point.x, parsed_point.y),
            "title": self.title,
            "description": self.description,
        }
