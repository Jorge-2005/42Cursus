from error import Error
from zones import Zone, ZoneTypes, Connection
from graph import Graph
from map import Map


def parse_drone(d_line: str) -> int:
    """Parse the number of drones from a map file line."""

    if d_line.startswith("nb_drones:"):
        line_parts: list[str] = d_line.split(":", 1)
        try:
            num_drones = int(line_parts[1].strip())
        except ValueError:
            raise Error("nb_drones must be a number")
        if num_drones <= 0:
            raise Error("nb_drones must be a positive integer")
        return num_drones
    else:
        raise Error("Wrong file structure")


def parse_metadata(
        l_metadata: str, allowed: set[str]) -> dict[str, str]:
    """Parse and validate optional metadata."""

    if l_metadata.startswith("[") and l_metadata.endswith("]"):
        l_metadata = l_metadata[1:-1]

        if not l_metadata:
            raise Error("Metadata is empty")
        group_metadata: list[str] = l_metadata.split()

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
    elif not l_metadata:
        return {}
    else:
        raise Error("Invalid metadata format")


def parse_zone(role: str, z_line: str) -> Zone:
    """Parse a zone definition and create a Zone object."""

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
    if "max_drones" in met_data:  # preguntar lo de start y end para "abc"
        try:
            max_d = int(met_data["max_drones"])
        except ValueError:
            raise Error("max_drones must be a valid number")
    if max_d <= 0 and role == "normal":
        raise Error("max_drones must be 1 or higher")
    if "color" in met_data:
        color = met_data["color"]

    return Zone(zone_data_list[0], x, y, zone_type, color, max_d,
                start_hub=(role == "start"),
                end_hub=(role == "end"))


def parse_connection(c_line: str, graph: Graph) -> Connection:
    """Parse a connection definition and create a Connection object."""

    con_data, separator, metadata = c_line.partition("[")
    con_data_list: list[str] = con_data.strip().split("-")

    if len(con_data_list) != 2:
        raise Error("Wrong connection format")
    if con_data_list[0] == "" or con_data_list[1] == "":
        raise Error("The connection must have 2 Zones")
    if " " in con_data_list[0] or " " in con_data_list[1]:
        raise Error("The format must be 'a-b'")

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

    zone1: Zone = graph.get_zone(con_data_list[0])
    zone2: Zone = graph.get_zone(con_data_list[1])

    return Connection(zone1, zone2, max_l_cap)


def parse_map(file: str) -> Map:
    """Read and parse a map file."""

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

    try:
        result: int = parse_drone(drone_line)
    except Error as e:
        raise Error(f"{line_num}: {e}")

    has_start: bool = False
    has_end: bool = False
    graph = Graph()

    for num, line in enumerate(lines[line_num:], start=line_num + 1):
        role: str = "normal"
        line = line.strip()
        try:
            if line.startswith("#") or line == "":
                continue
            elif line.startswith("start_hub:"):
                if has_start:
                    raise Error("Duplicated start_hub")

                role = "start"
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))
                has_start = True

            elif line.startswith("end_hub:"):
                if has_end:
                    raise Error("Duplicated end_hub")

                role = "end"
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))
                has_end = True

            elif line.startswith("hub:"):
                graph.add_zone(parse_zone(role, line.split(":", 1)[1]))

            elif line.startswith("connection:"):
                graph.add_connection(
                    parse_connection(line.split(":", 1)[1], graph))
            else:
                raise Error("Invalid format")
        except Error as e:
            raise Error(f"{num}: {e}")
    if not has_start or not has_end:
        raise Error("The map has to have a start and a end")

    return Map(result, graph)


parse_map("01_linear_path.txt")
# parse_map("01_maze_nightmare.txt")
