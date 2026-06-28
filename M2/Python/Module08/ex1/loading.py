import importlib # noqa
import sys


def check_package(name: str) -> None:
    try:
        module = importlib.import_module(name)
        version = module.__version__
        print(f"[OK] {name} ({version})")
    except ImportError:
        print(f"[ERROR] {name} - NOT INSTALLED")
        sys.exit(1)


print("\nLOADING STATUS: Loading programs...\n")

print("Checking dependencies:")
check_package("numpy")
check_package("pandas")
check_package("matplotlib")

print("\n--- Pip vs Poetry ---")
print("pip: uses requirements.txt (manual dependency management)")
print("poetry: uses pyproject.toml (automatic dependency management)")

import numpy as np # noqa
import pandas as pd # noqa
import matplotlib.pyplot as plt # noqa


time = np.arange(10)
data = np.random.random(10)
df = pd.DataFrame({
    "time": time,
    "data": data
})
plt.plot(df["time"], df["data"])
plt.title("Matrix Signal")
plt.xlabel("Time")
plt.ylabel("Value")
plt.grid()
plt.savefig("matrix_analysis.png")

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
