# Add Two Numbers

## 🧩 Problem Overview

You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in **reverse order**, meaning the first node contains the ones digit, the second node contains the tens digit, and so on.

Your task is to add the two numbers and return the result as a linked list.

---

## 💡 Solution: Convert Linked Lists to Numbers

### **Method Used**

Linked List Traversal + String Conversion + Arithmetic

### **Main Idea**

The linked lists store the digits in reverse order.

The approach is:

1. Traverse the first linked list and collect its digits into a string.
2. Traverse the second linked list and collect its digits into another string.
3. Reverse both strings to obtain the actual numbers.
4. Convert the strings into integers.
5. Add the two integers.
6. Extract the digits of the result one by one using modulo (`% 10`).
7. Create a new linked list containing those digits in reverse order.

---

### **Detailed Explanation**

1. Create a dummy linked-list node:

   * This node is used as the starting point of the result.
   * Keep a reference to this node so the beginning of the result can be returned later.

2. Traverse the first linked list:

   * Read each node's value.
   * Convert the value to a string.
   * Append it to the first number string.

3. Traverse the second linked list:

   * Read each node's value.
   * Append each value to the second number string.

4. Handle empty strings:

   * If a linked list did not contain any digits, treat its value as `0`.

5. Reverse the strings:

   * Since the linked lists store digits in reverse order, reversing the collected strings gives the normal number representation.

6. Convert the strings into integers:

   * This allows normal integer addition to be performed.

7. Add the two numbers:

   * Store the result of the addition.

8. Build the result linked list:

   * Use `% 10` to extract the last digit.
   * Store that digit in the current node.
   * Use integer division by `10` to remove the last digit.
   * Continue until there are no digits left.

---

## 🔍 Example Walkthrough

Suppose the linked lists represent:

```text
l1 = [2, 4, 3]
l2 = [5, 6, 4]