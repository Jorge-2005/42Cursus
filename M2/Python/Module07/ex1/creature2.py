from .capability import HealCapability
from .capability import TransformCapability
from ex0.creature import Creature


class Sproutling(Creature, HealCapability):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def heal(self) -> str:
        return ("Sproutling Heal")

    def attack(self) -> str:
        return (f"{self.name} uses Vine Whip!")


class Bloomelle(Creature, HealCapability):

    def __init__(self, name: str, type: str) -> None:
        super().__init__(name, type)

    def heal(self) -> str:
        return ("Bloomelle Heal")

    def attack(self) -> str:
        return (f"{self.name} uses Petal Dance!")


# ee si/ espaciar locura
class Shiftling(Creature, TransformCapability):

    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} attacks normally")

    def transform(self) -> str:
        return ("Shiftling shifts into a sharper form!")

    def revert(self) -> str:
        return ("Shiftling returns to normal.")


class Morphagon(Creature, TransformCapability):

    def __init__(self, name: str, type: str):
        super().__init__(name, type)

    def attack(self) -> str:
        return (f"{self.name} attacks normally")

    def transform(self) -> str:
        return ("Morphagon morphs into a dragonic battle form!")

    def revert(self) -> str:
        return ("Morphagon stabilizes its form.")
