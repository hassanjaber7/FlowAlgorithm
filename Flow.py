from collections import defaultdict
import sys

# check if the input and output files are in the arguments

if len(sys.argv) < 3:
    print("Please provide an input file name and output file name as a command line argument.")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]
try:
    with open(input_file) as f:
        lines = f.readlines()
    f.close()

except FileNotFoundError:
    print(
        f"The file {input_file} was not found!! Please enter an input file that already exists..")
    sys.exit()
except:
    print(f"Error: An error occurred while reading the file {input_file}.")
    sys.exit()

# reading the vertices and converting them into a list
n = lines.pop(0)
n = n.strip("\n")
n = n.strip("[]")
n = n.replace(" ", "")
nodes = n.split(",")


# reading the edges and convering it into a 2 dimensional list
e = lines.pop(0)
e = e.strip("\n")
e = e.replace("[", "")
e = e.replace("]", "")
e = e.replace(" ", "")
nodes_of_edges = e.split(",")
all_pairs = []

for i in range(0, len(nodes_of_edges), 2):
    if i < len(nodes_of_edges)-1:
        all_pairs.append([nodes_of_edges[i], nodes_of_edges[i+1]])

print(nodes)
print(all_pairs)


list_of_sink_nodes = []
list_of_max_flows = []
global source_node
global flow

# graph class


class Graph:
    def __init__(self, Nodes):
        self.nodes = Nodes
        self.adj_graph = {}

        for node in self.nodes:
            self.adj_graph[node] = []

    def print_adj(self):
        for node in self.nodes:
            print(node, "->", self.adj_graph[node])

    def add_edge(self, u, v):

        self.adj_graph[u].append(v)
        self.adj_graph[v].append(u)


graph = Graph(nodes)
network = Graph(nodes)

# printing the whole graph
for u, v in all_pairs:
    graph.add_edge(u, v)
graph.print_adj()

# clone the network from the graph
network = graph


# construct a network from the undirected graph
def transformToNetwork(network):
    global source_node
    minDegree = 1000_000

# assign a source node
    for i in network.adj_graph:

        if len(network.adj_graph[i]) < minDegree:
            minDegree = len(network.adj_graph[i])
            source_node = i


# assign all sink nodes
    for i in nodes:
        if i != source_node:
            list_of_sink_nodes.append(i)


# Construct the network
transformToNetwork(network)


def ford_fulkerson_alike(graph, s, t):

    # initialise the flow to 0
    flow = 0

    # initialize the residual graph

    residual = defaultdict(defaultdict)
    for u in graph.adj_graph:
        for v in graph.adj_graph[u]:
            residual[u][v] = 1
            residual[v][u] = 1

    # keep finding augmenting path as long as it exists
    while True:
        # run bfs to find an augmenting path
        queue = [s]
        parent = {s: None}

        while queue:
            u = queue.pop(0)
            for v, c in residual[u].items():
                if v not in parent and c > 0:
                    parent[v] = u
                    queue.append(v)
        # check if we reached the sink
        if t not in parent:
            break

        v = t
        while v != s:
            u = parent[v]

            v = u
        # update the flow and capacities
        v = t
        while v != s:
            u = parent[v]
            residual[u][v] -= 1
            residual[v][u] += 1
            v = u
        flow += 1

    return flow


def FindEdgeConnectivity(graph):

    # we take each case of the network for different sink nodes
    for t in list_of_sink_nodes:

        flow_of_network = ford_fulkerson_alike(graph, source_node, t)
        list_of_max_flows.append(flow_of_network)

    return min(list_of_max_flows)


# writing the final result that represent the edge connectivity into the output file
edgeConnectivity = FindEdgeConnectivity(network)
print(edgeConnectivity)
with open(output_file, "w") as f:
    if edgeConnectivity == 0:
        f.write(str(edgeConnectivity) + "\n")
        f.write("The graph you entered is already disconnected...")
    else:
        f.write(str(edgeConnectivity))
f.close()
