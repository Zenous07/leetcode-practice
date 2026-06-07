# Invert Binary Tree

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to invert the binary tree by swapping the left and right child of every node in the tree.

The function should return the root of the inverted binary tree.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Level Order Traversal (BFS)

### **Main Idea**

Traverse the tree level by level using a queue.

For every node visited:

* Swap its left and right children.
* Add the updated children to the queue for further processing.

By performing this operation on every node, the entire tree becomes inverted.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the root is `None`, return it immediately.

2. Create a queue and add the root node:

   * The queue helps process nodes level by level.

3. Traverse the tree while the queue is not empty:

   * Remove the front node from the queue.
   * Swap its left and right child pointers.

4. Add child nodes to the queue:

   * If the left child exists, add it to the queue.
   * If the right child exists, add it to the queue.

5. Continue until all nodes have been processed.

6. Return the root of the modified tree.

---

### **Example Walkthrough**

Original Tree:

```text
        4
      /   \
     2     7
    / \   / \
   1   3 6   9
```

After inversion:

```text
        4
      /   \
     7     2
    / \   / \
   9   6 3   1
```

Step-by-step:

* Visit node 4 → swap children (2 ↔ 7)
* Visit node 7 → swap children (6 ↔ 9)
* Visit node 2 → swap children (1 ↔ 3)
* Continue until all nodes are processed

Final tree is completely inverted.

---

### **Complexity**

Time Complexity: O(n)

* Every node is visited exactly once.

Space Complexity: O(n)

* The queue can store up to an entire level of the tree in the worst case.

---

## 🏁 Conclusion

Using Breadth-First Search (BFS), we visit every node exactly once and swap its children.

The queue-based approach is intuitive, efficient, and works for any binary tree structure.

This method successfully inverts the entire binary tree while maintaining optimal time complexity.