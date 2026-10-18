from zones import Zone


class Graph():
    """LOL"""
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}

    def add_zone(self, new_zone: Zone) -> None:
        if new_zone.name in self.zones:
            raise Exception  # tengo que crear mi excepcion
        else:
            self.zones[new_zone.name] = new_zone

    def get_zone(self, g_zone: str) -> Zone:
        if g_zone in self.zones:
            return self.zones[g_zone]
        else:
            raise Exception  # tengo que crear mi exception
