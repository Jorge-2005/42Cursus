with open("01_linear_path.txt") as file:
    number = 1
    for cont in file:
        if not (cont.startswith("#") or cont.startswith("\n")):
            print(f"{number}: {cont.strip()}")
        number += 1


def parse_map():
    pass
