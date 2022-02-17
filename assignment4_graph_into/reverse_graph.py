graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}


t = 0


def reverse_graph(graph):
    global t
    t = 0
    graphr = {key: [] for key in graph}
    # print(graphr)
    for key in graph:
        for i in graph[key]:
            graphr[i].append(key)
            t = t+1

    return graphr


# print(reverse_graph(graph))
# len(edge)=m len(node)=n    T=O(n+m)
# t=8 which is the number of edge apparently, It's linear time
