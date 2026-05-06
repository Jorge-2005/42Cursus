from ex0 import FlameFactory, AquaFactory
from typing import Any

if __name__ == "__main__":

    flame = FlameFactory()
    aqua = AquaFactory()

    def testFactory(f_obj: Any) -> None:
        try:
            creature = f_obj.create_base()
            print(creature.describe())
            print(creature.attack())

            creature = f_obj.create_evolved()
            print(creature.describe())
            print(creature.attack())

        except Exception as e:
            print(e)

    def testFight(f_obj: Any, f_obj2: Any) -> None:
        try:
            creature = f_obj.create_base()
            creature2 = f_obj2.create_base()

            print(creature.describe())
            print("vs.")
            print(creature2.describe())
            print("fight!")
            print(creature.attack())
            print(creature2.attack())

        except Exception as e:
            print(e)

    print("Testing factory")
    testFactory(flame)
    print("\nTesting factory")
    testFactory(aqua)

    print("\nTesting battle")
    testFight(flame, aqua)
