from abc import ABC, abstractmethod


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature) -> None:
        pass


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return True

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Invalid creature for NormalStrategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "transform") and hasattr(creature, "revert")

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Creature cannot use AggressiveStrategy")
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature) -> bool:
        return hasattr(creature, "heal")

    def act(self, creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError("Creature cannot use DefensiveStrategy")
        print(creature.attack())
        print(creature.heal())