from enum import Enum


class ZoneTypes(Enum):
    """Types for the zones"""
    NORMAL = "normal"
    BLOCKED = "blocked"
    RESTRICTED = "restricted"
    PRIORITY = "priority"


class Zone():
    """Values for the zones"""

    def __init__(self, name: str, x: int, y: int,
                 zone_type: ZoneTypes = ZoneTypes.NORMAL,
                 color: str = "none",
                 max_drones: int = 1,
                 start_hub: bool = False,
                 end_hub: bool = False):

        self.name = name
        self.x = x
        self.y = y
        self.zone_type = zone_type
        self.color = color
        self.max_drones = max_drones
        self.start_hub = start_hub
        self.end_hub = end_hub


"""Mirar si tengo que poner una funcion para imprimir valores"""


class Connection():
    """Save the zones that are conected"""

    def __init__(self, zone1: Zone, zone2: Zone, max_link_capacity: int = 1):
        self.zone1 = zone1
        self.zone2 = zone2
        self.max_link_capacity = max_link_capacity
