class Plant:
    def __init__(self, name, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    def set_age(self, new_age) -> None:
        if (new_age > self._age):
            self._age = new_age
            print(f"Age updated: {new_age} days")
        elif (new_age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def set_height(self, new_height) -> None:
        if (new_height > self._height):
            self._height = new_height
            print(f"Height updated: {new_height}cm")
        elif (new_height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> float:
        return self._height

    def get_info(self) -> None:
        print("Current state" +
              f": {self._name}: {self._height:.1f}cm, {self._age} days old")


plant = Plant("Rose", 15.0, 10)
print("=== Plant Factory Output ===")
plant.get_info()
print("")
plant.set_height(25)
plant.set_age(30)
print("")
plant.set_height(-3)
plant.set_age(-6)
print("")
plant.get_info()
