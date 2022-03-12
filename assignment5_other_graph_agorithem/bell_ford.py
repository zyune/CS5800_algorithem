def bellman_ford(graph, source):
    dist = {}
    p = {}
    max = 10000
    for v in graph:
        dist[v] = max  # 赋值为负无穷完成初始化
        p[v] = None
    dist[source] = 0
    num = 1
    for i in range(len(graph) - 1):
        print('current i is ', i)
        print('  ', )
        for u in graph:

            for v in graph[u]:
                print('step', num, '--------------')
                num += 1
                print('u is ', u, 'and v is ', v)
                print('dist[v]=', dist[v])
                print('graph[u][v] + dist[u]=', graph[u][v] + dist[u])
                if dist[v] > graph[u][v] + dist[u]:
                    print('Apparently,dist[v] > graph[u][v] + dist[u]')
                    dist[v] = graph[u][v] + dist[u]
                    p[v] = u  # 完成松弛操作，p为前驱节点

            print('dist is ', dist)
            print('Previous is ', p)
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
    Graph2 = {
        'A': {'B': 4, 'C': 2}, 'B': {'C': 3, 'D': 2, 'E': 3}, 'C': {'B': 1, 'D': 4, 'E': 5}, 'D': {}, 'E': {'D': 1}
    }
    graph3 = {
        'A': {'B': 3},
        'B': {'C': 4, 'H': -3},
        'C': {'D': 2},
        'D': {'E': -5, 'F': 2},
        'E': {'B': 2},
        'F': {'G': 1},
        'G': {'H': 8},
        'H': {'D': 7}
    }
    dist, p = bellman_ford(graph3, 'A')


def testfail():
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  2, 'd':  3, 'e':  2},
        'c': {'d': -5},
        'd': {'b':  3},
        'e': {'d': -3}
    }
    dist, p = bellman_ford(graph, 'a')
    # print(dist)
    # print(p)


test()
# testfail()
