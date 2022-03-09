import numpy
# 白嫖怪 给我爬
# dasgupta Figure 5.9
Graph_dasgupta = {
    'A': {'B': 5, 'C': 6, 'D': 4},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 6, 'B': 1, 'D': 2, 'E': 5, 'F': 3},
    'D': {'A': 4, 'B': 2, 'C': 2, 'F': 4},
    'E': {'C': 5, 'F': 4},
    'F': {'C': 3, 'D': 4, 'E': 4},
}
# dasgupta exercise 5.2
dasgupta_graph_test_Prim = {
    'A': {'B': 1, 'E': 4, 'F': 8},
    'B': {'A': 1, 'C': 2, 'F': 6, 'G': 6},
    'C': {'B': 2, 'D': 3, 'G': 2},
    'D': {'C': 3, 'G': 1, 'H': 4},
    'E': {'A': 4, 'F': 5},
    'F': {'A': 8, 'B': 6, 'E': 5, 'G': 1},
    'G': {'B': 6, 'C': 2, 'D': 1, 'F': 1, 'H': 1},
    'H': {'D': 4, 'G': 1},

}


def my_prims_adjacency_list(Graph, source):
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
    cost = {i: 100000 for i in Graph}
    cost[source] = 0
    heap_cost = {}
    heap_cost = {i: j for i, j in cost.items()}
    # print(previous)
    # print(cost)
    # print(cost)
    num = 1
    while len(heap_cost) != 0:
        u = deap_pop_min(heap_cost)

        for z in Graph[u]:
            print(' ')
            print('step', num, '--------------')
            print('current u is ', u, ' ,z is ', z)

            # print('current heap is ', heap_cost)
            num += 1
            edge_weight = Graph[u][z]
            if z in heap_cost and cost[z] > edge_weight:
                print('cost[', z, ']=', cost[z])
                print('Graph[', u, '][', z, '] is ', Graph[u][z])
                print('apparently cost[', z, '] > Graph[', u, '][', z, ']')
                print('*** update cost and previous ****')
                cost[z] = edge_weight
                previous[z] = u
                # 这一步就是 decrease key，
                heap_cost[z] = edge_weight
                print('current cost is ', cost)
                print('current prev is ', previous)
            else:
                print('cost[', z, '] is ', cost[z])
                print('Graph[', u, '][', z, '] is ', Graph[u][z])
                print('apparently cost[', z, '] < Graph[', u, '][', z, ']')
                print('no update continue')
            # 其实这里少了 decrease key 这一步 decreasekey(H,v)
            # https://stackoverflow.com/questions/9255620/why-does-dijkstras-algorithm-use-decrease-key#:~:text=The%20reason%20for%20using%20decrease,each%20priority%20queue%20balance%20low.
            # The reason for using decrease-key rather than reinserting nodes is to keep the number of nodes in the priority queue small, thus keeping the total number of priority queue dequeues small and the cost of each priority queue balance low.

    return previous


my_prims_adjacency_list(dasgupta_graph_test_Prim, 'A')
