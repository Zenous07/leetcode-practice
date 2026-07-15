# Path Sum

## 🧩 Problem Overview

You are given the root of a binary tree and an integer `targetSum`.

Your task is to determine whether the tree contains **at least one root-to-leaf path** whose node values add up exactly to `targetSum`.

A **root-to-leaf path** starts at the root node and ends at a leaf node (a node with no children).

The function should return:

- `True` if such a path exists.
- `False` otherwise.

---

## 💡 Solution: Iterative Depth-First Search (DFS)

### **Method Used**

Stack-Based Depth-First Search (DFS)

### **Main Idea**

Instead of using recursion, we use a stack to traverse the binary tree.

Each element stored in the stack contains:

- The current node.
- The sum of values from the root to that node.

As we explore the tree:

- Remove one node from the stack.
- Update the running sum for its children.
- If we reach a leaf node, compare the accumulated sum with `targetSum`.
- If they match, return `True`.
- If the entire tree is traversed without finding a valid path, return `False`.

---

### **Detailed Explanation**

1. Handle the empty tree.

   - If the root is `None`, there is no path, so return `False`.

2. Initialize a stack.

   - Store the root node along with its value as the initial running sum.

3. Traverse the tree while the stack is not empty.

   - Pop the top node and its current path sum.

4. Process the right child.

   - If it exists, push it onto the stack with the updated path sum.

5. Process the left child.

   - If it exists, push it onto the stack with the updated path sum.

6. Check for a leaf node.

   - If the current node has no left or right child, compare its path sum with `targetSum`.

7. If a matching sum is found,

   - Return `True` immediately.

8. If traversal finishes without finding a valid path,

   - Return `False`.

---

## 🌳 Example Walkthrough 1

Binary Tree:

```text
          5
        /   \
       4     8
      /     / \
     11    13  4
    /  \         \
   7    2         1
```

Target Sum:

```text
22
```

Traversal:

- Start at 5 → Sum = 5
- Visit 4 → Sum = 9
- Visit 11 → Sum = 20
- Visit 7 → Sum = 27 ❌
- Visit 2 → Sum = 22 ✅

A valid root-to-leaf path exists.

Output:

```text
True
```

---

## 🌳 Example Walkthrough 2

Binary Tree:

```text
      1
     / \
    2   3
```

Target Sum:

```text
5
```

Possible paths:

- 1 → 2 = 3
- 1 → 3 = 4

Neither equals 5.

Output:

```text
False
```

---

## 🌳 Example Walkthrough 3

Binary Tree:

```text
Empty Tree
```

Target Sum:

```text
0
```

Since there are no paths, the answer is:

```text
False
```

---

## 🌳 Example Walkthrough 4

Binary Tree:

```text
      1
       \
        2
         \
          3
```

Target Sum:

```text
6
```

Path:

- 1 → 2 → 3 = 6

Output:

```text
True
```

---

## 🌳 Example Walkthrough 5

Binary Tree:

```text
      -2
        \
        -3
```

Target Sum:

```text
-5
```

Path:

- -2 → -3 = -5

Output:

```text
True
```

This example shows that the algorithm works correctly even when node values are negative.

---

## ✅ Why Use an Iterative DFS?

Using a stack eliminates the need for recursive function calls.

Advantages include:

- Avoids recursion depth limitations.
- Explicitly tracks the current path sum.
- Visits every node at most once.
- Efficient for large binary trees.

---

## 📊 Complexity

### Time Complexity: **O(n)**

- Every node is visited exactly once.

### Space Complexity: **O(n)**

- In the worst case, the stack may contain up to all nodes along a path (or many nodes in a skewed tree).

---

## 🏁 Conclusion

The iterative Depth-First Search (DFS) approach efficiently checks every root-to-leaf path while maintaining the running sum for each path.

As soon as a leaf node with the required sum is found, the algorithm terminates early and returns `True`.

If no such path exists after exploring the entire tree, it returns `False`.

This solution is simple, avoids recursion, and achieves optimal time complexity of **O(n)**.