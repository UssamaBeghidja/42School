#!/usr/bin/env python3

import sys
import typing


def main(path: str) -> dict[str, str]:
    if len(sys.argv) != 2:
        print("Usage: python3 ft_ancient_text.py <path>")
        sys.exit(1)
    print("=== Cyber Archives Recovery and Preservation ===")
    print(f"Accessing file '{path}'")
    try:
        f: typing.IO = open(path, "r")
        content = f.read()
        print("---")
        print(content)
        print("---")
        f.close()
        print(f"File '{path}' closed.")
        print("Transform data:")
        print("---")
        lines = content.splitlines()
        new_content = "\n".join([line + "#" for line in lines])
        print(new_content)
        print("---")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        new_path = sys.stdin.readline().rstrip("\n")
        if new_path == "":
            print("Not saving data.")
        else:
            f: typing.IO = open(new_path, "w")
            f.write(new_content)
            f.close()
            print(f"Saving data to '{new_path}'")
            print(f"Data saved in file '{new_path}'.")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{path}': {e}\n")
        sys.stderr.flush()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        main(sys.argv[1])
