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
        self.connections[new_zone.name] = []

    def get_zone(self, g_zone: str) -> Zone:
        if g_zone in self.zones:
            return self.zones[g_zone]
        else:
            raise Error("Zone not found")

    def add_connection(self, new_connect: Connection) -> None:
        if (new_connect.zone1.name not in self.zones or
                new_connect.zone2.name not in self.zones):
            raise Error("The zones doesn't exist")

        if new_connect.zone1.name == new_connect.zone2.name:
            raise Error("A zone can't connect to itself")

        for i in self.connections[new_connect.zone1.name]:
            if ({new_connect.zone1.name, new_connect.zone2.name} ==
                    {i.zone2.name, i.zone1.name}):
                raise Error("the connection already exist")

        self.connections[new_connect.zone1.name].append(new_connect)
        self.connections[new_connect.zone2.name].append(new_connect)

    def get_connection(self, connect1: str, connect2: str) -> Connection:
        if (connect1 not in self.connections or
                connect2 not in self.connections):
            raise Error("The zone doesn't exist")

        for i in self.connections[connect1]:
            if ({connect1, connect2} == {i.zone2.name, i.zone1.name}):
                return i
        raise Error("The conexion doesn't exist")
