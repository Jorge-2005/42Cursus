# Class Plant
class Plant:
    # Contructor de la clase Plant
    def __init__(self, name, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self.stats = self.Stats()

    # Clase anidada
    class Stats():
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0
            self.shade_calls = 0  # Solo se usará en Tree

        def display(self) -> None:
            print(f"Stats: {self.grow_calls} grow, "
                  f"{self.age_calls} age, {self.show_calls} show")

    # Metodos de la clase

    # Metodo estatico/ serian por ejemplo las --->
    # acciones de moverse en una clase heroe
    @staticmethod
    def check_age(age) -> None:
        if (age > 365):
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")

    # Metodo de clase, solo lo puede usar esa clase
    @classmethod
    def anonymous(cls) -> "Plant":  # al ponerlo entre "" le estas diciendo que
        # va a devolver un objeto de una clase llamada Plant pero qeu todavia
        # no esta definida ya que el metodo de clase esat dentro de ella
        return cls("Unknown plant", 0, 0)

    # Metodo normal
    def age(self, new_age) -> None:
        if (new_age > 0):
            self._age = new_age
            self.stats.age_calls += 1
        else:
            print("Invalid age value")

    def grow(self, new_height) -> None:
        if (new_height > 0):
            self._height = new_height
            self.stats.grow_calls += 1
        else:
            print("Invalid height value")

    def show(self) -> None:
        self.stats.show_calls += 1
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
            self.has_bloomed = True
            return True
        else:
            return False

    def age(self, new_age) -> None:
        super().age(new_age)

    def grow(self, new_height) -> None:
        super().grow(new_height)

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if (self.has_bloomed is True):
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")


# Class Tree
class Tree(Plant):
    def __init__(self,
                 name, height: float, age: int, trunc_diameter: float) -> None:
        self.trunc_diameter = trunc_diameter
        # Con el super() llammamos al constructor del padre
        super().__init__(name, height, age)

    def produce_shade(self) -> None:
        self.stats.shade_calls += 1
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade "
              f"of {self._height:.1f}cm "
              f"long and {self.trunc_diameter:.1f}cm wide.")

    def age(self, new_age) -> None:
        super().age(new_age)

    def grow(self, new_height) -> None:
        super().grow(new_height)

    def display(self) -> None:
        self.stats.display()
        print(f" {self.stats.shade_calls} shade")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunc_diameter:.1f}cm")


# Class Flower
class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        # mirar si tengo que poner un nuevo atributo
        # o si tengo que usar un constructor para esta clase, creo que si
        self.seeds = 0
        super().__init__(name, height, age, color)
        # tambien mirar por que puedo usar la variable de abajo, aunque creo
        # que es por que la heredo de Flower

    def bloom(self) -> bool:
        res = super().bloom()
        if (res is True):
            self.seeds = 42
            return True
        else:
            return False

    def age(self, new_age) -> None:
        super().age(new_age)

    def grow(self, new_height) -> None:
        super().grow(new_height)

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


flower = Flower("Rose", 15, 10, "red")
tree = Tree("Oak", 200, 365, 5)
seed = Seed("Sunflower", 80, 45, "yellow")
p_anonimous = Plant.anonymous()


print("=== Garden Plant Types ===")
print("=== Check year-old")
Plant.check_age(30)
Plant.check_age(400)
print("")


print("=== Flower")
flower.show()
print(f"[statistics for {flower._name}]")
flower.stats.display()
print(f"[asking the {flower._name} to grow and bloom]")
flower.grow(23)
flower.bloom()
flower.show()
print(f"[statistics for {flower._name}]")
flower.stats.display()
print("")


print("=== Tree")
tree.show()
print(f"[statistics for {tree._name}]")
tree.display()
tree.produce_shade()
print(f"[statistics for {tree._name}]")
tree.display()
print("")


print("=== Seed")
seed.show()
print(f"[make {seed._name} grow, age and bloom]")
seed.grow(110)
seed.age(65)
seed.bloom()
seed.show()
print(f"[statistics for {seed._name}]")
seed.stats.display()
# estadisticas
print("")
print("=== Anonimous")
p_anonimous.show()
print(f"[statistics for {p_anonimous._name}]")
p_anonimous.stats.display()
