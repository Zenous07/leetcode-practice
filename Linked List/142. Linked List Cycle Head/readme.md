# Linked List Cycle II

## 🧩 Problem Overview
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

---

## 💡 Solution: Two-Pointer (Tortoise and Hare) Technique

### **Method Used**
Floyd’s cycle-finding algorithm. It is a memory-efficient approach to detect cycles and identify the exact entry node without extra data structures.



---

## 🧠 Core Idea
Use two pointers moving at different speeds to identify the cycle:

1. **Detection:** A `slow` pointer moves one step at a time, and a `fast` pointer moves two steps at a time. If there is a cycle, the `fast` pointer will eventually catch up to the `slow` pointer from behind.
2. **Finding the Entrance:** Once a collision occurs, reset the `slow` pointer to the head of the list. Move both pointers one step at a time. The node where they meet again is mathematically guaranteed to be the start of the cycle.

---

## 🔍 Step-by-Step Explanation
1. Initialize both `slow` and `fast` pointers at the head of the list.
2. Traverse the list:
   - Move `slow` forward by one node.
   - Move `fast` forward by two nodes.
3. Check for intersection:
   - If `fast` or `fast.next` reaches the end of the list, there is no cycle; return `null`.
   - If `slow == fast`, a cycle exists.
4. Locate the entrance:
   - Reset `slow` to the `head` of the list.
   - Keep `fast` at the meeting point.
   - Move both pointers one step at a time until they meet again.
5. Return the current node (the meeting point).

---

## ⏱️ Complexity Analysis
Time Complexity: **O(n)** Space Complexity: **O(1)** No additional data structures (like HashSets) are needed to track visited nodes.

---

## 🏁 Conclusion
This approach is optimal for memory. By leveraging the mathematical properties of the cycle's structure, we can identify the entry point in a single pass after the initial detection, keeping the space complexity constant.