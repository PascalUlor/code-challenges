"""
cost formula
if (dist(u) + cost(u,v)) > dist(v):
    d
"""
from pprint import pprint as pp

# build the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

pp(graph)

# hash table for the cost
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# hash table for parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


def dijkstra(costs):
    """Implementation of the Dijkstra algorithm
    Arguments:
        costs {dict} -- costs of the nodes
    """
    # to check if a node has been processed
    processed = []

    def find_lowest_cost_node(costs):
        """Find the node with the lowest cost
        Arguments:
        costs {dict} -- costs of the nodes
        Returns:
            dict -- the lowest cost node
        """
        lowest_cost = float("inf")
        lowest_cost_node = None

        for node in costs:
            cost = costs[node]

            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node

    node = find_lowest_cost_node(costs)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost = cost + neighbors[n]

            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)


# find the shortest possible path to the finish
dijkstra(costs)
# print the costs to views to view the
pp(costs)