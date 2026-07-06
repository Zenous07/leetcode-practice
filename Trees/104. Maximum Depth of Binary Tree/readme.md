# Maximum Depth of Binary Tree

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to find and return the maximum depth of the tree.

The maximum depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

---

## 💡 Solution: Recursive Depth-First Search (DFS)

### **Method Used**

Recursion (Depth-First Search)

### **Main Idea**

The depth of a tree can be determined by finding the depth of its left subtree and right subtree.

For every node:

* Recursively calculate the depth of the left subtree.
* Recursively calculate the depth of the right subtree.
* The depth of the current node is 1 plus the larger of the two depths.

If a node is `null`, its depth is `0`.

---

### **Detailed Explanation**

1. Check if the current node is empty:

   * If the node is `null`, return `0`.
   * This acts as the base case for recursion.

2. Recursively calculate the depth of the left subtree:

   * Find the maximum depth starting from the left child.

3. Recursively calculate the depth of the right subtree:

   * Find the maximum depth starting from the right child.

4. Add `1` to both depths:

   * The extra `1` represents the current node itself.

5. Return the larger depth:

   * The longest path determines the maximum depth of the tree.

---

### **Example Walkthrough**

Input:
``` text
    3
   / \
  9  20
     / \
    15  7
```
Step-by-step:

* Node 9 has depth 1.
* Nodes 15 and 7 each have depth 1.
* Node 20 has depth 2.
* Root node 3 has depth 3.

Output: 3

---

### **Why This Works**

Each node contributes one level to the depth.

By recursively exploring both subtrees and choosing the deeper one, the algorithm guarantees that the longest root-to-leaf path is found.

---

### **Complexity**

Time Complexity: O(n)

* Every node is visited exactly once.

Space Complexity: O(h)

* Recursive call stack stores at most the height of the tree.
* `h` is the height of the tree.
* In the worst case (skewed tree), space complexity becomes O(n).

---

## 🏁 Conclusion

This recursive DFS approach is one of the most common and intuitive ways to solve the Maximum Depth of Binary Tree problem.

By computing the depth of the left and right subtrees and taking their maximum, we can efficiently determine the longest path from the root to any leaf node.