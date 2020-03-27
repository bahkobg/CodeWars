def adjacent_nodes(pos, t):
    """
    Calculate adjacent nodes in given matrix (toll_map)
    :param pos: Takes tuple -> (x,y) coordinates of the X x Y matrix 
    :param t: Matrix -> toll_map
    :return: A dict {(x1, y1) : "right", (x2, y2): "left", ... } of all possibly adjacent squares which fall into the matrix dimensions
    """
    possible_adj_nodes = {(0, 1): "right", (0, -1): "left", (1, 0): "up", (-1, 0): "down"}
    adj_nodes = {}
    least_cost_node = {}
    for move in possible_adj_nodes.keys():
        if (len(t) > (move[0] + pos[0]) >= 0) and (len(t[0]) > (move[1] + pos[1]) >= 0):
            adj_nodes.update({(move[0] + pos[0], move[1] + pos[1]): possible_adj_nodes[move]})
            least_cost_node.update({(move[0] + pos[0], move[1] + pos[1]): t[move[0] + pos[0]][move[1] + pos[1]]})
    least = [k for k,v in least_cost_node.items() if v == min(least_cost_node.values())]
    return adj_nodes, least


def cheapest_path(t, start, finish):
    nodes = {}
    directions = {}
    unvisited_nodes = []
    current_node = start
    next_node_list = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if (i, j) != finish:
                unvisited_nodes.append((i, j))
            nodes.update({(i, j): 65536})
            directions.update({(i, j): ''})
    nodes[start] = 0

    for i in range(30):
        distance = t[current_node[0]][current_node[1]]

        print("UNVISITED NODES -> {}".format(unvisited_nodes))
        print("THIS IS CURRENT NODE -> {}".format(current_node))
        print("THIS IS CURRENT NODE DISTANCE-> {}".format(distance))

        print(adjacent_nodes(current_node, t)[0].items())
        print(adjacent_nodes(current_node, t)[1])
        for node, direction in adjacent_nodes(current_node, t)[0].items():

            if node in unvisited_nodes and node not in next_node_list:
                next_node_list.append(node)
            if nodes[node] > distance + nodes[current_node]:
                nodes[node] = distance + nodes[current_node]
                directions[node] = ' ' + direction + directions[current_node]
                if node not in unvisited_nodes and node not in next_node_list and node != finish:
                    unvisited_nodes.append(node)

        print("NEXT NODE LIST --> {}".format(next_node_list))
        if current_node in unvisited_nodes:
            unvisited_nodes.remove(current_node)
        if next_node_list:
            current_node = next_node_list[0]
        if current_node in next_node_list:
            next_node_list.remove(current_node)

        print("UNVISITED NODES -> {}".format(unvisited_nodes))
        print("THIS IS CURRENT NODE -> {}".format(current_node))
        print("THIS IS CURRENT NODE DISTANCE-> {}".format(distance))
        print(nodes)
        print(directions)
        print("********************************************************")

    return directions[finish].split(' ')[1:]


print(cheapest_path(
    [[1, 1, 1, 1, 1, 1, 1], [30, 30, 30, 30, 30, 30, 1], [1, 1, 1, 1, 1, 30, 1], [1, 30, 30, 30, 1, 30, 1], [1, 30, 1, 1, 1, 30, 1], [1, 30, 30, 30, 30, 30, 1],
     [1, 1, 1, 1, 1, 1, 1]], (0, 0), (4, 2)))
