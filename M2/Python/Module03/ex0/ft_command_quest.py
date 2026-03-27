import sys

print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if (len(sys.argv) == 1):
    print("No arguments provided!")
    print(f"Total arguments: {len(sys.argv)}")
else:
    print(f"Arguments received: {len(sys.argv) -1}")
    lenth: int = 1
    while (lenth < len(sys.argv)):
        print(f"Argument {lenth}: {sys.argv[lenth]}")
        lenth += 1
    print(f"Total arguments: {len(sys.argv)}")
