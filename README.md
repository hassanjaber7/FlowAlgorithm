# FlowAlgorithm
Our main project to design and implement an algorithm for calculating the edge 
connectivity of a simple undirected graph. 
An edge connectivity of a graph is the minimum number of edges whose removal will 
disconnect the graph. 

One of the usage of flow network is to find the maximum flow using the famous 
“Ford-Fulkerson Algorithm”, so let’s explain what’s a flow network in graph theory, 
and why should we calculate the maximum flow of a graph in order to find the edge 
connectivity of a graph.
1) A flow of graph is when we have a directed graph where each edge has a 
capacity and each edge receives a flow, the amount of the edge flow cannot be 
more than the edge capacity. And the flow network graph always starts with a 
source node and ends with a sink node.
2) A maximum flow is the maximum amount of flow that the graph would allow from 
source node to sink node. Hence we are going to calculate the maximum flow using 
“Ford-Fulkerson Algorithm”.
3) Max-flow Min-cut Theorem: The maximum flow in any graph should always be 
equal to the number of minimum cuts (edge connectivity). That’s why we are going 
to calculate the max-flow using “Ford-Fulkerson Algorithm”.
4) Ford-Fulkerson Algorithm: It’s an algorithm to find the maximum flow of a flow 
network by finding an “Augmenting path”.
An augmenting path is basically a path whose edges are(Better explanation is 
found in the next section 2.2):
 a. non-full forward
 b. non-empty backward
