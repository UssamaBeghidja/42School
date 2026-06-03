#!/usr/bin/env python3

from alchemy.transmutation import recipes


def main() -> None:
    gold_recipe = recipes.lead_to_gold()
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    print("Using: 'from alchemy.transmutation import recipes'"
          " structure to access recipes")
    print(f"Testing gold_recipe: {gold_recipe}")


if __name__ == "__main__":
    main()
