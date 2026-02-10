# Merge Two Sorted Lists

## 🧩 Problem Overview
You are given two sorted singly linked lists.
The task is to merge them into a single sorted linked list by reusing and
relinking existing nodes (no new nodes should be created).

---

## 💡 Solution: Two-Pointer + Dummy Node Approach

### **Method Used**
Iterative merge using two pointers and a dummy starter node.

---

## 🧠 Core Idea
- Maintain two pointers, one for each list.
- Compare values at both pointers.
- Attach the smaller node to the merged list.
- Move the pointer forward in the list from which the node was taken.
- Continue until one list is exhausted.
- Append the remaining nodes from the non-empty list.

A **dummy node** is used to simplify edge cases and easily return the head
of the merged list.

---

## 🔍 Step-by-Step Explanation
1. Create a dummy node and a `curr` pointer pointing to it.
2. Initialize two pointers:
   - `curr1` for the first list
   - `curr2` for the second list
3. While both pointers are not `None`:
   - Compare `curr1.val` and `curr2.val`
   - Attach the smaller node to `curr.next`
   - Move the corresponding pointer forward
4. Once one list becomes empty:
   - Attach the remaining nodes of the other list directly
5. Return `dummy.next` as the head of the merged list.

---

## ⏱️ Complexity Analysis
Time Complexity: **O(n + m)**  
Space Complexity: **O(1)**  

Where:
- `n` = number of nodes in list1
- `m` = number of nodes in list2

Only pointers are used; no extra data structures are created.

---

## 🏁 Conclusion
This approach efficiently merges two sorted linked lists in a single pass.
Using a dummy node keeps the logic clean and avoids special handling for
the head of the merged list.
