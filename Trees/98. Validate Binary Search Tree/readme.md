# Validate Binary Search Tree

## 🧩 Problem Overview

You are given the root of a binary tree.

Your task is to determine whether the given tree is a **valid Binary Search Tree (BST)**.

A Binary Search Tree satisfies the following conditions:

- Every node in the left subtree has a value **strictly smaller** than the current node.
- Every node in the right subtree has a value **strictly greater** than the current node.
- Both the left and right subtrees must also satisfy the BST property.

The function should return:

- `True` if the tree is a valid BST.
- `False` otherwise.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Level Order Traversal (BFS)

### **Main Idea**

Traverse the binary tree level by level using a queue.

For every node visited:

- Compare the current node with its left child.
- Compare the current node with its right child.
- If a child violates the BST ordering with its parent, immediately return `False`.
- Otherwise, continue traversing the tree.

If every node satisfies these checks, return `True`.

> **Note:** This approach only compares a node with its immediate children. While it works for some simple cases, it does **not** correctly validate every Binary Search Tree because BST rules apply to the entire subtree, not just parent-child relationships.

---

## 📖 Detailed Explanation

1. Handle the empty tree case.

   - If the root is `None`, the tree is considered a valid BST.

2. Create a queue.

   - Add the root node to begin level-order traversal.

3. Traverse the tree while the queue is not empty.

   - Remove the front node from the queue.

4. Check the left child.

   - If the left child exists and its value is greater than or equal to the current node, return `False`.
   - Otherwise, add the left child to the queue.

5. Check the right child.

   - If the right child exists and its value is less than or equal to the current node, return `False`.
   - Otherwise, add the right child to the queue.

6. Continue processing every node.

7. If no violations are found after the traversal, return `True`.

---

## 🌳 Example Walkthrough 1

Input Tree:

```text
      2
     / \
    1   3
```

Processing:

- Visit 2
  - 1 < 2 ✅
  - 3 > 2 ✅
- Visit 1
- Visit 3

No violations are found.

Output:

```text
True
```

---

## 🌳 Example Walkthrough 2

Input Tree:

```text
      5
     / \
    1   4
       / \
      3   6
```

Processing:

- Visit 5
  - 1 < 5 ✅
  - 4 < 5 ❌

The right child should be greater than the parent.

Output:

```text
False
```

---

## ⚠️ Example Where This BFS Approach Fails

Consider the tree:

```text
        10
       /  \
      5    15
          /  \
         6    20
```

The algorithm performs these checks:

- 5 < 10 ✅
- 15 > 10 ✅
- 6 < 15 ✅
- 20 > 15 ✅

It returns:

```text
True
```

However, this tree is **not** a valid BST because the node `6` lies in the right subtree of `10`, so it should be greater than `10`.

The correct answer should be:

```text
False
```

This demonstrates why comparing only a node with its immediate children is insufficient for validating a Binary Search Tree.

---

## 📊 Complexity

### Time Complexity: O(n)

- Every node is visited exactly once.

### Space Complexity: O(n)

- The queue may contain up to an entire level of the tree in the worst case.

---

## 🏁 Conclusion

This Breadth-First Search approach performs a level-order traversal and checks each node against its immediate children.

It correctly detects many simple BST violations and runs in linear time.

However, because it does **not** verify the valid range of values for every subtree, it cannot correctly validate all Binary Search Trees. A complete BST validation requires tracking allowable value ranges (or performing an inorder traversal), ensuring every node satisfies the BST property with respect to all of its ancestors.