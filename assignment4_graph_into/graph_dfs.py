import reverse_graph
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}

graph2 = {'A': ['C', 'H'],
          'B': ['A', 'G'],
          'C': ['D'],
          'D': ['F'],
          'E': ['A', 'I'],
          'F': ['J'],
          'G': ['I'],
          'H': ['F', 'G'],
          'I': ['H'],
          'J': ['C']
          }


def dfs(graph):
    global clock
    clock = 0
    visited = {a: False for a in graph}

    def explore(graph, node):
        visited[node] = True
        print(node)
        for nodei in graph[node]:
            if visited[nodei] == False:
                explore(graph, nodei)
    for node in graph:
        if visited[node] == False:
            explore(graph, node)


graph2R = reverse_graph.reverse_graph(graph2)
print(graph2R)

dfs(graph2R)
