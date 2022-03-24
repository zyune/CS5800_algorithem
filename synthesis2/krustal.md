#Kruskal's algorithm
Steps:
    1. Sort all the edges in non-decreasing order of their weight. 
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. 
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.

Greedy algorithem implementation of Kruskal's algorithm
- Candidates - edges
- Selection - a subset S⊆ E of the candidate edges
- Solution check - does S touch every vertex, is it connected?
- Feasibility check - does adding e ∈ E create a cycle?
- Select function - edge weight
- Objective function - sum of weights

How to detect cycles?
- We use union find(Disjoint Set) algorithem.
Use 
**Following word is I sited from geeks for geeks. I think it is very useful.**
Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate through all edges and apply the find-union algorithm. The find and union operations can take at most O(LogV) time. So overall complexity is O(ELogE + ELogV) time. The value of E can be at most O(V2), so O(LogV) is O(LogE) the same. Therefore, the overall time complexity is O(ElogE) or O(ElogV)