from __future__ import annotations

from src.production import Production
from src.graph import Graph
from src.parser import parse_node_input
from src.visualiser import Visualiser
from src.production_manager import ProductionManager
import json


if __name__ == "__main__":

    main_graph = Graph()

    production_manager: ProductionManager = ProductionManager()
    visualiser: Visualiser = Visualiser(main_graph)
    load_init: bool = input("Load initial sequence? [Y/N] (default: N)\n") in ("y", "Y")

    if load_init:
        try:
            with open("../init.json", "r") as f:
                init_list: list[list[list[int], str]] = json.load(f)
                for nodes_ids, production_name in init_list:
                    production: Production = production_manager.productions.get(production_name)
                    nodes = [main_graph.get_node(node_id) for node_id in nodes_ids]
                    try:
                        production.apply(main_graph, nodes)
                    except ValueError as e:
                        print(e)

                visualiser.show()
        except Exception:
            print("Error loading initial sequence.")
            main_graph = Graph()

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










