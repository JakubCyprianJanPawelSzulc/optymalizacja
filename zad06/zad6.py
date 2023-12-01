import networkx as nx
import numpy as np
from itertools import permutations

def triangle_graph(G):
    for node in G.nodes():
        neighbors = list(G.neighbors(node))
        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                edge1 = G[node][neighbors[i]]['weight']
                edge2 = G[node][neighbors[j]]['weight']
                third_edge = G[neighbors[i]][neighbors[j]]['weight']
                if not triangle(edge1, edge2, third_edge):
                    return False
    return True

def triangle(edge1, edge2, third_edge):
    return edge1 + edge2 >= third_edge and edge1 + third_edge >= edge2 and edge2 + third_edge >= edge1


def min_perfect_matching(G):
    # maximal = list(nx.maximal_matching(G))
    # min_weight = np.inf
    # min_weight_matching = []
    # for perm in permutations(maximal):
    #     weight = sum([G.edges[e]['weight'] for e in perm])
    #     if weight < min_weight:
    #         min_weight = weight
    #         min_weight_matching = perm

    # is_perfect = nx.is_perfect_matching(G, min_weight_matching)
    # if not is_perfect:
    #     raise Exception('Not perfect matching')

    # return min_weight_matching

    is_perfect = nx.is_perfect_matching(G, nx.min_weight_matching(G))
    if not is_perfect:
        raise Exception('Not perfect matching')
    return nx.min_weight_matching(G)

def christofides(G):

    if not triangle_graph(G):
        raise Exception('Graph does not satisfy triangle condition')
    
    #1
    T = nx.minimum_spanning_tree(G)
    #2
    M = min_perfect_matching(G.subgraph([v for v, d in T.degree if d % 2 == 1]))    
    
    #3
    H = nx.MultiGraph(T)
    H.add_edges_from(M)

    #4
    eulerian_circuit = list(nx.eulerian_circuit(H))
    #5
    visited = set()
    hamiltonian_cycle = []
    for edge in eulerian_circuit:
        u, v = edge
        if u not in visited:
            hamiltonian_cycle.append(u)
            visited.add(u)

    # można dodać ostatni wierzchołek aby zamknąć cykl hamiltona tylko nie wiem czy to jest potrzebne
    # hamiltonian_cycle.append(hamiltonian_cycle[0])

    weight = 0
    for i in range(len(hamiltonian_cycle) - 1):
        weight += G[hamiltonian_cycle[i]][hamiltonian_cycle[i + 1]]['weight']
    

    return hamiltonian_cycle, weight

G = nx.Graph()
#poniżej nie działa bo najwyraźniej nie jest spełniony warunek trójkąta
# G.add_nodes_from([0, 1, 2, 3, 4, 5])
# G.add_weighted_edges_from([(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 4, 7), (2, 5, 8), (3, 4, 9), (3, 5, 10), (4, 5, 11)])

#to działa bo spełniony jest warunek trójkąta
# G.add_nodes_from([0, 1, 2, 3])
# G.add_weighted_edges_from([(0, 1, 1), (0, 2, 1), (0, 3, 1), (1, 2, 1), (1, 3, 1), (2, 3, 1)])

#inny spełniający warunek trójkąta
# G.add_nodes_from([0, 1, 2, 3])
# G.add_weighted_edges_from([(0, 1, 2), (0, 2, 3), (0, 3, 2), (1, 2, 1), (1, 3, 2), (2, 3, 1)])

#jeszcze inny bardziej skomplikowany spełniający warunek trójkąta
G.add_nodes_from([0, 1, 2, 3, 4])
G.add_weighted_edges_from([(0,1,1),(0,2,1),(0,3,2),(0,4,3),(1,2,2),(1,3,2),(1,4,3),(2,3,3),(2,4,2),(3,4,2)])

print(christofides(G))
