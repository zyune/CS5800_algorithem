# apparently

# for nodei in graph:
#     for nodej in graph:
#         if there is no edge between nodej and node i:
#             put nodej into v
#         else put nodej into u
#     put nodei into u

# if u and v has no same node


def isBipartite(graph):
    color = {}

    def check_node_color(node, node_color):
        return color[node] == node_color

    def dfs(curr_node, curr_color):
        if curr_node not in color:
            # if node is not in color ,update dictionary color
            color[curr_node] = curr_color
        else:
            # if node is already in the colormap check if current color is correspond to colormap
            if check_node_color(curr_node, curr_color):
                return True
            else:
                return False
        # seach each edge of the current node
        for neighbour_nodes in graph[curr_node]:
            if not dfs(neighbour_nodes, not curr_color):
                return False
        return True
    for node in graph:
        if node not in color:
            if not dfs(node, True):
                return False
    return True


graph1 = {'A': ['B', 'C'],
          'B': ['C', 'D'],
          'C': ['D'],
          'D': ['C'],
          'E': ['F'],
          'F': ['C']}


graph = {
    'A': ['D', 'E', 'F'],
    'B': ['D', 'E', 'F'],
    'C': ['D', 'E', 'F'],
    'D': ['A', 'B', 'C'],
    'E': ['A', 'B', 'C'],
    'F': ['A', 'B', 'C']

}


print(isBipartite(graph))

print(isBipartite(graph1))
