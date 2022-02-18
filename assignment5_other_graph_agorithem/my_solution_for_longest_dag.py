# > - First find source nodes in a dag
# > - make a dictionary```python {sourse1: longest_path, source2: longest_path}```, caculate the longest path from each source node to a sink
# > - compute

Graph = {
    'a': ['b'],
    'b': ['d'],
    'c': ['d'],
    'd': ['e'],
    'e': ['f', 'g'],
    'f': [],
    'g': ['h'],
    'h': []

}


def find_source(graph):
    source = set()
    not_source = set()
    for node in Graph:
        for edge in Graph[node]:
            not_source.add(edge)
    for node in Graph:
        if node not in not_source:
            source.add(node)
    return source


print(find_source(Graph))


def find_longest_path_in_source_bellford(graph, source):
    dist = {}
    p = {}
    max = 0
    for v in graph:
        dist[v] = -10000  # 赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0

    for u in graph:
        for v in graph[u]:
            if dist[v] < dist[u]+1:
                dist[v] = dist[u]+1
            p[v] = u  # 完成松弛操作，p为前驱节点
    all_values = list(dist. values())
    sorted(all_values)

    return all_values[-1]


def solution(graph):
    longest_path_for_each_source = {}
    source = find_source(graph)
    for i in source:
        longest_path_for_each_source[i] = find_longest_path_in_source_bellford(
            graph, i)
    longest = list(longest_path_for_each_source.values())
    sorted(longest)

    return longest[-1]+1


print(solution(Graph))
