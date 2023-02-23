from src.color import Color
from src.production import Production
from src.node import Node
from src.edge import Edge
from src.graph import Graph
from typing import Any
import json
import glob
import os


class ProductionManager:
    def __init__(self) -> None:
        self.productions: dict[str, Production] = {}

        for production_path in glob.glob("../productions/*.json"):
            with open(production_path, "r") as f:
                self.parse_production(production_path.removeprefix("../productions/").removesuffix(".json"), json.load(f))

    def parse_production(self, production_name: str, production_dict: dict[str, dict[str, Any]]) -> None:
        left_nodes: dict[int, Node] = {}
        for node_id, node_color in production_dict["left"]["nodes"].items():
            left_nodes[int(node_id)] = Node(int(node_id), Color[node_color])

        left_edges: list[Edge] = []
        for node1, node2 in production_dict["left"]["edges"]:
            left_edges.append(Edge(left_nodes[node1], left_nodes[node2]))

        left_graph: Graph = Graph(list(left_nodes.values()), left_edges)

        right_nodes: dict[int, Node] = {}
        for node_id, node_color in production_dict["right"]["nodes"].items():
            right_nodes[int(node_id)] = Node(int(node_id), Color[node_color])

        right_edges: list[Edge] = []
        for node1, node2 in production_dict["right"]["edges"]:
            right_edges.append(Edge(right_nodes[node1], right_nodes[node2]))

        right_graph: Graph = Graph(list(right_nodes.values()), right_edges)

        self.productions[production_name] = (Production(left_graph, right_graph))



