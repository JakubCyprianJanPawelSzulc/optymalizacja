import networkx as nx
import matplotlib.pyplot as plt

def cpm(graph):
    G = nx.DiGraph(graph)

    #2
    if not nx.is_directed_acyclic_graph(G):
        raise ValueError("Podany graf nie jest acykliczny.")

    #3
    earliest_start = {node: 0 for node in G.nodes}
    for node in nx.topological_sort(G):
        for successor in G.successors(node):
            earliest_start[successor] = max(earliest_start[successor], earliest_start[node] + G[node][successor]['duration'])

    #4
    latest_start = {node: earliest_start[node] for node in G.nodes}
    for node in reversed(list(nx.topological_sort(G))):
        for predecessor in G.predecessors(node):
            latest_start[predecessor] = min(latest_start[predecessor], latest_start[node] - G[predecessor][node]['duration'])

    #5
    critical_path = [node for node in G.nodes if earliest_start[node] == latest_start[node]]

    return earliest_start, latest_start, critical_path, G

def visualize_graph(graph):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
    edge_labels = {(i, j): G[i][j]['duration'] for i, j in G.edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

def gantt_chart(graph, earliest_start, critical_path):
    sorted_nodes = list(nx.topological_sort(graph))
    start_times = [earliest_start[node] for node in sorted_nodes]

    fig, ax = plt.subplots()

    for i, node in enumerate(sorted_nodes):
        color = 'red' if node in critical_path else 'blue'
        duration = 0 if not graph[node] else list(graph[node].values())[0]['duration']
        ax.barh(node, duration, left=start_times[i], color=color)

    ax.set_xlabel('Czas')
    ax.set_ylabel('Zadania')
    ax.set_title('Diagram Gantta')

    plt.show()
    
graph = {
    'A': {'B': {'duration': 3}, 'C': {'duration': 2}},
    'B': {'D': {'duration': 4}},
    'C': {'D': {'duration': 2}},
    'D': {}
}

earliest_start, latest_start, critical_path, G = cpm(graph)

print("Najwcześniejsze czasy rozpoczęcia:", earliest_start)
print("Najpóźniejsze czasy rozpoczęcia:", latest_start)
print("Ścieżka krytyczna:", critical_path)

visualize_graph(graph)
gantt_chart(G, earliest_start, critical_path)
