# Linked List Cycle

## 🧩 Problem Overview
Given the head of a singly linked list, determine whether the list contains
a cycle. A cycle exists if a node can be revisited by continuously following
the `next` pointer.

---

## 💡 Solution: Floyd’s Tortoise and Hare Algorithm

### **Method Used**
Two-pointer technique (slow and fast pointers)

---

## 🧠 Core Idea
Use two pointers moving at different speeds:
- A **slow pointer** moves one step at a time.
- A **fast pointer** moves two steps at a time.

If the linked list has a cycle, the fast pointer will eventually catch up
to the slow pointer inside the cycle.

If the list has no cycle, the fast pointer will reach the end (`None`).

---

## 🔍 Step-by-Step Explanation
1. Initialize both `slow` and `fast` pointers to the head of the list.
2. Traverse the list while:
   - `fast` is not `None`
   - `fast.next` is not `None`
3. Move:
   - `slow` one step forward
   - `fast` two steps forward
4. After each move:
   - If `slow` and `fast` point to the same node, a cycle exists → return `True`
5. If the loop ends without pointers meeting, no cycle exists → return `False`

---

## ⏱️ Complexity Analysis
Time Complexity: **O(n)**  
Space Complexity: **O(1)**  

Only two pointers are used, regardless of list size.

---

## 🏁 Conclusion
This approach efficiently detects cycles without using extra memory.
Floyd’s algorithm is optimal and widely used for cycle detection problems
in linked lists.
