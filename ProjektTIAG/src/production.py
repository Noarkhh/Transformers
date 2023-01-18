from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.graph import Graph
    from src.node import Node


class Production:

    def __init__(self, left_graph: Graph, right_graph: Graph):
        self.left_graph: Graph = left_graph
        self.right_graph: Graph = right_graph
        self.middle_graph: Graph = left_graph.intersection(right_graph)

    def is_valid(self, main_graph: Graph, nodes: list[Node]) -> dict[int, int]:
        if len(nodes) != len(self.left_graph.nodes):
            raise ValueError("Wrong amount of nodes!")
        if not all([node in main_graph.nodes for node in nodes]):
            raise ValueError("Not all given nodes in the main graph!")
        prod_nodes = self.left_graph.nodes.copy()
        main_nodes = nodes.copy()

        prod_to_main_nodes_ids = {}

        while prod_nodes:
            for main_node in main_nodes:
                if main_node.color_eq(prod_nodes[-1]):
                    prod_node = prod_nodes.pop(-1)
                    main_nodes.remove(main_node)
                    prod_to_main_nodes_ids[prod_node.node_id] = main_node.node_id
                    break
            else:
                raise ValueError("Nodes' colors do not match!")

        return prod_to_main_nodes_ids

    def apply(self, main_graph: Graph, nodes: list[Node]) -> None:

        prod_to_main_nodes_ids = self.is_valid(main_graph, nodes)

        mapped_left = self.left_graph.copy_with_id_mapping(prod_to_main_nodes_ids)
        mapped_middle = self.middle_graph.copy_with_id_mapping(prod_to_main_nodes_ids)

        for left_edge in mapped_left.edges:
            if left_edge not in main_graph.edges:
                raise ValueError("Edge in left production graph not in main graph!")

        for left_node in mapped_left.nodes:
            if left_node in mapped_middle.nodes:
                continue
            for connected_node in main_graph.adjacency_dict[left_node]:
                if connected_node.node_id not in mapped_middle.nodes:
                    raise ValueError("Illegal embedding of production graph!")

        for left_edge in mapped_left.edges:
            if left_edge not in mapped_middle.edges:
                main_graph.remove_edge(left_edge)

        for left_node in mapped_left.nodes:
            if left_node not in mapped_middle.nodes:
                main_graph.remove_node(left_node)

        already_added = 0
        for node in self.right_graph.nodes:
            if prod_to_main_nodes_ids.get(node.node_id) is None:
                prod_to_main_nodes_ids[node.node_id] = main_graph.get_new_node_id() + already_added
                already_added += 1

        mapped_right = self.right_graph.copy_with_id_mapping(prod_to_main_nodes_ids)

        for right_node in mapped_right.nodes:
            if right_node not in mapped_middle.nodes:
                main_graph.add_node(right_node)

        for right_edge in mapped_right.edges:
            if right_edge not in mapped_middle.edges:
                main_graph.add_edge(right_edge)

    def __repr__(self):
        return f"L: {self.left_graph}\nM: {self.middle_graph}\nR: {self.right_graph}"
