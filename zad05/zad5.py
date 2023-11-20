import heapq
from collections import defaultdict 

def add_edge(graph, edges, u, v, w):
    graph[u].append((v, w))
    graph[v].append((u, w))
    edges.add((u, v, w))
    edges.add((v, u, w))

def eulerian_cycle(graph):
    temp_graph = {vertex: list(neighbors) for vertex, neighbors in graph.items()}
    stack = []
    cycle = []
    total_weight = 0
    current_vertex = next(iter(graph))
    stack.append(current_vertex)
    while stack:
        if temp_graph[current_vertex]:
            next_vertex, w = temp_graph[current_vertex].pop()
            total_weight += w
            temp_graph[next_vertex] = [(v, weight) for v, weight in temp_graph[next_vertex] if v != current_vertex]
            current_vertex = next_vertex
            stack.append(current_vertex)
        else:
            cycle.append(stack.pop())
            if stack:
                current_vertex = stack[-1]
    cycle.reverse()
    return cycle, total_weight

def dijkstra(graph, start, end):
    min_dist = {vertex: float('infinity') for vertex in graph}
    min_dist[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > min_dist[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight

            if distance < min_dist[neighbor]:
                min_dist[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return min_dist[end]

def find_eulerian_cycle(edges):
    graph = defaultdict(list)
    edge_set = set()
    for edge in edges:
        add_edge(graph, edge_set, *edge)

    odd_vertex_num = 0
    odd_vertex_list = []
    #czy jest Eulerianer
    for i in graph:
        if len(graph[i]) % 2 != 0:
            odd_vertex_num += 1
            for j in graph[i]:
                odd_vertex_list.append([i, j[0], j[1]])
    if odd_vertex_num == 0:
        return eulerian_cycle(graph)
    #czy jest Halbeulerianisch
    elif odd_vertex_num == 2:
        odd_vertices = [vertex for vertex in graph if len(graph[vertex]) % 2 != 0]
        min_weight_path = dijkstra(graph, odd_vertices[0], odd_vertices[1])
        eulerian_cycle_result = eulerian_cycle(graph)
        return eulerian_cycle_result, min_weight_path
    else:
        for i in odd_vertex_list:
            if i[0] > i[1]:
                tmp = i[0]
                i[0] = i[1]
                i[1] = tmp

        odd_vertex_list = [element for element in odd_vertex_list if odd_vertex_list.count(element) > 1]
        add_edge_list = []
        for element in reversed(odd_vertex_list):
            if element not in add_edge_list:
                add_edge_list.insert(0, element)

        for u, v, w in add_edge_list:
            add_edge(graph, edge_set, u, v, w)

        return eulerian_cycle(graph)

edges_eulerian = [(1, 2, 3), (2, 3, 1), (3, 1, 2)]
print("Eulerian Graph:")
print(find_eulerian_cycle(edges_eulerian))
print("\n")

edges_semi_eulerian = [(1, 2, 3), (2, 3, 1), (3, 4, 5), (4, 1, 2)]
print("Semi-Eulerian Graph:")
print(find_eulerian_cycle(edges_semi_eulerian))
print("\n")

edges_not_eulerian = [(1, 2, 3), (2, 3, 1), (3, 4, 5)]
print("Non-Eulerian Graph:")
print(find_eulerian_cycle(edges_not_eulerian))
