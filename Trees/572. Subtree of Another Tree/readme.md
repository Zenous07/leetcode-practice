# Subtree of Another Tree

## 🧩 Problem Overview

You are given the roots of two binary trees: `root` and `subRoot`.

Your task is to determine whether `subRoot` exists as a subtree of `root`.

A subtree is formed by any node in the original tree along with all of its descendants. Both the structure of the tree and the values of every corresponding node must match exactly.

The function should return:

- `True` if `subRoot` is a subtree of `root`
- `False` otherwise

---

## 💡 Solution: Breadth-First Search (BFS) + Tree Comparison

### **Method Used**

- Breadth-First Search (BFS) to search the main tree.
- BFS again to compare two trees whenever a possible matching root is found.

### **Main Idea**

Traverse every node of the main tree using a queue.

Whenever a node has the same value as the root of `subRoot`, perform a complete tree comparison.

During comparison:

- Both node values must be equal.
- Their left children must either both exist or both be absent.
- Their right children must either both exist or both be absent.

If every corresponding node matches, then `subRoot` is a valid subtree.

If not, continue searching the remaining nodes of the main tree.

---

### **Detailed Explanation**

1. Handle edge cases:

   - If both trees are empty, return `True`.
   - If only one tree is empty, return `False`.

2. Create a queue containing the root of the main tree.

3. Traverse the main tree using BFS.

4. For each node:

   - Compare its value with the root of `subRoot`.
   - If the values differ, continue searching.

5. If the values match:

   - Start another BFS to compare both trees node by node.
   - Check that:
     - Current node values are equal.
     - Left children match in both existence and value.
     - Right children match in both existence and value.

6. If any mismatch occurs:

   - Stop comparing.
   - Resume searching the remaining nodes in the main tree.

7. If every node in both comparison queues is processed successfully:

   - Return `True`.

8. If the entire main tree is searched without finding a matching subtree:

   - Return `False`.

---

### **Example Walkthrough 1**

Main Tree:

```text
       3
      / \
     4   5
    / \
   1   2
```

Subtree:

```text
     4
    / \
   1   2
```

Traversal:

- Visit node 3 → values do not match.
- Visit node 4 → values match.
- Compare both trees.
- Every node matches.

Result:

```text
True
```

---

### **Example Walkthrough 2**

Main Tree:

```text
        3
       / \
      4   5
     / \
    1   2
       /
      0
```

Subtree:

```text
     4
    / \
   1   2
```

Traversal:

- Visit node 3 → no match.
- Visit node 4 → possible match.
- Compare trees.
- Extra node (0) exists in the main tree.
- Structures differ.

Continue searching.

No other valid subtree exists.

Result:

```text
False
```

---

### **Example Walkthrough 3**

Main Tree:

```text
      1
     /
    1
   /
  1
```

Subtree:

```text
    1
   /
  1
```

Traversal:

- First node partially matches but structure differs.
- Continue searching.
- Second node matches perfectly.

Result:

```text
True
```

---

### **Why BFS Works Well**

This approach separates the problem into two parts:

1. Search every possible starting node in the main tree.
2. Verify whether the two trees are identical from that starting point.

Since every node in the main tree is considered once, no possible subtree is missed.

---

## 📊 Complexity

### Time Complexity

**O(n × m)**

- `n` = number of nodes in `root`
- `m` = number of nodes in `subRoot`

In the worst case, every node of the main tree may trigger a full subtree comparison.

---

### Space Complexity

**O(n + m)**

- The search queue can contain nodes from the main tree.
- The comparison queues store nodes from both trees during subtree verification.

---

## 🏁 Conclusion

This approach first searches the main tree using Breadth-First Search (BFS).

Whenever a node has the same value as the root of `subRoot`, another BFS compares both trees node by node.

By verifying both node values and tree structure, the algorithm correctly determines whether `subRoot` exists within `root`.

Although the worst-case time complexity is **O(n × m)**, the solution is straightforward, easy to understand, and works reliably for all valid binary trees.