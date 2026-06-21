#!/usr/bin/env python3

import sys
import typing


def main(path: str) -> None:
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{path}'")
    try:
        f: typing.IO = open(path, "r")
        content = f.read()
        print("---")
        print(content)
        print("---")
        f.close()
        print(f"File '{path}' closed.")
    except OSError as e:
        print(f"Error opening file '{path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        main(sys.argv[1])
