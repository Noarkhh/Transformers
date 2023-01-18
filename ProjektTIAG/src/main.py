from __future__ import annotations

from src.production import Production
from src.graph import Graph
from src.parser import parse_node_input
from src.visualiser import Visualiser
from src.production_manager import ProductionManager


if __name__ == "__main__":

    main_graph = Graph([], [])

    production_manager: ProductionManager = ProductionManager()
    visualiser: Visualiser = Visualiser(main_graph)

    while True:
        nodes_str: str = input("\nInput ID's of nodes to embed the transformation onto (ex. [1, 3, 5]): ")
        nodes = parse_node_input(nodes_str, main_graph)
        if nodes is None:
            continue

        production_name: str = input("Input the transformation name: ")
        production: Production = production_manager.productions.get(production_name)
        if production is None:
            print("Production does not exist!")
            continue

        try:
            production.apply(main_graph, nodes)
        except ValueError as e:
            print(e)
            continue

        visualiser.show()










