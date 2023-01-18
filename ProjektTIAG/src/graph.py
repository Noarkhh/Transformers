from __future__ import annotations
from typing import Optional
from src.node import Node
from src.edge import Edge
from src.color import Color
from src.production import Production


class Graph:
    def __init__(self, nodes: Optional[list[Node]] = None, edges: Optional[list[Edge]] = None) -> None:
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.adjacency_dict: dict[Node, list[Node]] = {}

        self.nodes_by_id: dict[int, Node] = {}

        if nodes is not None:
            for node in nodes:
                self.add_node(node)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def get_node(self, node_id: int) -> Optional[Node]:
        return self.nodes_by_id.get(node_id)

    def get_new_node_id(self) -> int:
        return max(self.nodes_by_id) + 1 if self.nodes_by_id else 0

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self.adjacency_dict[node] = []

        self.nodes_by_id[node.node_id] = node

    def add_edge(self, edge: Edge) -> None:
        for node in edge.ends:
            if node not in self.nodes:
                raise ValueError("At least one of edges ends doesn't belong to the graph.")
        self.edges.append(edge)
        self.adjacency_dict[edge.ends[0]].append(edge.ends[1])
        self.adjacency_dict[edge.ends[1]].append(edge.ends[0])

    def remove_node(self, node: Node) -> None:
        if node not in self.nodes:
            raise ValueError("Node not in graph")
        if self.adjacency_dict[node]:
            raise ValueError("Node connected, can't separate")

        self.nodes.remove(node)
        self.adjacency_dict.pop(node)
        self.nodes_by_id.pop(node.node_id)

    def remove_edge(self, edge: Edge):
        if edge not in self.edges:
            raise ValueError(f"Edge {edge} not in graph")

        self.edges.remove(edge)
        self.adjacency_dict[edge.ends[0]].remove(edge.ends[1])
        self.adjacency_dict[edge.ends[1]].remove(edge.ends[0])

    def intersection(self, other: Graph) -> Graph:
        shared_nodes: list[Node] = []
        shared_edges: list[Edge] = []

        for node1 in self.nodes:
            for node2 in other.nodes:
                if node1 == node2:
                    shared_nodes.append(node1)

        for edge1 in self.edges:
            for edge2 in other.edges:
                if edge1 == edge2:
                    shared_edges.append(edge1)

        return Graph(shared_nodes, shared_edges)

    def copy_with_id_mapping(self, mapping: dict[int, int]) -> Graph:
        nodes = [Node(mapping[node.node_id], node.color) for node in self.nodes]
        edges = [Edge(Node(mapping[edge.ends[0].node_id], edge.ends[0].color),
                      Node(mapping[edge.ends[1].node_id], edge.ends[1].color)) for edge in self.edges]
        return Graph(nodes, edges)

    def __repr__(self) -> str:
        return f"\nnodes: {self.nodes}\nedges: {self.edges}\ndict: {self.adjacency_dict}\n"
