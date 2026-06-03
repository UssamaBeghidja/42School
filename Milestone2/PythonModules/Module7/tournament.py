#!/usr/bin/env python3

from ex2.strategy import (
    BattleStrategy, NormalStrategy, DefensiveStrategy, AggressiveStrategy
)
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            c1 = factory1.create_base()
            c2 = factory2.create_base()
            print("* Battle *")
            print(c1.describe())
            print("vs.")
            print(c2.describe())
            print("now fight!")
            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    # create factories
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()
    # create strategies
    normal_strategy = NormalStrategy()
    defensive_strategy = DefensiveStrategy()
    aggressive_strategy = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_factory, normal_strategy),
        (healing_factory, defensive_strategy)
    ])

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Normal) ]")
    battle([
        (flame_factory, aggressive_strategy),
        (healing_factory, normal_strategy)
    ])

    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), "
          "(Transform+Aggressive) ]")
    battle([
        (aqua_factory, normal_strategy),
        (healing_factory, defensive_strategy),
        (transform_factory, aggressive_strategy)
    ])


if __name__ == "__main__":
    main()
