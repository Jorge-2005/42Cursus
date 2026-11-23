import sys
from error import Error
from map import Map
from parser import parse_map


def main() -> None:
    try:
        if len(sys.argv) != 2:
            raise Error("You need only 1 argument")
        d_map: Map = parse_map(sys.argv[1])
        print(d_map.nb_drones)
        print(d_map.graph.zones.keys())


    except Error as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
