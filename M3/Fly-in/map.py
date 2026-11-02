from graph import Graph


class Map():
    """keep the data to start the simulation"""
    def __init__(self, nb_drones: int, graph: Graph) -> None:
        self.nb_drones = nb_drones
        self.graph = graph
