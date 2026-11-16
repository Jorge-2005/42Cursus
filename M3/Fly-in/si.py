from error import Error
from zones import Zone, ZoneTypes, Connection
from graph import Graph


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
        l_metadata: str, allowed: set[str]) -> dict[str, str]:

    if l_metadata.startswith("[") and l_metadata.endswith("]"):
        l_metadata = l_metadata[1:-1]

        if not l_metadata:
            raise Error("Metadata is empty")
        group_metadata: list[str] = l_metadata.split()

        # esto lo tengo para ir guardando los datos y que no se repitan
        result: dict[str, str] = {}
        for i in group_metadata:
            key, sep, value = i.partition("=")
            if not sep or not value:
                raise Error("Invalid metadata")
            if key not in allowed:
                raise Error(f"The metadata '{key}' is not allowed")
            if key in result:
                raise Error(f"The metadata '{key}' is duplicated")
            result[key] = value
        return result
    elif not l_metadata:  # comprobar esta condición
        return {}
    else:
        raise Error("Invalid metadata format")


def parse_zone(role: str, z_line: str) -> Zone:

    zone_data, separator, metadata = z_line.partition("[")
    zone_data_list: list[str] = zone_data.strip().split()

    if len(zone_data_list) != 3:
        raise Error("Invalid data Zone")
    if "-" in zone_data_list[0]:
        raise Error("Invalid name Zone")
    try:
        x: int = int(zone_data_list[1])
        y: int = int(zone_data_list[2])
    except ValueError:
        raise Error("Invalid coordinates")

    met_data: dict[str, str] = parse_metadata(
        separator + metadata, {"zone", "color", "max_drones"})

    max_d: int = 1
    zone_type: ZoneTypes = ZoneTypes.NORMAL
    color: str = "none"
    if "zone" in met_data:
        try:
            zone_type = ZoneTypes(met_data["zone"])
        except ValueError:
            raise Error("Wrong zone type")
    if "max_drones" in met_data:  # preguntar lo de start y end
        try:
            max_d = int(met_data["max_drones"])
        except ValueError:
            raise Error("max_drones must be a valid number")
    if max_d <= 0 and role == "normal":  # ignorar cuando sea start y end
        raise Error("max_drones must be 1 or higher")
    if "color" in met_data:
        color = met_data["color"]

    return Zone(zone_data_list[0], x, y, zone_type, color, max_d,
                start_hub=(role == "start"),
                end_hub=(role == "end"))


"""
tengo que pasarle el graph para comprobar las zonar por que
tengo que parsearlo a zona, y ver que hacer cuando pasa
algo como esto a - b (espacio entre las conexiones, yo creo que es un error)
"""


def parse_connection(c_line: str) -> Connection:
    con_data, separator, metadata = c_line.partition("[")
    con_data_list: list[str] = con_data.strip().split("-")

    if len(con_data_list) != 2:
        raise Error("Wrong connection format")
    if con_data_list[0] == "" or con_data_list[1] == "":
        raise Error("The connection must have 2 Zones")

    met_data_con: dict[str, str] = parse_metadata(
        separator + metadata, {"max_link_capacity"})

    max_l_cap: int = 1
    if "max_link_capacity" in met_data_con:
        try:
            max_l_cap = int(met_data_con["max_link_capacity"])
        except ValueError:
            raise Error("max_link_capacity must be a valid number")
    if max_l_cap <= 0:
        raise Error("max_link_capacity must be 1 or higher")

    return Connection(con_data_list[0], con_data_list[1], max_l_cap)


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

    has_start: bool = False
    has_end: bool = False
    graph = Graph()

    for num, line in enumerate(lines[line_num:], start=line_num + 1):
        role: str = "normal"
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        elif line.startswith("start_hub:"):
            if has_start:
                raise Error(f"{num}: Duplicated start_hub")
            role = "start"
            try:
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))
            except Error as e:
                raise Error(f"{num}: {e}")
            has_start = True
        elif line.startswith("end_hub:"):
            if has_end:
                raise Error(f"{num}: Duplicated end_hub")
            role = "end"
            try:
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))
            except Error as e:
                raise Error(f"{num}: {e}")
            has_end = True
        elif line.startswith("hub:"):
            try:
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))
            except Error as e:
                raise Error(f"{num}: {e}")
        elif line.startswith("connection:"):
            parse_connection(line.split(":", 1)[1])
        else:
            raise Error(f"{num}: Invalid format")
    if not has_start or not has_end:
        raise Error("The map has to have a start and a end")


parse_map("01_linear_path.txt")
# parse_map("01_maze_nightmare.txt")
