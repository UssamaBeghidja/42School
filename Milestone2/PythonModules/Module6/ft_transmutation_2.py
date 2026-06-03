#!/usr/bin/env python3

import alchemy


def main() -> None:
    gold_recipe = alchemy.transmutation.recipes.lead_to_gold()
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    print(f"Testing gold_recipe: {gold_recipe}")


if __name__ == "__main__":
    main()
