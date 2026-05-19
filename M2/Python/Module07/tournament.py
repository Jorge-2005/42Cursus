from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategy import (NormalStrategy, AggressiveStrategy,
                          DefensiveStrategy, StrategyError)


def battle(opponents: list[tuple]) -> None:

    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):

            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")

            print(creature1.describe())
            print(" vs.")
            print(creature2.describe())
            print(" now fight!")

            try:
                strategy1.act(creature1)
                strategy2.act(creature2)

            except StrategyError as e:
                print(e)


if __name__ == "__main__":

    flame = FlameFactory()
    aqua = AquaFactory()
    healing = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")

    battle([
        (flame, normal),
        (healing, defensive)
    ])

    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")

    battle([
        (flame, aggressive),
        (healing, defensive)
    ])

    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")

    battle([
        (aqua, normal),
        (healing, defensive),
        (transform, aggressive)
    ])
