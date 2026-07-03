#!/usr/bin/env python3
"""
functools_artifacts.py

Exercise 3 - Ancient Library

Demonstrates functools treasures: reduce, partial, lru_cache, and
singledispatch.
"""

import operator
from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any

_OPERATIONS: dict[str, Callable[[int, int], int]] = {
    "add": operator.add,
    "multiply": operator.mul,
    "max": max,
    "min": min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combine spell powers with functools.reduce."""
    if not spells:
        return 0
    if operation not in _OPERATIONS:
        raise ValueError(f"Unknown operation: {operation}")
    return reduce(_OPERATIONS[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create three element-specialized enchantments via functools.partial.

    base_enchantment signature: (power: int, element: str,
    target: str) -> str
    """
    return {
        "fire": partial(base_enchantment, power=50, element="fire"),
        "water": partial(base_enchantment, power=50, element="water"),
        "earth": partial(base_enchantment, power=50, element="earth"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, memoized with lru_cache."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Build a singledispatch spell system for int/str/list inputs."""

    @singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def cast_int(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register
    def cast_str(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register
    def cast_list(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


def main() -> None:
    """Demonstrate functools artifacts."""
    spells = [10, 20, 30, 40]

    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print()
    print("Testing partial enchanter...")

    def enchant(power: int, element: str, target: str) -> str:
        return f"{element.title()} enchantment ({power}) on {target}"

    enchantments = partial_enchanter(enchant)
    print(enchantments["fire"](target="Sword"))
    print(enchantments["water"](target="Shield"))

    print()
    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(memoized_fibonacci.cache_info())

    print()
    print("Testing spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast([1, 2, 3]))
    print(cast(3.14))


if __name__ == "__main__":
    main()
