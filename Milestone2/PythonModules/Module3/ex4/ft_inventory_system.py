#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    args = sys.argv[1:]
    inventory = {}
    for arg in args:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter: '{arg}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
    print(inventory)
    print(f"Total items: {len(inventory)}")
    print(f"Total quantity of the 5 items: {sum(inventory.values())}")
    total = sum(inventory.values())
    for item in inventory:
        pct = round((inventory[item] / total) * 100, 1)
        print(f"Item {item} represents: {pct}%")
    most = max(inventory, key=inventory.get)
    print(f"The most abundant: {most} with quantity {inventory[most]}")
    least = min(inventory, key=inventory.get)
    print(f"The least abundant: {least} with quantity {inventory[least]}")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
