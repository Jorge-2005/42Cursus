class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)

    @classmethod
    def type_plant(cls, plant: str) -> None:
        if (plant != "tomato"):
            raise PlantError("The tomato plant is wilting!")

    @classmethod
    def watering(cls, water: int) -> None:
        if (water < 5):
            raise WaterError("Not enough water in the tank!")


class PlantError(GardenError):
    @classmethod
    def type_plant(cls, plant: str) -> None:
        super().type_plant(plant)


class WaterError(GardenError):
    @classmethod
    def watering(cls, water: int) -> None:
        super().watering(water)


print("=== Custom Garden Errors Demo ===\n")
try:
    print("Testing PlantError...")
    PlantError.type_plant("potato")

except PlantError as e:
    print(f"Caught PlantError: {e}\n")

try:
    print("Testing WaterError...")
    WaterError.watering(2)

except WaterError as e:
    print(f"Caught WaterError: {e}\n")
print("Testing catching all garden errors...")
for i in range(2):
    try:
        if i == 0:
            GardenError.type_plant("potato")
        else:
            GardenError.watering(2)

    except GardenError as e:
        print(f"Caught GardenError: {e}")
print("\nAll custom error types work correctly!")
