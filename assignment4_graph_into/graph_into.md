## 3.4.
 Run the strongly connected components algorithm on the following directed graphs G. When doing DFS on GR: whenever there is a choice of vertices to explore, always pick the one that is alphabetically first.
![imge](/assignment4_graph_into/image/problem1.png)
In each case answer the following questions.
- **(a) In what order are the strongly connected components (SCCs) found?**
 **(i)** Step1: Dfs on GR and order it in descending postvisit order
![GR](/assignment4_graph_into/image/gri.png)

If we write the GR in adjaceny list form it would be like, and the previst and post visit number would be like
```python
GR= {'A'=['B','E'],
'B'=[],
'C'=['A','J'],
'D'=['C'],
'E'=[],
'F'=['D','H'],
'G'=['B','H'],
'H'=['A','I'],
'I'=['E','G'],
'J'=['F']
}
previsit_number_GR={
'A'=1
'B'=2
'C'=7
'D'=10
'E'=4
'F'=9
'G'=14
'H'=12
'I'=13
'J'=8
}
postvisit_number_GR={
'A'=6
'B'=3
'C'=20
'D'=11
'E'=5
'F'=18
'G'=15
'H'=17
'I'=16
'J'=19
}
descending_order_of_post_visit=[C,J,F,H,I,G,D,A,E,B]
```

Step2. run dfs on $G$ the input of order of vertex would be ```[C,J,F,H,I,G,D,A,E,B]```
```python
previsit_number_G={
'A'=14
'B'=18
'C'=1
'D'=2
'E'=16
'F'=3
'G'=10
'H'=9
'I'=11
'J'=4
}
postvisit_number_G={
'A'=15
'B'=19
'C'=8
'D'=7
'E'=17
'F'=6
'G'=13
'H'=14
'I'=12
'J'=5
}
```
The order of how we find strongly connected components (SCCs) would be {$C,D,F,J$},{$H,G,I$},{$A$},{$E$},{$B$}





> **(ii)**
> Step1 Dfs on GR and order it in descending postvisit order

![GR](/assignment4_graph_into/image/GRII.png)
If we write the GR in adjaceny list form it would be like, and the previsit and postvisit number is
``` python
GR= {
'A'=['E'],
'B'=['A'],
'C'=['B'],
'D'=['A','G'],
'E'=['B'],
'F'=['C','H'],
'G'=['H'],
'H'=['D','E','I'],
'I'=['F','H'],

}
previsit_number_GR={
'A'=1
'B'=3
'C'=6
'D'=8
'E'=2
'F'=12
'G'=9
'H'=10
'I'=11
}
postvisit_number_GR={
'A'=6
'B'=4
'C'=7
'D'=17
'E'=5
'F'=13
'G'=16
'H'=15
'I'=14
}
descending_order_of_post_visit=[D,G,H,I,F,C,A,E,B]
```
Step2: run dfs on $G$ the input of order of vertex would be ```[D,G,H,I,F,C,A,E,B]```
```python
previsit_number_G={
'A'=13
'B'=14
'C'=11
'D'=1
'E'=15
'F'=3
'G'=7
'H'=2
'I'=4
}
postvisit_number_G={
'A'=18
'B'=17
'C'=12
'D'=10
'E'=16
'F'=6
'G'=8
'H'=9
'I'=5
}
```
The order of how we find strongly connected components (SCCs) would be {$D,H,F,I,G$},{$C$},{$A,B,E$}
- (b) Which are source SCCs and which are sink SCCs?
    **(i)**

    > source SCCs:{$E$},{$B$}
    > sink SCCs: {$C,D,F,J$}

    **(ii)**

    >source SCCs:{$A,B,E$}
    >sink SCCs:{$D,H,F,I,G$}
- (c) Draw the “metagraph” (each meta-node is an SCC of G).
**(i)**
![metagraphi](/assignment4_graph_into/image/metagraph(I).png)
**(ii)**
![metagraphii](/assignment4_graph_into/image/metagraph(ii).png)


##3.5. 
The reverse of a directed graph G = (V,E) is another directed graph GR = (V,ER) on the same vertex set, but with all edges reversed; that is, ER = {(v, u) : (u, v) ∈ E}.
### test graph:
```python
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
```
My solution: this solution define a new dictionary which is graphr to store the new order. I use adjacency list here
First, create graphr with keys but empty adjacency list.
```graphr = {key: [] for key in graph}```
Second for each node in the graph, scan it's adjacency list and append the node into the adjacency list of the node it's edge leads to in graphr. Time complexity is log(m+n) here.

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
![output](/assignment4_graph_into/image/reverse_graph.png)


## 3.7.
  A bipartite graph is a graph G=(V,E) whose vertices can be partitioned into two sets(V = V1 ∪ V2 and V1 ∩ V2 = ∅) such that there are no edges between vertices in the same set (for instance, if u, v ∈ V1, then there is no edge between u and v).
