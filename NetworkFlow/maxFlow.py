global MAX
MAX = 2**31 - 1
class Graph():
    def __init__(self, graph, s, t):
        self.source = s
        self.tank = t
        self.graph = graph
        self.row = len(graph)
        self.level = [0 for i in range(len(graph))]
        self.first_path_node = [0 for i in range(len(graph))]
        self.flow_graph = [[0 for i in range(len(graph))] for j in range(len(graph))]

    def set_levels(self):
        for i in range(self.row):
            self.level[i] = 0
        self.level[self.source] = 1
    
    def set_first_path_node(self):
        for i in range(self.row):
            self.first_path_node[i] = 0

    def Bfs(self):
        queue = [self.source]
        self.set_levels()  
        while queue:
            curr_node = queue.pop(0)
            for i in range(self.row):
                    if (self.flow_graph[curr_node][i] < self.graph[curr_node][i]) and (self.level[i] == 0):
                            self.level[i] = self.level[curr_node] + 1
                            queue.append(i)
        return self.level[self.tank] > 0

    def Dfs(self, curr_node, curr_flow):
        if curr_node == self.row - 1:
            return curr_flow
        flow = 0
        for i in range(self.first_path_node[curr_node], self.row):
            if (self.level[i] == self.level[curr_node] + 1) and (self.flow_graph[curr_node][i] < self.graph[curr_node][i]):
                flow = self.Dfs(i, min(curr_flow,self.graph[curr_node][i] - self.flow_graph[curr_node][i]))
                self.flow_graph[curr_node][i] += flow
                self.flow_graph[i][curr_node] -= flow
                self.first_path_node[curr_node] = i
                if flow:
                    return flow
        return flow

    def MaxFlow(self):
        Mflow = 0
        while(self.Bfs()):
            self.set_first_path_node()
            Aflow = self.Dfs(self.source, MAX)
            while Aflow:
                Mflow += Aflow
                Aflow = self.Dfs(self.source ,MAX)
        return Mflow
