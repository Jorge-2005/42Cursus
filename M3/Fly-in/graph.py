from zones import Zone, Connection
from error import Error


class Graph():
    """LOL"""
    def __init__(self) -> None:
        self.zones: dict[str, Zone] = {}
        self.connections: dict[str, list[Connection]] = {}

    def add_zone(self, new_zone: Zone) -> None:
        if new_zone.name in self.zones:
            raise Error("The zone already exist")

        self.zones[new_zone.name] = new_zone

    def get_zone(self, g_zone: str) -> Zone:
        if g_zone in self.zones:
            return self.zones[g_zone]
        else:
            raise Error("Zone not found")

    def add_connection(self, new_connect: Connection) -> None:
        if (new_connect.zone1.name not in self.zones or
                new_connect.zone2.name not in self.zones):
            raise Error("the zones doesn't exist")

        for i in self.connections[new_connect.zone1.name]:
            if ((new_connect.zone1.name == i.zone1.name and
                 new_connect.zone2.name == i.zone2.name) or
                (new_connect.zone1.name == i.zone2.name and
                    new_connect.zone2.name == i.zone1.name)):
                raise Error("The conexion already exist")

        """ tengo que comprobar sizone1 en el for existe, voy a preguntar si
            puedo try except antes"""

        if new_connect.zone1.name in self.connections:
            self.connections[new_connect.zone1.name].append(new_connect)
        else:
            self.connections[new_connect.zone1.name] = [new_connect]

        if new_connect.zone2.name in self.connections:
            self.connections[new_connect.zone2.name].append(new_connect)
        else:
            self.connections[new_connect.zone2.name] = [new_connect]

    def get_connection(self, connect1: str, connect2: str) -> Connection:
        if (connect1 not in self.connections or
                connect2 not in self.connections):
            raise Error("The zone is not conected")

        for i in self.connections[connect1]:
            if ((connect1 == i.zone1.name and connect2 == i.zone2.name) or
                    (connect1 == i.zone2.name and connect2 == i.zone1.name)):
                return i
        raise Error("The conexion doesn't exist")
