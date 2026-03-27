def input_temperature(temp_str: str) -> int:
    number: int = int(temp_str)
    if number >= 0 and number <= 40:
        return number
    elif (number < 0):
        raise Exception(f"Caught input_temperature error: {number}°C is "
              "too cold for plants (min 0°C)\n")
    elif (number > 40):
        raise Exception
    return 0


def test_temperature() -> None:
    number = "25"
    print("=== Garden Temperature Checker ===\n")
    print(f"Input data is '{number}'")
    print(f"Temperature is now {input_temperature(number)}°C\n")

    number = "abc"
    print(f"Input data is '{number}'")
    try:
        result = input_temperature(number)
        print(f"Temperature is now {result}°C\n")

    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")

    try:
        number = "100"
        print(f"Input data is '{number}'")
        result = input_temperature(number)

    except Exception:
        print(f"Caught input_temperature error: {number}°C is "
              "too hot for plants (max 40°C)\n")

    try:
        number = "-50"
        print(f"Input data is '{number}'")
        result = input_temperature(number)

    except Exception as e:
        print(f"{e}")
    print("All tests completed - program didn't crash!")


test_temperature()
