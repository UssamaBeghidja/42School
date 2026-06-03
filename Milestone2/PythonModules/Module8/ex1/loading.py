#!/usr/bin/env python3

import importlib.metadata

try:
    import numpy as np
    import pandas as pd
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    DEPS_OK = True
except ImportError as e:
    print(f"Missing: {e}")
    print("pip: pip install -r requirements.txt")
    print("Poetry: poetry install")
    DEPS_OK = False


def check_deps() -> None:
    print("Checking dependencies:")
    for pkg, desc in [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]:
        try:
            v = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({v}) - {desc}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[MISSING] {pkg}")


def analyze() -> None:
    print("Analyzing Matrix data...")
    data = np.random.randn(1000)   # numpy as data source!
    df = pd.DataFrame({"signal": data})
    print(f"Processing {len(df)} data points...")
    print("Generating visualization...")
    fig, ax = plt.subplots()
    ax.hist(data, bins=50, color="green")
    ax.set_title("Matrix Signal")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    print("LOADING STATUS: Loading programs...")
    check_deps()
    if DEPS_OK:
        analyze()


if __name__ == "__main__":
    main()
