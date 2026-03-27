# Class Plant
class Plant:
    # Contructor de la clase Plant
    def __init__(self, name, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age

    # Metodos de la clase
    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, {self._age} days old")


# Class Flower
class Flower(Plant):
    def __init__(self, name, height: float, age: int, color) -> None:
        self.color = color
        self.has_bloomed = False  # variable para saber si ya ha florecido o no
        # Con el super() llammamos al constructor del padre
        super().__init__(name, height, age)

    def bloom(self) -> bool:
        if (not self.has_bloomed):
            print("[asking the rose to bloom]")
            self.has_bloomed = True
            return True
        else:
            return False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.has_bloomed is True):
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")


# Class Tree
class Tree(Plant):
    def __init__(self,
                 name, height: float, age: int, trunc_diameter: float) -> None:
        self.trunc_diameter = trunc_diameter
        # Con el super() llammamos al constructor del padre
        super().__init__(name, height, age)

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade "
              f"of {self._height:.1f}cm "
              f"long and {self.trunc_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunc_diameter:.1f}cm")


# Class Vegetable
class Vegetable(Plant):
    def __init__(self, name, height: float,
                 age: int, harvest_season, nutritional_value):
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        super().__init__(name, height, age)

    def age(self, new_age) -> None:
        if (new_age > 0):
            self._age = new_age
            self.nutritional_value += 10
        else:
            print("Invalid age value")

    def grow(self, new_height) -> None:
        if (new_height > 0):
            self._height = new_height
            self.nutritional_value += 10
        else:
            print("Invalid height value")

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


flower = Flower("Rose", 15, 10, "red")
tree = Tree("Oak", 200, 365, 5)
vegetable = Vegetable("Tomato", 5, 10, "April", 0)
print("=== Garden Plant Types ===")
print("=== Flower")
flower.show()
flower.bloom()
flower.show()
print("")
print("=== Tree")
tree.show()
tree.produce_shade()
print("")
print("=== Vegetable")
vegetable.show()
print("[make tomato grow and age for 20 days]")
vegetable.grow(47)
vegetable.age(30)
vegetable.show()
