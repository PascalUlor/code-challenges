"""
node = find_lowest_cost_node(costs) that you haven’t processed yet.
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): Go through all the neighbors of this node.
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost 
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

"""