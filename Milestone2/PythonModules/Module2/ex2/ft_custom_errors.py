#!/usr/bin/env python3


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "plant" + 5


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    operation_number = 0
    while operation_number <= 4:
        print(f"Testing operation {operation_number}...")
        try:
            garden_operations(operation_number)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        operation_number += 1

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
