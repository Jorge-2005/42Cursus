import math
print("=== Game Coordinate System ===\n")


def get_player_pos() -> tuple[float, float, float]:
    stop = False
    while (not stop):
        coor: str = input("Enter new coordinates as "
                          "floats in format 'x,y,z': ")
        i = 0
        cont2: int = 0
        cont: int = 0
        lenght: int = 0
        num: str = ""
        value: list[float] = []
        for m in coor:
            lenght += 1
        for j in coor:
            cont += 1
            if (j == ","):
                try:
                    value.append(float(num))
                    num = ""
                    cont2 += 1
                except ValueError:
                    print("Invalid syntax")
                    i = 1
                    num = ""
                    break
            else:
                num += j
        if (cont == lenght and cont2 == 2):
            try:
                value.append(float(num))
                stop = True
            except ValueError:
                print("Invalid syntax")
        else:
            if i != 1:
                print("Invalid syntax")
    return (value[0], value[1], value[2])


coordinates = get_player_pos()
x: float = coordinates[0]
y: float = coordinates[1]
z: float = coordinates[2]
print(f"Got a first tuple: {coordinates}")
print(f"It includes: X={x}, Y={y}, Z={z}")
print(f"Distance to center: {math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)}")
print("\nGet a second set of coordinates")
coordinates2 = get_player_pos()
x2, y2, z2 = coordinates2
print("Distance between the 2 sets of coordinates: "
      f"{math.sqrt((x2-x)**2 + (y2-y)**2 + (z2-z)**2)}")
