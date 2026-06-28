# piton -m venv carpeta
# source myenv/bin/activate
# which python3
# deactivate
import sys
import os
import site


if (sys.prefix != sys.base_prefix):
    VIRTUAL_ENV = os.environ.get("VIRTUAL_ENV")
    name: str | None = (VIRTUAL_ENV or "no-venv").split("/")[-1]
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {name}")
    print(f"Environment Path: {VIRTUAL_ENV}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(f"{site.getsitepackages()}")
else:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.prefix}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env/Scripts/activate # On Windows\n")
    print("Then run this program again.")
