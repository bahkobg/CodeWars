class SPF():

    def __init__(self, graph, start, finish):
        self.graph = graph
        self.start = start
        self.current_node = finish
        self.unvisited_nodes = {}
        self.nodes = {}
        self.next_node = []
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                self.unvisited_nodes.update({(i, j): 65536})
                self.nodes.update({(i, j): 65536})
        self.nodes.update({finish: 0})

    def __str__(self):
        _line = ' -----' * len(self.graph[0]) + ' \n'
        _map = _line
        for row in self.graph:
            _map += '|  ' + ' '.join(str(x) + '   |' if len(str(x)) == 1 else str(x) + '  |' for x in row) + ' \n' + _line
        return _map

    def _valid_moves(self, pos):
        _possible_moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        _valid_moves = []
        for move in _possible_moves:
            if ((len(self.graph) - 1) >= (move[0] + pos[0]) >= 0) and ((len(self.graph[0]) - 1) >= (move[1] + pos[1]) >= 0):
                _valid_moves.append((move[0] + pos[0], move[1] + pos[1]))
        return _valid_moves

    def run_spf(self, to):
        _distance = self.nodes[self.current_node]
        print("CURRENT NODE {} DISTANCE -> {}".format(self.current_node, _distance))

        for node in self._valid_moves(self.current_node):  # Find node's neighbours
            self.next_node.append(node)
            if self.nodes[node] > _distance + self.graph[node[0]][node[1]]:
                print("NODE {} HAS DISTANCE {}".format(node, self.nodes[node]))
                self.nodes[node] = _distance + self.graph[node[0]][node[1]]
                print("FOR NODE {} -> UPDATED DISTANCE IS {}".format(node, self.nodes[node]))

        del self.unvisited_nodes[self.current_node]
        self.current_node = self.next_node[0]
        self.next_node.remove(self.current_node)
        print("\n")
        print("**************** NEXT ITERATION ***********")


s = SPF([[1, 9, 1], [2, 9, 1], [2, 1, 1]], (0, 0), (0, 2))
s.run_spf((0, 2))
s.run_spf((0, 2))



print(s)
