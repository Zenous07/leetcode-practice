# Remove Duplicates from Sorted List

## 🧩 Problem Overview
You are given the head of a **sorted singly linked list**.
Remove all duplicate elements so that each value appears **only once**.

The linked list must remain sorted after removing duplicates.

---

## 💡 Solution: In-Place Linked List Traversal

### **Method Used**
Single Pointer Traversal

### **Main Idea**
Because the linked list is **already sorted**, duplicate values will always appear
**next to each other**.

By traversing the list once and comparing each node with its next node,
duplicates can be removed by adjusting pointers directly—without using extra memory.

---

## 🛠️ Detailed Explanation
1. If the linked list is empty, return the head immediately.
2. Start traversing from the head node using a pointer.
3. Compare the current node’s value with the next node’s value:
   - If both values are the same, skip the next node by updating pointers.
   - Otherwise, move the pointer forward.
4. Continue this process until the end of the list is reached.
5. Return the modified linked list head.

---

## ⏱️ Complexity
Time Complexity: O(n)  
Space Complexity: O(1)

---

## 🆚 Comparison Summary

| Aspect | Brute Force | In-Place Traversal |
|------|------------|-------------------|
| Time Complexity | O(n²) | O(n) |
| Space Complexity | O(n) | O(1) |
| Extra Memory | Yes | No |
| Performance | Slow | Fast |
| Recommended | ❌ No | ✅ Yes |

---

## 🏁 Conclusion
Since the linked list is sorted, duplicate removal can be done efficiently
with a single traversal.

The in-place pointer approach is optimal and avoids unnecessary memory usage,
making it the preferred solution for this problem.
