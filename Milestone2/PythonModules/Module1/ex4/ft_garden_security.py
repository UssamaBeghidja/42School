#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_height: float) -> bool:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = float(new_height)
        return True

    def set_age(self, new_age: int) -> bool:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = new_age
        return True

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant.show()

    if plant.set_height(25):
        print("Height updated: 25cm")
    else:
        print("Height update rejected")

    if plant.set_age(30):
        print("Age updated: 30 days")
    else:
        print("Age update rejected")

    if plant.set_height(-5):
        print("Height updated")
    else:
        print("Height update rejected")

    if plant.set_age(-2):
        print("Age updated")
    else:
        print("Age update rejected")

    print("Current state:", end=" ")
    plant.show()


if __name__ == "__main__":
    main()
