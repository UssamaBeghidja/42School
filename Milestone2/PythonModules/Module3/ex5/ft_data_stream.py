#!/usr/bin/env python3

import random


def gen_event() -> tuple[str, str]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "use"]
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(events) -> tuple[str, str]:
    while events:
        idx = random.randint(0, len(events) - 1)
        event = events.pop(idx)
        yield event


def main() -> None:
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    fresh_gen = gen_event()
    event = [next(fresh_gen) for i in range(10)]
    print(f"Built list of 10 events: {event}")
    remaining_events = consume_event(event)
    for e in remaining_events:
        print(f"Got event from list: {e}")
        print(f"Remaining in list: {event}")


if __name__ == "__main__":
    main()
