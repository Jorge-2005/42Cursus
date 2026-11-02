from error import Error


def parse_drone(d_line: str, l_num: int) -> int:
    if d_line.startswith("nb_drones:"):
        line_parts: list[str] = d_line.split(":", 1)
        try:
            num_drones = int(line_parts[1].strip())
        except ValueError:
            raise Error(f"{l_num}: nb_drones must be a number")
        if num_drones <= 0:
            raise Error(f"{l_num}: nb_drones must be a positive integer")
        return num_drones
    else:
        raise Error(f"{l_num}: Wrong file structure")


def parse_map(file: str) -> None:
    try:
        with open(file, "r") as f:
            lines: list[str] = f.readlines()

    except OSError:
        raise Error(f"Error opening file '{file}'.")

    drone_line: str = ""
    line_num: int = 0
    for num, line in enumerate(lines, start=1):
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        else:
            drone_line = line
            line_num = num
            break

    if drone_line == "":
        raise Error("The file is empty")

    result: int = parse_drone(drone_line, line_num)
    print(f"{line_num}:{result}")


parse_map("01_linear_path.txt")
