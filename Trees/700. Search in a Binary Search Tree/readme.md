# Search in a Binary Search Tree

## 🧩 Problem Overview

You are given the root of a Binary Search Tree (BST) and an integer `val`.

Your task is to find the node whose value is equal to `val` and return the subtree rooted at that node.

If the value does not exist in the BST, return `None`.

---

## 💡 Solution: Recursive Binary Search

### **Method Used**

Recursive Search using BST Properties

### **Main Idea**

A Binary Search Tree follows these rules:

- Every value in the left subtree is smaller than the current node.
- Every value in the right subtree is greater than the current node.

Instead of searching every node, compare the target value with the current node:

- If they are equal, the required node has been found.
- If the target is smaller, continue searching in the left subtree.
- If the target is larger, continue searching in the right subtree.
- If the required child does not exist, the value is not present in the tree.

This allows us to ignore half of the remaining tree at every step.

---

### **Detailed Explanation**

1. Start searching from the root node.

2. Compare the target value with the current node.

   - If both values are equal, return the current node.

3. If the target value is greater than the current node's value:

   - Move to the right child because all larger values are located there.

4. If the target value is smaller than the current node's value:

   - Move to the left child because all smaller values are located there.

5. Repeat this process recursively until:

   - The value is found, or
   - There is no further child to search.

6. If the search reaches a missing child (`None`), the value does not exist in the BST.

---

### **Example Walkthrough 1**

BST:

```text
        4
      /   \
     2     7
    / \
   1   3
```

Target:

```text
val = 2
```

Search Process:

- Start at node 4.
- Since 2 < 4, move left.
- Arrive at node 2.
- Value found.

Returned Subtree:

```text
      2
     / \
    1   3
```

---

### **Example Walkthrough 2**

BST:

```text
        4
      /   \
     2     7
    / \
   1   3
```

Target:

```text
val = 5
```

Search Process:

- Start at node 4.
- Since 5 > 4, move right.
- Reach node 7.
- Since 5 < 7, move left.
- Left child does not exist.
- Stop searching.

Result:

```text
None
```

---

### **Why BST Makes Searching Faster**

Unlike a normal binary tree, a BST keeps its elements in sorted order.

At each comparison, one entire subtree can be discarded.

For example:

```text
        8
      /   \
     3     10
    / \      \
   1   6      14
```

Searching for `14`:

- Compare with 8 → move right.
- Compare with 10 → move right.
- Compare with 14 → found.

Only three nodes are visited instead of searching the entire tree.

---

### **Complexity**

**Time Complexity**

- **Best / Average Case:** `O(log n)`
  - The search moves down one branch of a balanced BST.

- **Worst Case:** `O(n)`
  - If the BST is completely skewed (similar to a linked list), every node may need to be visited.

**Space Complexity**

- **Average Case:** `O(log n)`
  - Due to the recursion stack.

- **Worst Case:** `O(n)`
  - For a highly skewed tree.

---

## 🏁 Conclusion

Using the Binary Search Tree property allows us to efficiently locate a value without exploring every node.

At each step, we eliminate half of the remaining search space by moving either left or right, making the recursive search simple, elegant, and highly efficient for balanced BSTs.