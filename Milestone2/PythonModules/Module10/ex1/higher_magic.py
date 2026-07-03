#!/usr/bin/env python3
"""
higher_magic.py

Exercise 1 - Higher Realm

Demonstrates higher-order functions: functions that accept and/or
return other spell functions.

Every spell follows the same contract:
    def spell(target: str, power: int) -> str
"""

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Combine two spells into one that casts both and returns a tuple."""

    def combined(target: str, power: int) -> tuple:
        return spell1(target, power), spell2(target, power)

    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a spell that multiplies power before casting."""

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts when condition(target, power)."""

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts every spell in order."""

    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]

    return sequence


def main() -> None:
    """Demonstrate higher-order spell functions."""

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target}"

    def heal(target: str, power: int) -> str:
        return f"Heals {target}"

    def power_echo(target: str, power: int) -> str:
        return str(power)

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    hit, healed = combined("Dragon", 20)
    print(f"Combined spell result: {hit}, {healed}")

    print()
    print("Testing power amplifier...")
    mega_echo = power_amplifier(power_echo, 3)
    original = 10
    print(f"Original: {original}, Amplified: {mega_echo('Dragon', 10)}")

    print()
    print("Testing conditional caster...")
    guarded = conditional_caster(lambda t, p: p >= 15, fireball)
    print(guarded("Dragon", 20))
    print(guarded("Dragon", 5))

    print()
    print("Testing spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence("Dragon", 20))

    print()
    print("Is fireball callable?", callable(fireball))


if __name__ == "__main__":
    main()
