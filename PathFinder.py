def path_finder(maze):
    maze = maze.split('\n')
    finish = (len(maze) - 1, len(maze) - 1)
    unvisited_nodes = []
    for x in range(len(maze)):
        unvisited_nodes.extend([(x, y) for y in range(len(maze)) if maze[x][y] != 'W'])
    print(unvisited_nodes)

    def distance(pos1, pos2):
        return (pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2

    def valid_moves(pos):
        valid_moves = {}
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for m in moves:
            if len(maze) > (pos[0] + m[0]) >= 0 and len(maze) > (pos[1] + m[1]) >= 0:
                if maze[pos[0] + m[0]][pos[1] + m[1]] != 'W' and (pos[0] + m[0], pos[1] + m[1]) in unvisited_nodes:
                    valid_moves.update({distance((pos[0] + m[0], pos[1] + m[1]), finish): (pos[0] + m[0], pos[1] + m[1])})
        return valid_moves if valid_moves else False

    if valid_moves((len(maze) - 1, len(maze) - 1)):
        penultimate_hops = valid_moves((len(maze) - 1, len(maze) - 1)).values()
    else:
        return False

    next_node = [(0, 0)]
    while next_node:
        if (len(maze) - 1, len(maze) - 1) not in unvisited_nodes:
            return True
        elif all(elem not in unvisited_nodes for elem in penultimate_hops):
            return True
        if valid_moves(next_node[0]):
            for k,m in sorted(valid_moves(next_node[0]).items()):
                if m not in next_node:
                    next_node.insert(k, m)
            if next_node[0] in unvisited_nodes:
                unvisited_nodes.remove(next_node[0])
            if next_node[0]:
                del next_node[0]
        else:
            return False

    return False


c = "\n".join([
    "...",
    "W.W",
    "..."
])
print(path_finder(c))
print('debug')
