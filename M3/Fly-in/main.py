import sys
from error import Error
from map import Map
from parser import parse_map
from graph import Graph


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise Error("You need only 1 argument")
        map: Map = parse_map(sys.argv[1])
        # print(map.nb_drones)
        # print(map.graph.zones.keys())
        map.graph.get_neighbors("waypoint1")  # Borrar
    except Error as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
