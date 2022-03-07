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

Graph2 = {
    'A': {'B': 5, 'C': 6}, 'B': {}, 'C': {'B': -3}
}


def dijkstra_adjacency_list(Graph, source):
    def deap_pop_min(heap):  # remember the input should be an dictionary
        min_key = None
        min_num = 1000000
        for i, j in heap.items():
            if j < min_num:
                min_num = j
                min_key = i
        heap.pop(min_key)
        return min_key

    previous = {i: None for i in Graph}
    visied = []
    dist = {i: 100000 for i in Graph}
    dist[source] = 0
    heap_dist = {}
    heap_dist = {i: j for i, j in dist.items()}
    print(previous)
    print(dist)
    print(heap_dist)
    while len(heap_dist) != 0:
        u = deap_pop_min(heap_dist)
        visied.append(u)
        for v in Graph[u]:
            if v not in visied:
                edge_length = Graph[u][v]
                if dist[v] > dist[u] + edge_length:
                    dist[v] = dist[u] + edge_length
                    previous[v] = u
                    heap_dist[v] = dist[u] + edge_length
            # 其实这里少了 decrease key 这一步 decreasekey(H,v)
            # https://stackoverflow.com/questions/9255620/why-does-dijkstras-algorithm-use-decrease-key#:~:text=The%20reason%20for%20using%20decrease,each%20priority%20queue%20balance%20low.
            # The reason for using decrease-key rather than reinserting nodes is to keep the number of nodes in the priority queue small, thus keeping the total number of priority queue dequeues small and the cost of each priority queue balance low.
    print(previous)
    return dist


print(dijkstra_adjacency_list(Graph, 'A'))
