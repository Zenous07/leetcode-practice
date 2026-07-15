# Symmetric Tree

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to determine whether the tree is **symmetric**, meaning the left subtree is a mirror image of the right subtree.

A tree is symmetric if:

- The values of corresponding nodes are equal.
- The left child of one subtree matches the right child of the other subtree.
- The right child of one subtree matches the left child of the other subtree.

Return `True` if the tree is symmetric; otherwise, return `False`.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Mirror Traversal (BFS)

### **Main Idea**

Use two queues to simultaneously traverse the left and right sides of the tree in mirrored order.

At every step:

- Remove one node from each queue.
- Compare their values.
- Verify that their children exist in mirrored positions.
- Continue checking the next mirrored pair.

If every mirrored pair matches, the tree is symmetric.

---

### **Detailed Explanation**

1. Handle the edge case:

   - If the root is `None`, the tree is symmetric, so return `True`.

2. Create two queues:

   - Both queues initially contain the root node.
   - One queue explores the tree normally.
   - The other queue explores it in mirrored order.

3. Process both queues together:

   - Remove one node from each queue.
   - Compare their values.
   - If the values differ, the tree is not symmetric.

4. Check the left child of the first node against the right child of the second node.

   - If only one exists, return `False`.
   - If both exist, add them to their respective queues.

5. Check the right child of the first node against the left child of the second node.

   - If only one exists, return `False`.
   - If both exist, continue processing.

6. Repeat until both queues become empty.

7. If every comparison succeeds, return `True`.

---

### **Example Walkthrough 1**

Tree:

```text
        1
      /   \
     2     2
    / \   / \
   3   4 4   3
```

Processing:

- Compare 1 and 1 ✓
- Compare 2 and 2 ✓
- Compare 3 and 3 ✓
- Compare 4 and 4 ✓

All mirrored nodes match.

Output:

```text
True
```

---

### **Example Walkthrough 2**

Tree:

```text
        1
      /   \
     2     2
      \     \
       3     3
```

Processing:

- Compare 1 and 1 ✓
- Compare 2 and 2 ✓
- Left child of the first subtree is missing, but the mirrored right child exists.

Mirror structure is violated.

Output:

```text
False
```

---

### **Example Walkthrough 3**

Tree:

```text
      1
     / \
    2   2
```

Processing:

- Compare 1 and 1 ✓
- Compare 2 and 2 ✓
- Both subtrees end together.

Output:

```text
True
```

---

### **Why Two Queues?**

The first queue always explores nodes in the normal order:

- Left child
- Right child

The second queue explores nodes in the mirrored order:

- Right child
- Left child

This ensures that every pair of nodes being compared should be exact mirror images.

---

### **Complexity**

**Time Complexity:** O(n)

- Every node is visited exactly once.

**Space Complexity:** O(n)

- In the worst case, the queues may store an entire level of the binary tree.

---

## 🏁 Conclusion

Using Breadth-First Search (BFS) with two queues allows us to compare mirrored nodes level by level.

By checking both node values and mirrored child positions, we can accurately determine whether the binary tree is symmetric.

This approach is efficient, easy to understand, and runs in linear time.