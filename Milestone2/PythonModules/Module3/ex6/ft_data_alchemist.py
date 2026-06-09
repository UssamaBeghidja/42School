#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john',
               'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    capital_all = [p.capitalize() for p in players]
    print(f"New list with all names capitalized: {capital_all}")

    capital_players = [p for p in players if p[0].isupper()]
    print(f"New list of capitalized names only: {capital_players}")

    scores = {p: random.randint(0, 1000) for p in capital_all}
    print(f"Score dict: {scores}")

    avg_score = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {avg_score}")

    high_scores = {k: v for k, v in scores.items() if v > avg_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
