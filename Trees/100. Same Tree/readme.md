# Same Tree

## 🧩 Problem Overview

You are given the roots of two binary trees, `p` and `q`.

Your task is to determine whether the two trees are exactly the same.

Two binary trees are considered identical if they have the same structure and every corresponding node contains the same value.

The function should return `True` if the trees are identical; otherwise, return `False`.

---

## 💡 Solution: Breadth-First Search (BFS)

### **Method Used**

Queue-Based Level Order Traversal (BFS)

### **Main Idea**

Traverse both binary trees simultaneously using two queues.

For every pair of corresponding nodes:

* Compare their values.
* Check whether both have left children.
* Check whether both have right children.
* If both corresponding children exist, add them to their respective queues.
* If any structural mismatch or value mismatch is found, immediately return `False`.

If the traversal completes without finding any differences, the two trees are identical.

---

### **Detailed Explanation**

1. Handle the edge cases:

   * If one tree is empty while the other is not, return `False`.
   * If both trees are empty, return `True`.

2. Create two queues:

   * Add the root of the first tree to the first queue.
   * Add the root of the second tree to the second queue.

3. Traverse both trees while the queues are not empty:

   * Remove one node from each queue.
   * Compare their values.
   * If the values differ, return `False`.

4. Check the left children:

   * If both nodes have left children, add them to their respective queues.
   * If only one node has a left child, return `False`.

5. Check the right children:

   * If both nodes have right children, add them to their respective queues.
   * If only one node has a right child, return `False`.

6. Continue until all corresponding nodes have been processed.

7. If both queues become empty together without finding any mismatch, return `True`.

---

### **Example Walkthrough**

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

Step-by-step:

* Compare root nodes → 1 == 1
* Compare left children → 2 == 2
* Compare right children → 3 == 3
* Both trees finish traversal simultaneously.
* Return `True`.

---

### **Complexity**

Time Complexity: O(n)

* Every node in both trees is visited exactly once.

Space Complexity: O(n)

* The queues may store up to one level of the trees in the worst case.

---

## 🏁 Conclusion

Using Breadth-First Search (BFS), both trees are traversed level by level at the same time.

By comparing node values and verifying that the structure matches throughout the traversal, we can efficiently determine whether the two binary trees are identical.

This approach is simple, effective, and runs in linear time.