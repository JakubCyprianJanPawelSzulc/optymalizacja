graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]


def fleury(graph, start):
    n = len(graph)
    visited = [False] * n
    path = []
    current_vertex = start

    while True:
        path.append(current_vertex)
        if len(path) == n:
            break

        for i in range(n):
            if graph[current_vertex][i] != 0 and not visited[i]:
                break

        if len(path) == n - 1:
            path.append(i)
            break

        path_weight = 0
        for j in range(n):
            if graph[current_vertex][j] != 0:
                path_weight += graph[current_vertex][j]

        for j in range(n):
            if graph[current_vertex][j] != 0:
                graph[current_vertex][j] = 0
                graph[j][current_vertex] = 0
                break

        visited[current_vertex] = True
        current_vertex = i

    return path

def dijkstra(graph, start, end):
    n = len(graph)
    visited = [False] * n
    distance = [float("inf")] * n
    distance[start] = 0

    for _ in range(n):
        min_distance = float("inf")
        u = -1

        for i in range(n):
            if not visited[i] and distance[i] < min_distance:
                min_distance = distance[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        for v in range(n):
            if not visited[v] and graph[u][v] != 0 and distance[u] + graph[u][v] < distance[v]:
                distance[v] = distance[u] + graph[u][v]

    return distance[end]

def minimum_weight_perfect_matching(graph):
    n = len(graph)
    visited = [False] * n
    matching = []
    start_vertex = 0
    visited[start_vertex] = True

    while len(matching) < n - 1:
        min_weight = float("inf")
        u, v = -1, -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if not visited[j] and graph[i][j] != 0 and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        u = i
                        v = j

        if u != -1 and v != -1:
            matching.append((u, v, min_weight))
            visited[v] = True
    return matching

def chinese_postman_path(grahp,start):
    odd_degree_vertices = []
    for i in range(len(graph)):
        if sum(graph[i]) % 2 != 0:
            odd_degree_vertices.append(i)

    G_prime = [[0 for _ in range(len(odd_degree_vertices))] for _ in range(len(odd_degree_vertices))]
    for i in range(len(odd_degree_vertices)):
        for j in range(len(odd_degree_vertices)):
            G_prime[i][j] = dijkstra(graph, odd_degree_vertices[i], odd_degree_vertices[j])

    matching = minimum_weight_perfect_matching(G_prime)

    for u, v, _ in matching:
        matching[u] = (odd_degree_vertices[u], odd_degree_vertices[v])

    eulerian_cycle = fleury(graph, start)
    eulerian_cycle = eulerian_cycle[:-1]
    eulerian_cycle = eulerian_cycle + [start]

    path = []
    for vertex in eulerian_cycle:
        if vertex not in path:
            path.append(vertex)

    return path

if __name__ == "__main__":
    path = chinese_postman_path(graph, 0)
    total_weight = 0
    for i in range(len(path) - 1):
        total_weight += graph[path[i]][path[i + 1]]
    print(f"Ścieżka chińskiego listonosza: {path}")
    print(f"Całkowita waga: {total_weight}")