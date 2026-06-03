#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        try:
            coords = []
            for i, part in enumerate(parts):
                coords.append(float(part))
            return coords[0], coords[1], coords[2]
        except ValueError as e:
            print(f"Error on parameter '{parts[i]}': {e}")


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    x, y, z = pos1
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    dist_center = round(math.sqrt(x**2 + y**2 + z**2), 4)
    print(f"Distance to center: {dist_center}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    dist = round(math.sqrt((x2 - x)**2 + (y2 - y)**2 + (z2 - z)**2), 4)
    print(f"Distance between the 2 sets of coordinates: {dist}")


if __name__ == "__main__":
    main()
