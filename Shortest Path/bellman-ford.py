mission id: 3747913

global maximum
maximum = 2 * (10 ** 9)
class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def BellmanFord(self, src, dist):
        dist[src] = 0
        for i in range(self.V - 1):
            flag = 0
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    flag = 1
            if flag == 0:
                break
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                return -1
        return 0
