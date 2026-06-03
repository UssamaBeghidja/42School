#!/usr/bin/env python3


def input_temperature(value: str) -> int:
    temperature = int(value)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]

    for value in test_values:
        print(f"Input data is'{value}'")
        try:
            temp = input_temperature(value)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
