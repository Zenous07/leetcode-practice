# Reverse Linked List

## 🧩 Problem Overview
You are given the head of a singly linked list.
Your task is to reverse the linked list and return the new head.

The reversal must be done by modifying the existing node pointers.

---

## 💡 Solution: Iterative Pointer Reversal

### **Method Used**
Three-Pointer Iterative Technique

### **Main Idea**
To reverse a linked list, we change the direction of each node’s `next` pointer.
This is done in-place by carefully tracking:
- the previous node
- the current node
- the next node (to avoid losing the rest of the list)

---

## 🛠️ Detailed Explanation
1. Initialize:
   - `prev` as `None` (will become the new head)
   - `curr` as the current head of the list
2. Traverse the list while `curr` is not `None`:
   - Store `curr.next` in a temporary variable
   - Reverse the pointer: make `curr.next` point to `prev`
   - Move `prev` to `curr`
   - Move `curr` to the saved next node
3. Once traversal is complete:
   - `prev` points to the reversed list head
4. Return `prev`

---

## ⏱️ Complexity
Time Complexity: O(n)  
Space Complexity: O(1)

---

## 🆚 Comparison Summary

| Aspect | Recursive Method | Iterative Method |
|------|-----------------|------------------|
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(n) | O(1) |
| Extra Stack Space | Yes | No |
| Risk of Stack Overflow | Possible | None |
| Recommended | ❌ No | ✅ Yes |

---

## 🏁 Conclusion
The iterative pointer reversal approach is the most efficient way to reverse a linked list.

It runs in linear time, uses constant space, and avoids recursion-related overhead.
