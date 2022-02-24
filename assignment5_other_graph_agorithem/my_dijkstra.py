# procedure
# Input:
# Output:
# dijkstra(G, l, s)
# Graph G = (V, E), directed or undirected;
# positive edge lengths {le : e ∈ E}; vertex s ∈ V
# For all vertices u reachable from s,
# dist(u) is set to the distance from s to u.
# for all u ∈ V :
#       dist(u) = ∞
# prev(u) = nil
# dist(s) = 0
# H = makequeue (V ) (using dist-values as keys)
# while H is not empty:
# u = deletemin(H)
# for all edges (u, v) ∈ E:
# if dist(v) > dist(u) + l(u, v):
#   dist(v) = dist(u) + l(u, v)
#   prev(v) = u decreasekey(H, v)
import numpy
Graph = {
    'A': {'B': 4, 'C': 2}, 'B': {'C': 3, 'D': 2, 'E': 3}, 'C': {'B': 1, 'D': 4, 'E': 5}, 'D': {}, 'E': {'D': 1}
}


def dijkstra_adjacency_list(Graph):
    def deap_pop_min(heap):  # remember the input should be an dictionary
        min_key = None
        min_num = 100000
        for i, j in heap.items():
            if j < min_num:
                min_num = j
                min_key = i
        heap.pop(min_key)
        return min_key

    # def update_heap(heap,dist):
    #     for
    previous = {i: None for i in Graph}

    dist = {i: 100000 for i in Graph}
    dist['A'] = 0
    heap_dist = {}
    heap_dist = {i: j for i, j in dist.items()}
    while len(heap_dist) != 0:
        u = deap_pop_min(heap_dist)

        for v in Graph[u]:

            edge_length = Graph[u][v]
            if dist[v] > dist[u] + edge_length:
                dist[v] = dist[u] + edge_length
                previous[v] = u
            # decreasekey(H, v),其实就是update heap_dist
                heap_dist[v] = dist[u] + edge_length
    return dist


print(dijkstra_adjacency_list(Graph))
