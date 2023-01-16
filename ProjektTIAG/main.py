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
    # adds yellow and pink node, connected to red node
    if len(node)!=1:
        print("Incorrect amount of input nodes")
        return
    if colors[node[0]]!='#FF0000':
        print("Incorrect input for this transformation")
    #adds yellow node
    if len(nodes)==0:
        print("Incorrect input")
    else:
        nodes.append(max(nodes) + 1)
    edges.append((node[0], max(nodes)))
    labels.append(str(max(nodes)))
    colors.append('#FFCC00')

    # adds pink node
    nodes.append(max(nodes) + 1)
    edges.append((node[0], max(nodes)))
    labels.append(str(max(nodes)))
    colors.append('#FFCCFF')
    print("Transformation complete")

def t0(nodes, colors, labels, node):
    #adds one free red node
    if len(node)>0:
        print("Incorrect amount of input nodes")
    if len(nodes) == 0:
        nodes.append(0)
    else:
        nodes.append(max(nodes) + 1)
    labels.append(str(max(nodes)))
    colors.append(color("red"))
    print("Transformation complete")


def t2(nodes, colors, labels, t_nodes):
    # adds yellow node between red node connected to pink node
    if len(t_nodes) != 2:
        print("Incorrect amount of input nodes")
        return
    if colors[t_nodes[0]] != color("red") or colors[t_nodes[1]] != color("pink"):
        print("Incorrect input for this transformation")

    if len(nodes) == 0:
        print("Incorrect input")
        return
    if (t_nodes[0],t_nodes[1]) not in edges and (t_nodes[1],t_nodes[0]) not in edges:
        print("Incorrect input (edge doesn't exists)")

    #adding pink node
    colors.append(color("yellow"))
    nodes.append(max(nodes) + 1)
    labels.append(str(max(nodes)))
    #creating new edges
    edges.append((t_nodes[0], max(nodes)))
    edges.append((t_nodes[1], max(nodes)))
    #deleting old edge
    if (t_nodes[0],t_nodes[1]) in edges:
        edges.remove((t_nodes[0],t_nodes[1]))
    else:
        edges.remove((t_nodes[1], t_nodes[0]))

    print("Transformation complete")

def t3(nodes, colors, labels, t_nodes):
    # disconnects yellow node from red node
    if len(t_nodes) != 2:
        print("Incorrect amount of input nodes")
        return
    if colors[t_nodes[0]] != color("red") or colors[t_nodes[1]] != color("yellow"):
        print("Incorrect input for this transformation")

    if len(nodes) == 0:
        print("Incorrect input")
        return
    if (t_nodes[0],t_nodes[1]) not in edges and (t_nodes[1],t_nodes[0]) not in edges:
        print("Incorrect input (edge doesn't exists)")

    #deleting old edge
    if (t_nodes[0],t_nodes[1]) in edges:
        edges.remove((t_nodes[0],t_nodes[1]))
    else:
        edges.remove((t_nodes[1], t_nodes[0]))

    print("Transformation complete")

if __name__ == "__main__":
    nodes = []
    labels = []
    edges = []
    colors = []
    graph = Graph(nodes, edges, False)

    nodes_to_transform = []
    i=1

    while i != "e":
        show(graph, "tiag.html", colors, labels)
        print("Nodes to transform: ", nodes_to_transform)
        print("Choose one more node to transform, transformation name to transform chosen nodes or e to exit")
        i= input()

        match i:
            case "e":
                break
            case "t0":
                t0(nodes, colors, labels, nodes_to_transform)
                nodes_to_transform = []
            case "t1":
                t1(nodes, colors, labels, nodes_to_transform)
                nodes_to_transform=[]
            case "t2":
                t2(nodes, colors, labels, nodes_to_transform)
                nodes_to_transform = []
            case "t3":
                t3(nodes, colors, labels, nodes_to_transform)
                nodes_to_transform = []
            case _:
                if not i.isnumeric() : #checking if input is a number:
                    print("Incorrect input")
                else:
                    nodes_to_transform.append(int(i))

