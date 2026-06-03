#!/usr/bin/env python3

import random


def gen_player_achievements(achievements):
    num_achievements = random.randint(4, 9)
    player_achievements = random.sample(achievements, num_achievements)
    return set(player_achievements)


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===\n")

    ACHIEVEMENTS = [
        "Crafting Genius",
        "World Savior",
        "Master Explorer",
        "Collector Supreme",
        "Untouchable",
        "Boss Slayer",
        "Strategist",
        "Unstoppable",
        "Speed Runner",
        "Survivor",
        "Treasure Hunter",
        "First Steps",
        "Sharp Mind",
        "Hidden Path Finder"
    ]

    players = {
        "Alice": gen_player_achievements(ACHIEVEMENTS),
        "Bob": gen_player_achievements(ACHIEVEMENTS),
        "Charlie": gen_player_achievements(ACHIEVEMENTS),
        "Dylan": gen_player_achievements(ACHIEVEMENTS)
    }

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}")
    print()
    all_achievements = set()
    for achievements in players.values():
        all_achievements = all_achievements.union(achievements)
    print(f"All distinct achievements: {all_achievements}\n")

    common = set(ACHIEVEMENTS)
    for achievements in players.values():
        common = common.intersection(achievements)
    print(f"Common achievements: {common}\n")

    for name, achievements in players.items():
        others = set()
        for other_name, other_achievements in players.items():
            if other_name != name:
                others = others.union(other_achievements)
        unique = achievements.difference(others)
        print(f"Only {name} has: {unique}")
    print()
    for name, achievements in players.items():
        missing = set(ACHIEVEMENTS).difference(achievements)
        print(f"{name} is missing: {missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
