import sys
from typing import TextIO


if (len(sys.argv) == 2):
    print("=== Cyber Archives Recovery ===")
    try:
        file: TextIO = open(sys.argv[1])
        print(f"Accessing file '{sys.argv[1]}'")
        print("---\n")
        print(file.read())
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.")
        file.close()
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except IsADirectoryError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except Exception as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
else:
    print(f"Usage: {sys.argv[0]} <file>")
