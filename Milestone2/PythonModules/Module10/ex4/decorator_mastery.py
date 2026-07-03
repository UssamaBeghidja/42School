#!/usr/bin/env python3
"""
decorator_mastery.py

Exercise 4 - Master's Tower

Demonstrates decorator mastery: timing, parameterized validation,
retry logic, and staticmethod usage within a class.
"""

import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that prints how long a spell took to cast."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that enforces a minimum power requirement.

    Assumes the decorated callable receives 'power' either as the
    keyword argument 'power' or as its last positional argument.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            power = kwargs.get("power", args[-1] if args else 0)
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a failing spell up to N times."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts:
                        break
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Demonstrates staticmethod alongside a power-validated method."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name is at least 3 letters/spaces long."""
        return len(name) >= 3 and all(
            char.isalpha() or char.isspace() for char in name
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if the caster has enough power."""
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    """Demonstrate decorator mastery."""
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str, power: int) -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball("Dragon", 20)
    print(f"Result: {result}")

    print()
    print("Testing retrying spell...")

    @retry_spell(3)
    def cursed_spell(target: str, power: int) -> str:
        raise RuntimeError("The spell always fizzles")

    print(cursed_spell("Golem", 10))

    @retry_spell(3)
    def victory_spell(target: str, power: int) -> str:
        return "Waaaaaaagh spelled !"

    print(victory_spell("Golem", 10))

    print()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
