# Binary Tree Zigzag Level Order Traversal

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to return the zigzag level order traversal of the tree's nodes' values.

The zigzag pattern means traversing from left to right on odd levels (1st, 3rd, 5th...) and from right to left on even levels (2nd, 4th, 6th...).

The function should return a list of lists containing the node values in zigzag order.

---

## 💡 Solution: Breadth-First Search (BFS) with Queue

### **Method Used**

Queue-Based Level Order Traversal (BFS) with Alternating Direction

### **Main Idea**

Traverse the tree level by level using a queue.

For every level visited:

* Collect all node values at that level in a temporary list.
* If the level index is odd, add the list as-is to the result.
* If the level index is even, reverse the list before adding to the result.
* This creates the zigzag pattern without modifying the tree structure.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the root is `None`, return an empty list immediately.

2. Initialize a queue and result list:

   * Add the root node to the queue.
   * Initialize an index counter starting at 1.

3. Traverse the tree level by level while the queue is not empty:

   * Create a temporary list to store values at the current level.
   * Get the current queue length to process all nodes at this level.

4. For each node at the current level:

   * Remove the front node from the queue.
   * Add its value to the temporary list.
   * If the node has a left child, add it to the queue.
   * If the node has a right child, add it to the queue.

5. After processing all nodes at the current level:

   * If the level index is odd (1, 3, 5...), append the temporary list as-is.
   * If the level index is even (2, 4, 6...), reverse the temporary list and append.
   * Increment the level index.

6. Continue until all levels have been processed.

7. Return the result list.

---

### **Example Walkthrough 1**

Original Tree:

```
       3
      / \
     9  20
       /  \
      15   7
```

Step-by-step traversal:

Level 1 (index=1, odd): Process node 3 → [3]
Level 2 (index=2, even): Process nodes 9, 20 → [9, 20] → reverse to [20, 9]
Level 3 (index=3, odd): Process nodes 15, 7 → [15, 7]

Result: [[3], [20, 9], [15, 7]]

---

### **Example Walkthrough 2**

Original Tree:

```
         1
        / \
       2   3
      / \
     4   5
    /
   6
```

Step-by-step traversal:

Level 1 (index=1, odd): Process node 1 → [1]
Level 2 (index=2, even): Process nodes 2, 3 → [2, 3] → reverse to [3, 2]
Level 3 (index=3, odd): Process nodes 4, 5 → [4, 5]
Level 4 (index=4, even): Process node 6 → [6] → reverse to [6]

Result: [[1], [3, 2], [4, 5], [6]]

---

### **Example Walkthrough 3**

Single Node Tree:

```
  5
```

Step-by-step traversal:

Level 1 (index=1, odd): Process node 5 → [5]

Result: [[5]]

---

### **Complexity**

Time Complexity: O(n)

* Every node is visited exactly once during BFS traversal.
* Reversing lists at even levels takes O(n) in total across all levels.

Space Complexity: O(w)

* The queue can store up to the maximum width of the tree.
* In the worst case (complete binary tree), this is O(2^h) where h is the height.
* For a balanced tree, the space is O(n/2) = O(n).

---

## 🏁 Conclusion

Using Breadth-First Search (BFS) with an alternating direction strategy, we traverse every node exactly once and collect values in the zigzag pattern.

The queue-based approach is intuitive, efficient, and works for any binary tree structure.

This method successfully achieves zigzag level order traversal while maintaining optimal time complexity.