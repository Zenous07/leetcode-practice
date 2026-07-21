# Binary Tree Level Order Traversal

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to return the level order traversal of its nodes' values (also known as Breadth-First Traversal).

The traversal should visit nodes level by level, from left to right, and return the values as a list of lists.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Level Order Traversal (BFS)

### **Main Idea**

Use a queue to process the tree one level at a time.

At each level:

* Determine how many nodes belong to the current level.
* Visit each of those nodes from left to right.
* Store their values in a temporary list.
* Add their left and right children to the queue for the next level.
* After finishing the current level, add the temporary list to the final result.

Repeat this process until there are no more nodes left to process.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the tree is empty (`root` is `None`), return an empty list.

2. Create an empty result list.

   * This will store the traversal level by level.

3. Create a queue and insert the root node.

   * The queue ensures nodes are processed in the correct order.

4. Process the tree while the queue is not empty.

   * Count how many nodes belong to the current level.
   * Create a temporary list for storing the current level's values.

5. Visit every node in the current level.

   * Remove a node from the front of the queue.
   * Store its value.
   * If it has a left child, add it to the queue.
   * If it has a right child, add it to the queue.

6. After processing all nodes of the current level,

   * Add the temporary list to the final result.

7. Continue until the queue becomes empty.

8. Return the completed level order traversal.

---

### **Example Walkthrough 1**

Binary Tree:

```text
        3
       / \
      9   20
         /  \
        15   7
```

Traversal:

* Level 1 → [3]
* Level 2 → [9, 20]
* Level 3 → [15, 7]

Final Output:

```text
[[3], [9,20], [15,7]]
```

---

### **Example Walkthrough 2**

Binary Tree:

```text
      1
```

Traversal:

* Level 1 → [1]

Final Output:

```text
[[1]]
```

---

### **Example Walkthrough 3**

Binary Tree:

```text
Empty Tree
```

Traversal:

There are no nodes to visit.

Final Output:

```text
[]
```

---

### **Example Walkthrough 4**

Binary Tree:

```text
          10
         /  \
        5    15
       / \     \
      2   7     20
```

Traversal:

* Level 1 → [10]
* Level 2 → [5, 15]
* Level 3 → [2, 7, 20]

Final Output:

```text
[[10], [5,15], [2,7,20]]
```

---

### **Why BFS Works Best**

Breadth-First Search naturally processes nodes one level at a time.

Since the problem specifically asks for level order traversal, BFS is the most direct and efficient approach.

A queue preserves the order in which nodes should be visited, ensuring every level is processed correctly before moving to the next one.

---

### **Complexity**

**Time Complexity:** O(n)

* Every node is visited exactly once.

**Space Complexity:** O(n)

* In the worst case, the queue may store an entire level of the tree.

---

## 🏁 Conclusion

Using Breadth-First Search (BFS), we process the binary tree level by level while maintaining the correct left-to-right order.

The queue-based approach is simple, intuitive, and guarantees that every node is visited exactly once, making it the optimal solution for level order traversal.
