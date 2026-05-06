from ..elements import create_air
import elements
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (f"Recipe transmuting Lead to Gold: brew '{create_air()}' "
            f"and '{strength_potion()}'"
            f"mixed with '{elements.create_fire()}'")
