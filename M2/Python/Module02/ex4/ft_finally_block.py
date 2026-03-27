def water_plant(plant_name: str) -> None:
    if (plant_name == plant_name.capitalize()):
        print(f"Watering {plant_name}: [OK]")
    else:
        PlantError.error(plant_name)


class PlantError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def error(cls, plantName: str) -> None:
        raise PlantError(f"Invalid plant name to water: '{plantName}'")


print("=== Garden Watering System ===\n")
print("Testing valid plants...")


def test_watering_system() -> None:
    try:
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print("Closing watering system\n")
    try:
        print("Testing invalid plants...")
        print("Opening watering system")
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    finally:
        print(".. ending tests and returning to main")


test_watering_system()
print("Closing watering system\n")
print("Cleanup always happens, even with errors!")
