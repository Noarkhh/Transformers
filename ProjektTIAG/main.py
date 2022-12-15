from collections import namedtuple
from itertools import combinations

from pyvis.network import Network

Graph = namedtuple("Graph", ["nodes", "edges", "is_directed"])


def adjacency_dict(graph):
    """
    Returns the adjacency list representation
    of the graph.
    """
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        if not graph.is_directed:
            adj[node2].append(node1)
    return adj


def adjacency_matrix(graph):
    """
    Returns the adjacency matrix of the graph.
    Assumes that graph.nodes is equivalent to range(len(graph.nodes)).
    """
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1][node2] += 1
        if not graph.is_directed:
            adj[node2][node1] += 1
    return adj


def show(graph, output_filename, colors, labels):
    """
    Saves an HTML file locally containing a
    visualization of the graph, and returns
    a pyvis Network instance of the graph.
    """
    g = Network(directed=graph.is_directed)
    g.add_nodes(graph.nodes, label=labels, color=colors)
    g.add_edges(graph.edges)
    g.show(output_filename)
    return g


def _validate_num_nodes(num_nodes):
    """
    Check whether or not `num_nodes` is a
    positive integer, and raise a TypeError
    or ValueError if it is not.
    """
    if not isinstance(num_nodes, int):
        raise TypeError(f"num_nodes must be an integer; {type(num_nodes)=}")
    if num_nodes < 1:
        raise ValueError(f"num_nodes must be positive; {num_nodes=}")


def color(s):
    match s:
        case "yellow":
            return '#FFCC00'
        case "red":
            return '#FF0000'
    return '#FFFFFF'


def t1(nodes, colors, labels, node):
    # adds yellow node
    nodes.append(max(nodes) + 1)
    edges.append((node, max(nodes)))
    labels.append(str(max(nodes)))
    colors.append('#FFCC00')

    # adds pink node
    nodes.append(max(nodes) + 1)
    edges.append((node, max(nodes)))
    labels.append(str(max(nodes)))
    colors.append('#FFCCFF')


if __name__ == "__main__":
    nodes = [0]
    labels = ["0"]
    edges = []
    colors = ['#FF0000']
    graph = Graph(nodes, edges, False)

    i = "wthwth"

    while i != "e":
        show(graph, "tiag.html", colors, labels)
        print("Choose node to transform or e to exit")
        i = input()
        if i == "e":
            break
        elif int(i) > max(nodes):
            print("Incorrect input")
        else:
            t1(nodes, colors, labels, int(i))
            print("Transformation complete")
