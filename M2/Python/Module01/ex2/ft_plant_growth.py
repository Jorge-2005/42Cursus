class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        self.height += 1

    def new_age(self) -> None:
        self.age += 1

    def get_info(self):
        print(self.name + ":", self.height, "cm,", self.age, "days old")


plant = Plant("Rose", 25, 30)
for i in range(1, 8):
    print(f"=== Day {i} ===")
    plant.get_info()
    plant.grow()
    plant.new_age()
i -= 1
print(f"Growth this week: +{i}cm")
