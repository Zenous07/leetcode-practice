# Find if Path Exists in Graph

## 🧩 Problem Overview

You are given a bi-directional graph with n vertices labeled from 0 to n - 1.

Your task is to determine if there is a valid path from a source vertex to a destination vertex using the given edges.

The function should return true if a path exists between the two vertices, or false otherwise.

---

## 💡 Solution: Depth-First Search (DFS)

### **Method Used**

Stack-Based Depth-First Search (DFS) with Adjacency List Representation

### **Main Idea**

Build an adjacency list to represent the graph connections between vertices.

Traverse the graph using a stack-based DFS starting from the source vertex.

For every vertex visited:

* Mark it as visited to avoid revisiting.
* Explore all its unvisited neighbors.
* Push each unvisited neighbor onto the stack for further exploration.

If the destination vertex is encountered during traversal, return true immediately.

If the stack becomes empty without finding the destination, return false.

---

### **Detailed Explanation**

1. Handle edge cases:

   * If there are no edges and source equals destination, return true.
   * If source and destination are the same vertex, return true immediately.

2. Build an adjacency list from the edges:

   * Create a dictionary mapping each vertex to its list of neighbors.
   * For each bidirectional edge [u, v], add v to u's neighbors and u to v's neighbors.

3. Initialize the DFS traversal:

   * Create a set to track visited vertices.
   * Add the source vertex to the visited set.
   * Create a stack and push the source vertex onto it.

4. Traverse the graph while the stack is not empty:

   * Pop a vertex from the stack.
   * Iterate through all neighbors of the current vertex.
   * For each unvisited neighbor:
   * Mark it as visited.
   * Push it onto the stack.
   * If the neighbor is the destination vertex, return true immediately.

5. After stack is empty:

   * If destination was never found, return false.

---

### **Example Walkthrough 1**

Graph with Connected Path:

n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2

Original Graph:

```text
    0 ←→ 1
    ↓   ↙
    2 ←→
```

Or as connections:
* 0 connected to: 1, 2
* 1 connected to: 0, 2
* 2 connected to: 1, 0

Adjacency List Structure:
0 → [1, 2]
1 → [0, 2]
2 → [1, 0]

Step-by-step DFS Traversal:

* Initialize: visited = {0}, stack = [0]
* Step 1: Pop 0, explore neighbors [1, 2]
  - Neighbor 1 not visited → mark visited, push 1
  - Neighbor 2 not visited → mark visited, push 2, destination found? YES → return true

Result: true
Valid paths exist: 0 → 2 or 0 → 1 → 2

---

### **Example Walkthrough 2**

Graph with Disconnected Components:

n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5

Original Graph:

```text
Component 1:     Component 2:
    1               3
    |              / \
    0             5   4
    |              \ /
    2

(No connection between components)
```

Adjacency List Structure:
0 → [1, 2]
1 → [0]
2 → [0]
3 → [5, 4]
4 → [5, 3]
5 → [3, 4]

Step-by-step DFS Traversal:

* Initialize: visited = {0}, stack = [0]
* Step 1: Pop 0, explore neighbors [1, 2]
  - Neighbor 1 not visited → mark visited, push 1
  - Neighbor 2 not visited → mark visited, push 2
* Step 2: Pop 2, explore neighbors [0]
  - Neighbor 0 already visited → skip
* Step 3: Pop 1, explore neighbors [0]
  - Neighbor 0 already visited → skip
* Stack is empty, destination 5 never reached

Result: false
Vertices 0-2 form one component, vertices 3-5 form another disconnected component.

---

### **Example Walkthrough 3**

Linear Chain Graph:

n = 4, edges = [[0,1],[1,2],[2,3]], source = 0, destination = 3

Original Graph:

```text
0 ←→ 1 ←→ 2 ←→ 3
```

Linear connection:
0 is connected only to 1
1 is connected to 0 and 2
2 is connected to 1 and 3
3 is connected only to 2

Adjacency List Structure:
0 → [1]
1 → [0, 2]
2 → [1, 3]
3 → [2]

Step-by-step DFS Traversal:

* Initialize: visited = {0}, stack = [0]
* Step 1: Pop 0, explore neighbors [1]
  - Neighbor 1 not visited → mark visited, push 1
* Step 2: Pop 1, explore neighbors [0, 2]
  - Neighbor 0 already visited → skip
  - Neighbor 2 not visited → mark visited, push 2
* Step 3: Pop 2, explore neighbors [1, 3]
  - Neighbor 1 already visited → skip
  - Neighbor 3 not visited → mark visited, push 3, destination found? YES → return true

Result: true
Valid path: 0 → 1 → 2 → 3

---

### **Example Walkthrough 4**

Single Vertex Graph:

n = 1, edges = [], source = 0, destination = 0

No edges to process.

Step-by-step:

* Initialize: Check if source == destination → YES → return true immediately

Result: true
No traversal needed, source and destination are the same vertex.

---

### **Example Walkthrough 5**

Dense Graph with Multiple Paths:

n = 5, edges = [[0,1],[0,2],[1,2],[1,3],[2,3],[3,4]], source = 0, destination = 4

Original Graph:

```text
    0
   / \
  1——2
   \ /
    3
    |
    4
```

Connections:
0 is connected to: 1, 2
1 is connected to: 0, 2, 3
2 is connected to: 0, 1, 3
3 is connected to: 1, 2, 4
4 is connected to: 3

Adjacency List Structure:
0 → [1, 2]
1 → [0, 2, 3]
2 → [0, 1, 3]
3 → [1, 2, 4]
4 → [3]

Step-by-step DFS Traversal:

* Initialize: visited = {0}, stack = [0]
* Step 1: Pop 0, explore neighbors [1, 2]
  - Neighbor 1 not visited → mark visited, push 1
  - Neighbor 2 not visited → mark visited, push 2
* Step 2: Pop 2, explore neighbors [0, 1, 3]
  - Neighbor 0 already visited → skip
  - Neighbor 1 already visited → skip
  - Neighbor 3 not visited → mark visited, push 3
* Step 3: Pop 3, explore neighbors [1, 2, 4]
  - Neighbor 1 already visited → skip
  - Neighbor 2 already visited → skip
  - Neighbor 4 not visited → mark visited, push 4, destination found? YES → return true

Result: true
Multiple valid paths: 0 → 1 → 3 → 4 or 0 → 2 → 3 → 4

---

### **Complexity**

Time Complexity: O(n + e)

* n is the number of vertices in the graph.
* e is the number of edges in the graph.
* Building the adjacency list takes O(e) time.
* DFS visits each vertex at most once and explores each edge at most twice (bidirectional).
* Early termination when destination is found reduces practical runtime.

Space Complexity: O(n + e)

* The adjacency list requires O(n + e) space to store all vertices and their connections.
* The visited set requires O(n) space to track explored vertices.
* The stack requires O(n) space in the worst case (linear chain or worst-case DFS depth).

---

## 🏁 Conclusion

Using Depth-First Search with an adjacency list representation, we efficiently explore the graph to determine if a path exists from source to destination.

The DFS approach is intuitive, works for any graph structure, and finds paths optimally.

Early termination upon discovering the destination makes this solution practical for large graphs.

This method successfully solves the path existence problem while maintaining linear time complexity relative to graph size.