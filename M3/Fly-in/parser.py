from error import Error
from zones import Zone, ZoneTypes


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


def parse_metadata(
        l_metadata: str, allowed: set[str], l_num: int) -> dict[str, str]:

    if l_metadata.startswith("[") and l_metadata.endswith("]"):
        l_metadata = l_metadata[1:-1]
        # no esta terminado revisar bien
        if not l_metadata:
            raise Error(f"{l_num}: Metadata is empty")
        group_metadata: list[str] = l_metadata.split()

        # esto lo tengo para ir guardando los datos y que no se repitan
        result: dict[str, str] = {}
        for i in group_metadata:
            key, sep, value = i.partition("=")
            if not sep or not value:
                raise Error(f"{l_num}: Invalid metadata")
            if key not in allowed:
                raise Error(f"{l_num}: The metadata '{key}' is not allowed")
            if key in result:
                raise Error(f"{l_num}: The metadata '{key}' is duplicated")
            result[key] = value
        return result
    elif not l_metadata:  # comprobar esta condición
        return {}
    else:
        raise Error(f"{l_num}: Invalid metadata format")


def parse_zone(role: str, z_line: str, l_num: int) -> None:

    zone_data, separator, metadata = z_line.partition("[")
    zone_data_list: list[str] = zone_data.strip().split()

    if len(zone_data_list) != 3:
        raise Error(f"{l_num}: Invalid data Zone")
    if "-" in zone_data_list[0]:
        raise Error(f"{l_num}: Invalid name Zone")
    try:
        int(zone_data_list[1])
        int(zone_data_list[2])
    except ValueError:
        raise Error(f"{l_num}: Invalid coordinates")

    met_data: dict[str, str] = parse_metadata(
        separator + metadata,
        {"zone", "color", "max_drones"},
        l_num)

    max_d: int = 1
    zone_type: ZoneTypes = ZoneTypes.NORMAL
    if "zone" in met_data:
        try:
            zone_type = ZoneTypes(met_data["zone"])
        except ValueError:
            raise Error(f"{l_num}: Wrong zone type")
    if "max_drones" in met_data:
        try:
            max_d = int(met_data["max_drones"])
        except ValueError:
            raise Error(f"{l_num}: max_drones must be a valid number")
    if max_d <= 0:
        raise Error(f"{l_num}: max_drones must be 1 or higher")
    # lo unico que creo que me queda es mandar todos los datos al graph
    # name, x, y, zone_type, color. max_drones

    # Esto es lo ultimo que voy a hacer por que es solo
    # para rellenar las zonas
    if role == "start":
        pass
    elif role == "end":
        pass
    else:
        pass


def parse_connection(c_line: str, l_num: int) -> None:
    pass


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

    for num, line in enumerate(lines[line_num:], start=line_num + 1):
        role: str = "normal"
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        elif line.startswith("start_hub:"):
            role = "start"
            parse_zone(role, line.split(":", 1)[1], num)
        elif line.startswith("end_hub:"):
            role = "end"
            parse_zone(role, line.split(":", 1)[1], num)
        elif line.startswith("hub:"):
            parse_zone(role, line.split(":", 1)[1], num)
        elif line.startswith("connection:"):
            # revisar
            parse_connection(line.split(":", 1)[1], num)
        else:
            raise Error(f"{num}: Invalid format")


parse_map("01_linear_path.txt")
# parse_map("01_maze_nightmare.txt")
