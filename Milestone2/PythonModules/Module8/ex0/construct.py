#!/usr/bin/env python3

import sys
import os
import site


def is_in_venv() -> bool:
    return sys.prefix != sys.base_prefix


def main() -> None:
    if is_in_venv():
        venv = os.environ.get("VIRTUAL_ENV", "")
        venv_name = os.path.basename(venv)
        pkg_path = site.getsitepackages()[0]
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {venv}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print(f"Package installation path:\n{pkg_path}")
    else:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
