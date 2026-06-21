#!/usr/bin/env python3

import sys
import typing


def main(path: str) -> None:
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
    except OSError as e:
        print(f"Error opening file '{path}': {e}")
        return

    print("Transform data:")
    print("---")
    lines = content.splitlines()
    new_content = "\n".join([line + "#" for line in lines])
    print(new_content)
    print("---")
    new_path = input("Enter new file name (or empty): ")
    if new_path == "":
        print("Not saving data.")
        return

    try:
        new_f: typing.IO = open(new_path, "w")
        new_f.write(new_content)
        new_f.close()
        print(f"Saving data to '{new_path}'")
        print(f"Data saved in file '{new_path}'.")
    except OSError as e:
        print(f"Error opening file '{new_path}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        main(sys.argv[1])
