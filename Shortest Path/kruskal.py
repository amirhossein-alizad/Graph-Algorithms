class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def addEdge(self, u, v, w):
        self.edges.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] <= rank[yroot]:
            parent[xroot] = yroot
            rank[yroot] += 1
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def make_graph(self, n, arr):
        for i in range(n):
            for j in range(n):
                if i < j and arr[i][j] <= arr[j][i]:
                    g.addEdge(i, j, arr[i][j])
                if i > j and arr[i][j] < arr[j][i]:
                    g.addEdge(i, j, arr[i][j])

    def evaluate_table(self, res, table):
        for i in res:
            table[i[0]][i[1]] = 0
            if arr[i[0]][i[1]] == arr[i[1]][i[0]]:
                table[i[1]][i[0]] = 0

    def check_for_cycle_and_mst(self, parent, rank, cycle, res):
        weight = 0
        temp = []
        global last_weight
        for i in self.edges:
            u, v, w = i
            if i is self.edges[0]:
                last_weight = self.edges[0][2]
            if last_weight != w:
                for t in temp:
                    res.append(t)
                    self.union(parent, rank, t[0], t[1])
                temp = []
            x = self.find(parent, u)
            y = self.find(parent, v)
            cycle_x = self.find(cycle, u)
            cycle_y = self.find(cycle, v)
            if x != y:
                if cycle_x != cycle_y:
                    weight += w
                    last_weight = w
                temp.append([u, v])
            self.union(cycle, rank, u, v)
        for t in temp:
            res.append(t)
        return weight

    def KruskalMST(self, res):
        self.edges = sorted(self.edges, key=lambda item: item[2])
        parent = []
        cycle = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            cycle.append(node)
            rank.append(0)
        weight = self.check_for_cycle_and_mst(parent, rank, cycle, res)
        return weight
