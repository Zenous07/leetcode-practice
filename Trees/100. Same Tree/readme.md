# Same Tree

## 🧩 Problem Overview

You are given the roots of two binary trees, `p` and `q`.

Your task is to determine whether the two trees are **identical**.

Two binary trees are considered the same if:

- They have the same structure.
- Corresponding nodes contain the same values.
- Every left child matches the corresponding left child.
- Every right child matches the corresponding right child.

Return `True` if both trees are identical; otherwise, return `False`.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Parallel Traversal (BFS)

### **Main Idea**

Traverse both trees simultaneously using two queues.

For every pair of nodes:

- Compare their values.
- Ensure both have matching left children.
- Ensure both have matching right children.
- Continue checking until every node has been visited.

If every comparison succeeds, the trees are identical.

---

### **Detailed Explanation**

1. Handle the initial edge cases.

   - If one tree is empty while the other is not, return `False`.
   - If both trees are empty, return `True`.

2. Create two queues.

   - One queue stores nodes from the first tree.
   - The other queue stores nodes from the second tree.

3. Traverse both trees together.

   - Remove one node from each queue.
   - Compare their values.
   - If the values differ, return `False`.

4. Compare the left children.

   - If both exist, add them to their respective queues.
   - If only one exists, the structures differ, so return `False`.

5. Compare the right children.

   - If both exist, add them to their respective queues.
   - If only one exists, return `False`.

6. Continue until both queues become empty.

7. If every comparison succeeds and both queues finish together, return `True`.

---

### **Example Walkthrough 1**

Tree 1:

```text
      1
     / \
    2   3
```

Tree 2:

```text
      1
     / \
    2   3
```

Processing:

- Compare 1 and 1 ✓
- Compare 2 and 2 ✓
- Compare 3 and 3 ✓

Every node matches.

Output:

```text
True
```

---

### **Example Walkthrough 2**

Tree 1:

```text
      1
     / \
    2   1
```

Tree 2:

```text
      1
     / \
    1   2
```

Processing:

- Compare root nodes ✓
- Compare left children → 2 ≠ 1 ✗

The node values differ.

Output:

```text
False
```

---

### **Example Walkthrough 3**

Tree 1:

```text
      1
     /
    2
```

Tree 2:

```text
      1
       \
        2
```

Processing:

- Compare root nodes ✓
- One tree has a left child while the other has a right child.

The structures are different.

Output:

```text
False
```

---

### **Example Walkthrough 4**

Tree 1:

```text
Empty Tree
```

Tree 2:

```text
Empty Tree
```

Processing:

- Both trees are empty.

Output:

```text
True
```

---

### **Why Two Queues?**

Each queue traverses one tree level by level.

At every step:

- Nodes are removed together.
- Their values are compared.
- Their children are checked in the same positions.

Since both traversals stay synchronized, any difference in structure or values is detected immediately.

---

### **Complexity**

**Time Complexity:** O(n)

- Every node in both trees is visited exactly once.

**Space Complexity:** O(n)

- In the worst case, the queues may contain an entire level of the trees.

---

## 🏁 Conclusion

Using Breadth-First Search (BFS), we compare both binary trees level by level.

By checking node values and ensuring corresponding left and right children exist in the same positions, we can determine whether the two trees are identical.

This approach is simple, efficient, and guarantees a correct result with linear time complexity.