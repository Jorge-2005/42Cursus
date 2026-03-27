class Plant:
    def __init__(self, name, height: float, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def new_age(self) -> None:
        self.age += 1

    def get_info(self) -> None:
        print(f"Created: {self.name}: {self.height}cm, {self.age} days old")


plants = [
    Plant("Rose", 25.0, 30),
    Plant("Oak", 200.0, 365),
    Plant("Cactus", 5.0, 90),
    Plant("Sunflower", 80.0, 45),
    Plant("Fern", 15.0, 120)
    ]
print("=== Plant Factory Output ===")
for i in plants:
    i.get_info()