- (a) Give a linear-time algorithm to determine whether an undirected graph is bipartite.
> Here's my solution. I use a color dictionary to store color for each node.
> - At first the value for each node is Null.
> - Then we do the dfs on the graph. If the node is in color dictionary. 
> - check if the input node_color is correspond to the node's value in the dictionary. If yes return True, else return False. 
> - Then do dfs on the nodes that current node's edges lead to, the input corrent color is the opposite of the currentcolor. 
> The time complexity is O(n+m)
```python
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
```
***test case***
```python
graph1 = {'A': ['B', 'C'],
          'B': ['C', 'D'],
          'C': ['D'],
          'D': ['C'],
          'E': ['F'],
          'F': ['C']}
```
![output](/assignment4_graph_into/image/NON_BIPARTITLE.NPG.png)
```python
graph = {
    'A': ['D', 'E', 'F'],
    'B': ['D', 'E', 'F'],
    'C': ['D', 'E', 'F'],
    'D': ['A', 'B', 'C'],
    'E': ['A', 'B', 'C'],
    'F': ['A', 'B', 'C']

}
```
![output](/assignment4_graph_into/image/bipartitle.png)
![output](/assignment4_graph_into/image/bipartitleoutput.png)
- (b) There are many other ways to formulate this property. For instance, an undirected graph is bipartite if and only if it can be colored with just two colors.
Prove the following formulation: an undirected graph is bipartite if and only if it contains no cycles of odd length.
> First, let's make one thing clear. In a bipartitle graph, every odd edge brings the cycle to set $Y$,every even edge bring cycle back to set $X$
> ![output](/assignment4_graph_into/image/erfentuB.png)
>  - let's prove by contradiction. Let $C:(V1,V2,...Vn)$ and $n$ is a odd number.there is an odd cycle in our graph which we will call C and let's just say this cycle starts with the vertex v1 then goes to v2 ,all the way to some last vertex VN before returning to v1 since we assumed that this is an odd cycle we know the N  has to be odd.
> - $V1$ brings cycle to $Y$, $V2$ brings cycle back to $X$,$V3$ brings cycle to $Y$,$V4$ brings cycle back to $X$
> - Let $ Vi \in X$ if $i$ is odd,let $ Vi \in Y$ if $i$ is even
> - we know that n is odd, and $Vn \in X$. 
> - Then $Vn, V1 \in X $ ,but because Vn bring back to V1 which means they are adjacent. In a bipartitle graph, two adjacency vertex  cannot be in one set. Then the Graph C is not a bipartitle
- (c) At most how many colors are needed to color in an undirected graph with exactly one odd- length cycle?
 **Answer**: 3
## 3.13. Undirected vs. directed connectivity. ###
- (a) Prove that in any connected undirected graph G = (V,E) there is a vertex v ∈ V whose removal leaves G connected. (Hint: Consider the DFS search tree for G.)
> ***First, let's talk about what is the definition for connected undirected graph***
> An undirected graph is connected if there is a path between any pair of vertices. 
> Then look at the dfs_graph code. The recursion function is explore. if we carefully look at the explore() function, the base case for it is that we reach a node $Vn$ that all node its edge connects has been visited. We can remove this edge, and G is still connected, because there are edge from other nodes that leads to the nodes that $Vn$'s edge leads.
```python
def dfs(graph):
    global clockb
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

- (b) Give an example of a strongly connected directed graph G = (V,E) such that, for every v ∈ V , removing v from G leaves a directed graph that is not strongly connected.
> For every two nodes in a strongly connected directed graph, we say node v1,v2 $\in$ V , there is a path from v1 to v2, and a path from v2 to v1. The following graph is an example of a strongly connected directed graph. It is actually a cycle if we remove any one of the node, it became a line. It's not strong connected
> 
```python
graph1 = {'A': ['B'],
          'B': ['C'],
          'C': ['D'],
          'D': ['F'],
          'F': ['A']}
```
![directed](/assignment4_graph_into/image/directed_graph_example2.png)
- (c) In an undirected graph with 2 connected components it is always possible to make the graph connected by adding only one edge. Give an example of a directed graph with two strongly connected components such that no addition of one edge can make the graph strongly connected.

![directed](/assignment4_graph_into/image/directed_graph_example.png)
```python
graph1 = {'A': ['B'],
          'B': ['C'],
          'C': ['A'],
          'C': ['D'],
          'E': ['D'],
          'E': ['F'],
          'F': ['G'],
          'G': ['E'],
}
```
## 3.16. ##
Suppose a CS curriculum consists of n courses, all of them mandatory. The prerequisite graph G has a node for each course, and an edge from course v to course w if and only if v is a prerequisite for w. Find an algorithm that works directly with this graph representation, and computes the minimum number of semesters necessary to complete the curriculum (assume that a student can take any number of courses in one semester). The running time of your algorithm should be linear.

- Let's say this is a dag (directed acyclic graph) with n node, we have to complete the parent of a node the graph then we can move on，a dag at least has one source and one sink. The problem turns into finding the longest path from one source to a sink in the dag.
 Here's my example data
 ```python 
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
```
![image](/assignment4_graph_into/image/316.png)
 - First find source nodes in a dag, let len(node)=n,len(edge)=m, this function equals to m
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
 - build a function to caculate the longest path from  source node to a sink， I use bellford algorithem here. The time complicity is m here
```python
def find_longest_path_in_source_bellford(graph, source):
    dist = {}
    p = {}
    max = 0
    for v in graph:
        dist[v] = -10000  
        p[v] = None
    dist[source] = 0

    for u in graph:
        for v in graph[u]:
            if dist[v] < dist[u]+1:
                dist[v] = dist[u]+1
            p[v] = u  
    all_values = list(dist. values())
    sorted(all_values)

    return all_values[-1]
```
 - make a dictionary```python {sourse1:longest_path, source2:longest_path}``` , Then pick the max value of the dictionary. And plus 1 to the max number you will get the semester number
```python
def solution(graph):
    longest_path_for_each_source = {} # this dictionary stores longest path from each node to sink
    source = find_source(graph)  # m 
    for i in source:  # len(source)*m
        longest_path_for_each_source[i] = find_longest_path_in_source_bellford(
            graph, i)
    longest = list(longest_path_for_each_source.values())
    sorted(longest)

    return longest[-1]+1
```
![output](/assignment4_graph_into/image/316output.png)