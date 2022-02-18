def bellman_ford(graph, source):
    dist = {}
    p = {}
    max = 10000
    for v in graph:
        dist[v] = max  # 赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0

    for i in range(len(graph) - 1):
        for u in graph:
            for v in graph[u]:
                if dist[v] > graph[u][v] + dist[u]:
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u  # 完成松弛操作，p为前驱节点

    for u in graph:
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                return None, None  # 判断是否存在环路

    return dist, p


def test():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  2, 'd':  3, 'e':  2},
        'c': {},
        'd': {'b':  3, 'c':  5},
        'e': {'d': -3}
    }
    dist, p = bellman_ford(graph, 'a')
    print(dist)
    print(p)


def testfail():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  2, 'd':  3, 'e':  2},
        'c': {'d': -5},
        'd': {'b':  3},
        'e': {'d': -3}
    }
    dist, p = bellman_ford(graph, 'a')
    print(dist)
    print(p)


test()
testfail()
