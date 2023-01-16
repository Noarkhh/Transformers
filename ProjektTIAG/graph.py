from __future__ import annotations
from typing import Optional
from node import Node
from edge import Edge
from color import Color
from production import Production


class Graph:
    def __init__(self, nodes: Optional[list[Node]] = None, edges: Optional[list[Edge]] = None) -> None:
        self.nodes: list[Node] = []
        self.edges: list[Edge] = []
        self.adjacency_dict: dict[Node, list[Node]] = {}
        self.adjacency_matrix: dict[Node, dict[Node, bool]] = {}

        self.nodes_by_id: dict[int, Node] = {}

        if nodes is not None:
            for node in nodes:
                self.add_node(node)

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def get_node(self, node_id: int) -> Node:
        return self.nodes_by_id.get(node_id)

    def get_new_node_id(self) -> int:
        return max(self.nodes_by_id) + 1 if self.nodes_by_id else 0

    def add_node(self, node: Node) -> None:
        self.nodes.append(node)
        self.adjacency_dict[node] = []
        self.adjacency_matrix[node] = {}
        for existing_node in self.nodes:
            self.adjacency_matrix[node][existing_node] = False
            self.adjacency_matrix[existing_node][node] = False

        self.nodes_by_id[node.node_id] = node

    def add_edge(self, edge: Edge) -> None:
        for node in edge.ends:
            if node not in self.nodes:
                raise ValueError("At least one of edges ends doesn't belong to the graph.")
        self.edges.append(edge)
        self.adjacency_dict[edge.ends[0]].append(edge.ends[1])
        self.adjacency_dict[edge.ends[1]].append(edge.ends[0])

        self.adjacency_matrix[edge.ends[0]][edge.ends[1]] = True
        self.adjacency_matrix[edge.ends[1]][edge.ends[0]] = True

    def remove_node(self, node: Node) -> None:
        if node not in self.nodes:
            raise ValueError("Node not in graph")
        if self.adjacency_dict[node]:
            raise ValueError("Node connected, can't separate")

        self.nodes.remove(node)
        self.adjacency_dict.pop(node)
        self.adjacency_matrix.pop(node)
        for connections in self.adjacency_matrix.values():
            connections.pop(node)
        self.nodes_by_id.pop(node.node_id)

    def remove_edge(self, edge: Edge):
        if edge not in self.edges:
            raise ValueError("Edge not in graph")

        self.edges.remove(edge)
        self.adjacency_dict[edge.ends[0]].remove(edge.ends[1])
        self.adjacency_dict[edge.ends[1]].remove(edge.ends[0])

        self.adjacency_matrix[edge.ends[0]][edge.ends[1]] = False
        self.adjacency_matrix[edge.ends[1]][edge.ends[0]] = False

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
        matrix_str = str(self.adjacency_matrix).replace('}, ', '}\n ')
        return f"\nnodes: {self.nodes}\nedges: {self.edges}\ndict: {self.adjacency_dict}\nmatrix:\n{matrix_str}"


if __name__ == "__main__":
    graph1 = Graph()
    graph1.add_node(Node(0, Color.RED))
    graph1.add_node(Node(1, Color.YELLOW))
    graph1.add_edge(Edge(graph1.get_node(0), graph1.get_node(1)))
    graph1.add_node(Node(2, Color.PINK))
    graph1.add_edge(Edge(graph1.get_node(0), graph1.get_node(2)))
    print(graph1)

    graph2 = Graph()
    graph2.add_node(Node(1, Color.YELLOW))
    graph2.add_node(Node(2, Color.PINK))
    graph2.add_edge(Edge(graph1.get_node(1), graph1.get_node(2)))
    print("\n\n")
    print(graph2)
    print(graph1.intersection(graph2))

    production = Production(graph1, graph2)

    production.apply(graph1, [Node(0, Color.RED), Node(1, Color.YELLOW), Node(5, Color.PINK)])
