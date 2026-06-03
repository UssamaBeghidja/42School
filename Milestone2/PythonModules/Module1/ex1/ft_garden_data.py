#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Registry ===")

    plants = [
        Plant("rose", 25, 30),
        Plant("sunflower", 80, 45),
        Plant("cactus", 15, 120),
    ]

    for plant in plants:
        plant.show()


if __name__ == "__main__":
    main()
