#!/usr/bin/env python3

from alchemy import potions, create_air
import elements


def lead_to_gold() -> str:
    air = create_air()
    potion = potions.strength_potion()
    fire = elements.create_fire()
    return (
        f"Recipe transmuting Lead to Gold: "
        f"brew '{air}' and '{potion}' mixed with '{fire}'"
    )
