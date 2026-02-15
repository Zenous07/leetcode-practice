# Remove Nth Node From End of List

## 🧩 Problem Overview
You are given the head of a singly linked list and an integer `n`.  
The task is to remove the **nth node from the end** of the list and return the updated head.

The removal should be done efficiently, ideally in **one pass**.

---

## 💡 Solution: Two-Pointer + Dummy Node Approach

### Method Used
Iterative two-pointer technique using a dummy starter node.

---

## 🧠 Core Idea
- Use two pointers: `fast` and `slow`.
- Move the `fast` pointer `n` steps ahead first.
- Then move both `fast` and `slow` one step at a time.
- When `fast` reaches the last node:
  - `slow` will be just before the node to remove.
- Remove the target node by adjusting pointers.

A **dummy node** is used to:
- Handle removal of the head safely.
- Avoid special edge-case handling.

---

## 🔍 Step-by-Step Explanation

1. Create a dummy node and point it to head:
   ```python
   dummy = ListNode(0)
   dummy.next = head
   ```

2. Initialize two pointers:
   ```python
   slow = dummy
   fast = dummy
   ```

3. Move the fast pointer `n` steps forward:
   ```python
   for i in range(n):
       fast = fast.next
   ```

4. Move both pointers until `fast.next` becomes `None`:
   ```python
   while fast.next != None:
       fast = fast.next
       slow = slow.next
   ```

5. Remove the nth node from end:
   ```python
   slow.next = slow.next.next
   ```

6. Return the updated head:
   ```python
   return dummy.next
   ```

---

## ⏱️ Complexity Analysis
Time Complexity: **O(L)**  
Space Complexity: **O(1)**  

Where:
- `L` = length of the linked list  

Only pointers are used. No extra memory is required.

---

## ⚠️ Edge Cases
- List has only one node  
- Removing the head node  
- Removing the last node  
- Removing any middle node  

The dummy node ensures all cases work correctly.

---

## 🏁 Conclusion
This approach removes the nth node from the end efficiently in a single traversal.

Using the two-pointer technique with a dummy node keeps the logic simple,
clean, and handles all edge cases safely.
