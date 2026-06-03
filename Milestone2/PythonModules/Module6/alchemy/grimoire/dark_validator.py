#!/usr/bin/env python3

from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    for item in allowed:
        if item.lower() not in ingredients.lower():
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
