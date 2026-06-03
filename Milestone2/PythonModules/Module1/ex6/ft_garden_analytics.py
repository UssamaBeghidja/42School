#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self._height = 0.0
        self._age = 0
        self._stats: Plant.Stats = Plant.Stats()

        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = float(height)

        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("unknown plant", 0.0, 0)

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

    def grow(self) -> None:
        self._height += 8.0
        self._stats.add_grow()

    def age_one_day(self) -> None:
        self._age += 20
        self._stats.add_age()

    def show(self) -> None:
        self._stats.add_show()
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def display_stats(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self._bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def add_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f"{self._shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self._stats: Tree.Stats = Tree.Stats()

    def produce_shade(self) -> None:
        self._stats.add_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        self._height += 2.1
        self.nutritional_value += 1
        self._stats.add_grow()

    def age_one_day(self) -> None:
        self._age += 1
        self._stats.add_age()

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        seeds: int = 0
    ) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def grow(self) -> None:
        self._height += 30.0
        self._stats.add_grow()

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(
        f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}"
    )

    print("=== Flower")
    rose = Flower("rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_one_day()
    sunflower.bloom()
    sunflower.show()
    display_plant_statistics(sunflower)

    print("=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_plant_statistics(unknown)


if __name__ == "__main__":
    main()
