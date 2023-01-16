from __future__ import annotations
from typing import Optional
from node import Node
from edge import Edge
from color import Color
from production import Production
from graph import Graph

if __name__ == "__main__":
    n1 = Node(1, Color.RED)
    n2 = Node(2, Color.YELLOW)
    n3 = Node(3, Color.PINK)
    n6 = Node(6, Color.RED)
    n7 = Node(7, Color.RED)
    n8 = Node(8, Color.PINK)

    edge_list = [Edge(n1, n2), Edge(n7, n2), Edge(n3, n2), Edge(n1, n3), Edge(n1, n6), Edge(n6, n7)]
    main_graph = Graph([n1, n2, n3, n6, n7, n8], edge_list)
    print(main_graph)

    ln1 = Node(11, Color.RED)
    ln2 = Node(2, Color.YELLOW)
    ln3 = Node(3, Color.PINK)

    left_graph = Graph([ln1, ln2, ln3],
                       [Edge(ln1, ln2), Edge(ln2, ln3), Edge(ln3, ln1)])

    rn1 = Node(11, Color.RED)
    rn2 = Node(2, Color.YELLOW)
    rn5 = Node(5, Color.PINK)
    rn4 = Node(4, Color.YELLOW)

    right_graph = Graph([rn1, rn2, rn5, rn4],
                        [Edge(rn1, rn4), Edge(rn2, rn4), Edge(rn5, rn2), Edge(rn5, rn1)])

    production = Production(left_graph, right_graph)

    print(left_graph)
    print(right_graph)
    print(production.middle_graph)

    production.apply(main_graph, [n1, n2, n3])

    print(main_graph)




