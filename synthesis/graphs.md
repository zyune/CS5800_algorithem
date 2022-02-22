#4 **Graphs**
## 4.1 **basic definition**
####4.1.1 what is dag？
Directed acyclic graphs, or dags for short, come up all the time. They are good for modeling relations like causalities, hierarchies, and temporal dependencies。
-  In a dag, every edge leads to a vertex with a lower post number.
- Every dag has at least one source and at least one sink.
- Every directed graph is a dag of its strongly connected components.
- So every metagraph is a dag. Because each node is a strongly connected components
####4.1.2 what is directed and undirected graph
undirected graph

directed graph
####4.1.3 what is sink what is source 
- **sink**
> First, I want to make it clear that sink and source only exists in directed graph.
***A sink is a node of a directed graph with no exiting edges.***
<p align=center>
    <img align=center src="/synthesis/image_for_symthesis/graph1.svg" align=right >

</p>

- **source** 
>A source is a node of a directed graph that don't have parent node.  In the picture below $B$ is source node.
<p align=center>
    <img align=center src="/synthesis/image_for_symthesis/graph2.png" align=right >

</p>

>This is  my function to find a source in an unweighted directed graph. It works!
```python
def find_source(graph):
    source = set()
    not_source = set()
    # 这个方法其实是m次
    for node in Graph:
        for edge in Graph[node]:
            not_source.add(edge)
    for node in Graph:
        if node not in not_source:
            source.add(node)
    return source
```
  
####what is metagraph
- metagraph is a graph to describe the strong connection relationship in a directed graph. 
- Nodes in a metagraph can contain more than one node.
- Every node in a metagraph is a strongly connected components.
- metagraph is a dag

<p align=center>
    <img align=center src="/synthesis/image_for_symthesis/graph3.png" align=right >

</p>



### **exercise:**

### **solution:**

## 4.2 graph representations
There are two way to build a graph
####4.2.1 adjacency list
<p align=center>
    <img align=center src="/synthesis/image_for_symthesis/graph5.png" align=right >

</p>
 an unweighted directed graph with python
```python
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
```
 an weighted directed graph with python
```python
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  2, 'd':  3, 'e':  2},
        'c': {},
        'd': {'b':  3, 'c':  5},
        'e': {'d': -3}
    }
```
####4.2.2. adjacency matrix
In python an adjacency matrix is implemented like a 2-dimensional matrix ```[[0,1,1,1][1,0,1,0][1,1,0,0][1,0,0,0]]```

<p align=center>
    <img align=center src="/synthesis/image_for_symthesis/graph4.png" align=right >

</p>

```python

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size
```
### **exercise:**

### **solution:**

## 4.3 **graph traversal algorithms**
####4.3.1 depth first search
```python
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
```
####4.3.2 breath first search
```python
    def BFS(self, s):
 
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)
 
        # Create a queue for BFS
        queue = []
 
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
 
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
```

### **exercise:**

### **solution:**

## 4.4 connectivity and strongly connected regions
####4.4.1 connectivity in undirected graph


- A graph that is not connected can be decomposed in a natural and obvious manner into several connected components
- In directed graph Two nodes u and v of a directed graph are connected if there is a path from u to v and a path from v to u.
- An undirected graph is connected if there is a path between any pair of vertices.


####4.4.2 an algorithem to check connectivity on a directed graph
1. Run depth-first search on GR.
2. Run the undirected connected components algorithm (from Section 3.2.3) on G, and dur- ing the depth-first search, process the vertices in decreasing order of their post numbers from step 1.

```python
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
```

### **exercise:**

### **solution:**
