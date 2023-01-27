from __future__ import annotations
from typing import Optional
from src.node import Node
from src.graph import Graph
import ast


def parse_node_input(nodes_str: str, main_graph: Graph) -> Optional[list[Node]]:
    try:
        nodes_ids = ast.literal_eval(nodes_str)
        if isinstance(nodes_ids, int):
            nodes_ids = [nodes_ids]
        if not isinstance(nodes_ids, list) and not isinstance(nodes_ids, tuple) and not isinstance(nodes_ids, set):
            raise ValueError
        if not all([isinstance(node_id, int) for node_id in nodes_ids]):
            raise ValueError
    except (SyntaxError, ValueError):
        if nodes_str == "":
            nodes_ids = []
        else:
            print("Incorrect input format!")
            return None

    nodes: list[Node] = []
    for node_id in nodes_ids:
        node = main_graph.get_node(node_id)
        if node is None:
            print(f"Node {node_id} does not exist in the main graph!")
            return None
        nodes.append(node)

    return nodes

