def input_temperature(temp_str: str) -> int:
    number: int = int(temp_str)
    return number


def test_temperature() -> None:
    number = "25"
    print("=== Garden Temperature ===\n")
    print(f"Input data is '{number}'")
    print(f"Temperature is now {input_temperature(number)}°C\n")

    number = "abc"
    print(f"Input data is '{number}'")
    try:
        result = input_temperature(number)
        print(f"Temperature is now {result}°C\n")

    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    print("All tests completed - program didn't crash!")
