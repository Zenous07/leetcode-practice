# Middle of the Linked List

## 🧩 Problem Overview
Given the head of a singly linked list, return the middle node.
If the list contains two middle nodes, return the second one.

---

## 💡 Solution: Two-Pointer (Slow and Fast) Technique

### **Method Used**
Floyd’s two-pointer approach (same pattern as cycle detection,
but used here to find the midpoint).

---

## 🧠 Core Idea
Use two pointers moving at different speeds:

- A **slow pointer** moves one step at a time.
- A **fast pointer** moves two steps at a time.

When the fast pointer reaches the end of the list,
the slow pointer will be at the middle.

If the list has an even number of nodes,
the slow pointer naturally lands on the **second middle node**,
which satisfies the problem requirement.

---

## 🔍 Step-by-Step Explanation
1. Initialize both `slow` and `fast` pointers at the head.
2. Traverse the list while:
   - `fast` is not `None`
   - `fast.next` is not `None`
3. In each iteration:
   - Move `slow` one step forward.
   - Move `fast` two steps forward.
4. When the loop stops:
   - `slow` will point to the middle node.
5. Return the `slow` pointer.

---

## ⏱️ Complexity Analysis
Time Complexity: **O(n)**  
Space Complexity: **O(1)**  

Only constant extra space is used.

---

## 🏁 Conclusion
This approach efficiently finds the middle node in a single pass
without calculating the length of the list.
The two-pointer technique is optimal and elegant for linked list problems.
