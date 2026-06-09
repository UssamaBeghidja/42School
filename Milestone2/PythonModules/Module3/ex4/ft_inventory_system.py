#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    inventory: dict[str, int] = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    print(f"Total quantity of the {len(inventory)} items: "
          f"{sum(inventory.values())}")

    total = sum(inventory.values())
    for item in inventory:
        pct = round((inventory[item] / total) * 100, 1)
        print(f"Item {item} represents {pct}%")

    most = max(inventory, key=lambda k: inventory[k])
    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    least = min(inventory, key=lambda k: inventory[k])
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
