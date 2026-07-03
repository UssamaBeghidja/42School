#!/usr/bin/env python3
"""
lambda_spells.py

Exercise 0 - Lambda Sanctum

Demonstrates lambda expressions for artifact sorting, mage filtering,
spell name transformation, and mage power statistics.
"""


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort magical artifacts by power level, descending."""
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return only the mages whose power is at least min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name with a '* ' prefix and ' *' suffix."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """Compute max, min, and average power across a list of mages."""
    strongest = max(mages, key=lambda mage: mage["power"])
    weakest = min(mages, key=lambda mage: mage["power"])
    average = sum(map(lambda mage: mage["power"], mages)) / len(mages)
    return {
        "max_power": strongest["power"],
        "min_power": weakest["power"],
        "avg_power": round(average, 2),
    }


def main() -> None:
    """Demonstrate lambda-based artifact and mage utilities."""
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Shadow Cloak", "power": 60, "type": "armor"},
    ]
    mages = [
        {"name": "Alex", "power": 75, "element": "fire"},
        {"name": "Jordan", "power": 40, "element": "water"},
        {"name": "Riley", "power": 90, "element": "earth"},
    ]
    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    first, second = sorted_artifacts[0], sorted_artifacts[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print()
    print("Testing power filter...")
    strong_mages = power_filter(mages, 70)
    names = [mage["name"] for mage in strong_mages]
    print(f"Mages with power >= 70: {names}")

    print()
    print("Testing spell transformer...")
    print(" ".join(spell_transformer(spells)))

    print()
    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
