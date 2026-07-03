#!/usr/bin/env python3
"""
scope_mysteries.py

Exercise 2 - Memory Depths

Demonstrates closures and lexical scoping: functions that remember
variables from the environment in which they were created.
"""

from collections.abc import Callable


def mage_counter() -> Callable:
    """Return a closure that counts how many times it has been called."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a closure that accumulates power across calls."""
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies a fixed enchantment to any item."""

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a private store exposed only via store/recall closures."""
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
    """Demonstrate closures and lexical scoping."""
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print()
    print("Testing spell accumulator...")
    accumulate = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulate(20)}")
    print(f"Base 100, add 30: {accumulate(30)}")

    print()
    print("Testing enchantment factory...")
    flame_enchant = enchantment_factory("Flaming")
    frost_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(frost_enchant("Shield"))

    print()
    print("Testing memory vault...")
    vault = memory_vault()
    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
