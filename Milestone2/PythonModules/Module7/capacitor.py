#!/usr/bin/env python3

from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_heal_factory(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in [("base", factory.create_base()),
                            ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in [("base", factory.create_base()),
                            ("evolved", factory.create_evolved())]:
        print(f"{label}:")
        print(creature.describe())
        if isinstance(creature, TransformCapability):
            print(creature.attack())
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())


def main() -> None:
    test_heal_factory(HealingCreatureFactory())
    print()
    test_transform_factory(TransformCreatureFactory())


if __name__ == "__main__":
    main()
