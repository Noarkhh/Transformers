from node import Node


class Edge:
    ends: tuple[Node, Node]

    def __init__(self, node1: Node, node2: Node):
        self.ends = (node1, node2)

    def __repr__(self):
        return f"({self.ends[0]} <-> {self.ends[1]})"

    def __eq__(self, other):
        if not isinstance(other, Edge):
            return False
        return set(self.ends) == set(other.ends)
