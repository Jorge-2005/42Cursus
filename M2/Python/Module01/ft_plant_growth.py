class Plant:
    def __init__(self, name, height, age) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, heights) -> None:
        self.height += heights

    def new_age(self, ages) -> None:
        self.age += ages

    def get_info(self):
        print(self.name + ":", self.height, "cm,", self.age, "days old")


plant = Plant("Rose", 25, 30)
print("=== Day 1 ===")
plant.get_info()
print("=== Day 7 ===")
plant.grow(6)
plant.new_age(6)
plant.get_info()
print("Growth this week: +6cm")
