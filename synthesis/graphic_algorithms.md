5 **Graph Algorithms**
5.1 **Dijkstra’s Algorithm**
![output](/synthesis/image_for_symthesis/ga1.png)
- > Step1 : we make prev,dist and heap make the distance for the node where we start to 0
  > ```prev={{'A': None, 'B': None, 'C': None, 'D': None, 'E': None}}```
  > ```dist={'A': 0, 'B': 100000, 'C': 100000, 'D': 100000, 'E': 100000}```
  > ```heap={'A': 0, 'B': 100000, 'C': 100000, 'D': 100000, 'E': 100000}```
- > Step2 we pop the item who has smallest value from heap,make it u. u=```A:0```
  A's edges are ```'A': {'B': 4, 'C': 2},```
    Now we have
  > ```prev={{'A': None, 'B': A, 'C': A, 'D': None, 'E': None}}```
  > ```dist={'A': 0, 'B': 4, 'C': 2, 'D': 100000, 'E': 100000}```
    update the distance for heap
  > ```heap={'B': 4, 'C': 2, 'D': 100000, 'E': 100000}```
- > Step3 we pop the item who has smallest value from heap,make it u. u=```C:2``` 
  C's edges are ```'C': {'B': 1, 'D': 4, 'E': 5}```
    Now we have
  > ```prev={{'A': None, 'B': C, 'C': A, 'D': C, 'E': C}}```
  > ```dist={'A': 0, 'B': 3, 'C': 2, 'D': 6, 'E': 7}```
    update the distance for heap
  > ```heap={'B': 3, 'D': 6, 'E': 7}```

- > Step4 We pop the item who has smallest value from heap,make it u. u=```'B':3```
  C's edges are ``` 'B': {'C': 3, 'D': 2, 'E': 3}```
    Now we have
  > ```prev={{'A': None, 'B': C, 'C': A, 'D': B, 'E': B}}```
  > ```dist={'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}```
    update the distance for heap
  > ```heap={'D': 5, 'E': 6}```

- > Step5. We pop the item who has smallest value from heap,make it u. u=```'D': 5```
  C's edges are ``` 'D': {}```
    Because D leads to no vertices so nothing changes,Now we have
  > ```prev={{'A': None, 'B': C, 'C': A, 'D': B, 'E': B}}```
  > ```dist={'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}```
    update the distance for heap
  > ```heap={'E': 6}```

- > Step6.  Pop the item who has smallest value from heap,make it u. u=```'E': 6```
  C's edges are ``` 'E': {'D': 1}```
  > ```prev={{'A': None, 'B': C, 'C': A, 'D': B, 'E': B}}```
  > ```dist={'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}```
  > ```heap={}```
- > step 7. Now heap is empty
  > return dist={'A': 0, 'B': 3, 'C': 2, 'D': 5, 'E': 6}


- Input : (Graph,source)
Graph is a  dictionary and source is a vertex. The data type of graph is dictionary, and the data type of source is string. actually source is a vertex here. You can use 'A','B' or any letter in the ```Graph```
```python
Graph = {
    'A': {'B': 4, 'C': 2}, 
    'B': {'C': 3, 'D': 2, 'E': 3}, 
    'C': {'B': 1, 'D': 4, 'E': 5}, 
    'D': {}, 
    'E': {'D': 1}
}
```
- I have three containers in the function. They are ```dist{}```, ```previous {}```, ```heap_dist{}``` On the dasgupty, dist and prev are lists. But I use dictionary in my function. Because I use letter to denote the vertex. 
- - dist{} shows the distance to each node from  source   
- - heap_dist{} contains key:value pair of unvisited vertices:dist I handle it as a heap, 
- - previous {} holds one crucial piece of information for each node :the identity of the node immediately before it on the shortest path from s to u. By following these back-pointers, we can easily reconstruct shortest paths, and so this array is a compact summary of all the paths found

**exercise:**
Develop the Dijkstra’s Algorithm with python.
``` 
Input: Graph G = (V, E), directed or undirected;
positive edge lengths {le : e ∈ E}; vertex s ∈ V
Output: For all vertices u reachable from s, dist(u) is set to the distance from s to u.
for all u ∈ V : 
    dist(u) = ∞
    prev(u) = nil 
dist(s) = 0
H = makequeue (V ) (using dist-values as keys) 
while H is not empty:
    u = deletemin(H)
    for all edges (u, v) ∈ E:
    if dist(v) > dist(u) + l(u, v): 
        dist(v) = dist(u) + l(u, v) 
        prev(v) = u 
    decreasekey(H, v)
```
**solution:**
```python
def dijkstra_adjacency_list(Graph, source):
    def deap_pop_min(heap):  # remember the input should be an dictionary
        min_key = None
        min_num = 1000000
        for i, j in heap.items():
            if j < min_num:
                min_num = j
                min_key = i
        heap.pop(min_key)
        return min_key


    previous = {i: None for i in Graph}

    dist = {i: 100000 for i in Graph}
    dist[source] = 0
    heap_dist = {}
    heap_dist = {i: j for i, j in dist.items()}
    while len(heap_dist) != 0:
        u = deap_pop_min(heap_dist)

        for v in Graph[u]:

            edge_length = Graph[u][v]
            if dist[v] > dist[u] + edge_length:
                dist[v] = dist[u] + edge_length
                previous[v] = u
            # decreasekey(H, v),其实就是update heap_dist
                heap_dist[v] = dist[u] + edge_length
        # print(dist)
    print(previous)
    return dist


print(dijkstra_adjacency_list(Graph, 'A'))
```
5.2 **Bellman-Ford Algorithm**

**exercise:**
<your write up goes here>
**solution:**
<your write up goes here>
5.3 **Matchings**
<your write up goes here>
**exercise:**
<your write up goes here>
**solution:**
<your write up goes here>
5.3 **Domination**
<your write up goes here>
**exercise:**
<your write up goes here>
**solution:**
<your write up goes here>