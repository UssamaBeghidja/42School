#!/usr/bin/env python3

import alchemy.transmutation.recipes


def main() -> None:
    gold_recipe = alchemy.transmutation.recipes.lead_to_gold()
    print("=== Transmutation 0 ===")
    print("Using: 'import alchemy' structure to access recipes")
    print(f"Testing gold_recipe: {gold_recipe}")


if __name__ == "__main__":
    main()
