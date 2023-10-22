def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

def DFS(graph, v, visited):
    visited.add(v)
    print(v, end=' ')

    for neighbor in graph[v]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

def DFS_spanning_tree(graph, v, visited, parent):
    visited.add(v)

    for neighbor in graph[v]:
        if neighbor not in visited:
            parent[neighbor] = v
            DFS_spanning_tree(graph, neighbor, visited, parent)

def DFS_driver(graph, v):
    visited = set()
    DFS(graph, v, visited)

def DFS_spanning_tree_driver(graph, v):
    visited = set()
    parent = {}
    parent[v] = None
    DFS_spanning_tree(graph, v, visited, parent)
    return parent

graph = {}
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 3)
add_edge(graph, 3, 3)

print("Przejście DFS zaczynając od wierzchołka 2:")
DFS_driver(graph, 2)

print("\nDrzewo spinające DFS zaczynając od wierzchołka 2:")
parent = DFS_spanning_tree_driver(graph, 2)
for key, value in parent.items():
    print(key, "->", value)
