# Following is complete algorithm for finding longest distances.
# 1) Initialize dist[] = {NINF, NINF, ….} and dist[s] = 0 where s is the source vertex. Here NINF means negative infinite.
# 2) Create a topological order of all vertices.
# 3) Do following for every vertex u in topological order.
# ………..Do following for every adjacent vertex v of u
# ………………if (dist[v] < dist[u] + weight(u, v))
# ………………………dist[v] = dist[u] + weight(u, v)

# A recursive function used by longestPath. See below
# link for details
# https:#www.geeksforgeeks.org/topological-sorting/
def topologicalSortUtil(v):
    global Stack, visited, adj
    visited[v] = True

    # Recur for all the vertices adjacent to this vertex
    # list<AdjListNode>::iterator i
    for i in adj[v]:
        if (not visited[i[0]]):
            topologicalSortUtil(i[0])

    # Push current vertex to stack which stores topological
    # sort
    Stack.append(v)

# The function to find longest distances from a given vertex.
# It uses recursive topologicalSortUtil() to get topological
# sorting.


def longestPath(s):
    global Stack, visited, adj, V
    dist = [-10**9 for i in range(V)]

    # Call the recursive helper function to store Topological
    # Sort starting from all vertices one by one
    for i in range(V):
        if (visited[i] == False):
            topologicalSortUtil(i)
    # print(Stack)

    # Initialize distances to all vertices as infinite and
    # distance to source as 0
    dist[s] = 0
    # Stack.append(1)

    # Process vertices in topological order
    while (len(Stack) > 0):

        # Get the next vertex from topological order
        u = Stack[-1]
        del Stack[-1]
        # print(u)

        # Update distances of all adjacent vertices
        # list<AdjListNode>::iterator i
        if (dist[u] != 10**9):
            for i in adj[u]:
                # print(u, i)
                if (dist[i[0]] < dist[u] + i[1]):
                    dist[i[0]] = dist[u] + i[1]

    # Print calculated longest distances
    # print(dist)
    for i in range(V):
        print("INF ", end="") if (dist[i] == -
                                  10**9) else print(dist[i], end=" ")


# Driver code
if __name__ == '__main__':
    V, Stack, visited = 6, [], [False for i in range(7)]
    adj = [[] for i in range(7)]

    # Create a graph given in the above diagram.
    # Here vertex numbers are 0, 1, 2, 3, 4, 5 with
    # following mappings:
    # 0=r, 1=s, 2=t, 3=x, 4=y, 5=z
    adj[0].append([1, 5])
    adj[0].append([2, 3])
    adj[1].append([3, 6])
    adj[1].append([2, 2])
    adj[2].append([4, 4])
    adj[2].append([5, 2])
    adj[2].append([3, 7])
    adj[3].append([5, 1])
    adj[3].append([4, -1])
    adj[4].append([5, -2])

    s = 1
    print("Following are longest distances from source vertex ", s)
    longestPath(s)

    # This code is contributed by mohit kumar 29.
