from src.graph import Graph
from pyvis.network import Network


class Visualiser:
    def __init__(self, main_graph: Graph):
        self.main_graph: Graph = main_graph

    def show(self) -> None:
        network = Network()
        network.add_nodes([node.node_id for node in self.main_graph.nodes],
                          label=[str(node) for node in self.main_graph.nodes],
                          color=[str(node.color) for node in self.main_graph.nodes])

        network.add_edges([(edge.ends[0].node_id, edge.ends[1].node_id) for edge in self.main_graph.edges])
        network.show("tiag.html")

