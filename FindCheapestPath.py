# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph


def cheapest_path(t, start, finish):
    max_cost = 65536
    vertices = t
    graph = [[0 for column in range(vertices)]
             for row in range(vertices)]

    def print_solution(dist):
        print("Vertex \tDistance from Source")
        for node in range(vertices):
            print(node, "\t", dist[node])

    def min_distance(dist, spt_set):
        """"
         # A utility function to find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
        """

        # Initialize minimum distance for next node
        minimum_distance = max_cost

        min_index = None

        # Search for nearest vertex not in the spt_set
        for v in range(vertices):
            if dist[v] < minimum_distance and spt_set[v] == False:
                minimum_distance = dist[v]
                min_index = v

        return min_index

    def dijkstra(src):
        dist = [max_cost] * vertices
        dist[src] = 0
        spt_set = [False] * vertices

        for cout in range(vertices):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = min_distance(dist, spt_set)

            # Put the minimum distance vertex in the
            # shortest path tree
            spt_set[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(vertices):
                if graph[u][v] > 0 and spt_set[v] == False and \
                        dist[v] > dist[u] + graph[u][v]:
                    dist[v] = dist[u] + graph[u][v]

            return print_solution(dist)

    return dijkstra()


cheapest_path([[1, 9, 1], [2, 9, 1], [2, 1, 1]], (0, 0), (0, 2))
