import networkx as nx
import numpy as np
from itertools import permutations

def min_perfect_matching(G):
    maximal = list(nx.maximal_matching(G))
    min_weight = np.inf
    min_weight_matching = []
    for perm in permutations(maximal):
        weight = sum([G.edges[e]['weight'] for e in perm])
        if weight < min_weight:
            min_weight = weight
            min_weight_matching = perm

    is_perfect = nx.is_perfect_matching(G, min_weight_matching)
    if not is_perfect:
        raise Exception('Not perfect matching')

    return min_weight_matching 

def christofides(G):
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

    return hamiltonian_cycle

G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5])
G.add_weighted_edges_from([(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 2, 4), (1, 3, 5), (2, 3, 6), (2, 4, 7), (2, 5, 8), (3, 4, 9), (3, 5, 10), (4, 5, 11)])

print(christofides(G))
