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


def dfs_v2(graph):
    global clock
    clock = 0
    visited = {a: False for a in graph}
    previsit_num = {i: 0 for i in graph}
    postvisit_num = {i: 0 for i in graph}

    def explore(graph, node):
        global clock
        clock = clock + 1
        previsit_num[node] = clock
        visited[node] = True
        print(node)
        for nodei in graph[node]:
            if visited[nodei] == False:
                explore(graph, nodei)
        clock = clock + 1
        postvisit_num[node] = clock
    for node in graph:
        if visited[node] == False:
            explore(graph, node)

    print(previsit_num)
    print(postvisit_num)


GR = {
    'A': ['E'],
    'B': ['A'],
    'C': ['B'],
    'D': ['A', 'G'],
    'E': ['B'],
    'F': ['C', 'H'],
    'G': ['H'],
    'H': ['D', 'E', 'I'],
    'I': ['F', 'H'],

}

dfs_v2(GR)
