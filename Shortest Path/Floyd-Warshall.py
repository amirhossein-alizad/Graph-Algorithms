def floydWarshall(graph, V):
    dist = [[0 for i in range(V)]for j in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
