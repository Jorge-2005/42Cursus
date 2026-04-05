import sys
from typing import TextIO


if (len(sys.argv) == 2):
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        file: TextIO = open(sys.argv[1])
        print(f"Accessing file '{sys.argv[1]}'")
        print("---\n")
        print(file.read())
        print("\n---")
        print(f"File '{sys.argv[1]}' closed.\n")
        file.close()
        file = open(sys.argv[1])
        new_list: list[str] = file.read().split("\n")
        print("Transform data:")
        print("---\n")
        i: int = 0
        while i < len(new_list):
            new_list[i] = new_list[i].strip() + "#\n"
            print(new_list[i], end="")
            i += 1
        print("\n---")
        name: str = input("Enter new file name (or empty):")
        if (name == ""):
            print("Not saving data.")
        else:
            print(f"Saving data to '{name}'")
            new_file = open(name, "w")
            i = 0
            while i < len(new_list):
                new_file.write(new_list[i])
                i += 1
            print(f"Data saved in file '{name}'.")
            new_file.close()
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
