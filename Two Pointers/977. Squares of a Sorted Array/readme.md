# Squares of a Sorted Array

## 🧩 Problem Overview

You are given an integer array `nums` sorted in non-decreasing order.

Your task is to return a new array containing the squares of each number, also sorted in non-decreasing order.

Since squaring negative numbers can produce values larger than those from positive numbers, simply squaring each element does not guarantee the array remains sorted.

---

## 💡 Solution: Two Pointer Approach

### **Method Used**

Two Pointers

### **Main Idea**

The array is already sorted, so the largest square will always come from either:

- the leftmost (most negative) element, or
- the rightmost (largest positive) element.

By comparing their squares:

- Place the larger square at the end of the result array.
- Move the corresponding pointer inward.
- Continue until all positions in the result array are filled.

This avoids the need to sort the squared values again.

---

### **Detailed Explanation**

1. Create a result array of the same size as the input array.

2. Initialize two pointers:

   - Left pointer at the beginning.
   - Right pointer at the end.

3. Start filling the result array from the last index.

4. Compare the squares of the left and right elements:

   - If the left square is larger, place it in the current position and move the left pointer forward.
   - Otherwise, place the right square in the current position and move the right pointer backward.

5. Move to the previous position in the result array.

6. Repeat until all elements have been processed.

---

### **Example Walkthrough**

Input:

`[-7, -3, 2, 3, 11]`

Squares:

`[49, 9, 4, 9, 121]`

Step-by-step:

- Compare 49 and 121 → place 121
- Compare 49 and 9 → place 49
- Compare 9 and 9 → place 9
- Compare 9 and 4 → place 9
- Place remaining 4

Final Output:

`[4, 9, 9, 49, 121]`

---

### **Complexity**

**Time Complexity:** O(n)

- Each element is processed exactly once.

**Space Complexity:** O(n)

- A new result array is used to store the sorted squares.

---

## 🏁 Conclusion

The two-pointer approach takes advantage of the sorted nature of the input array.

Instead of squaring all elements and sorting again, it directly builds the sorted squared array in a single traversal, making the solution efficient and easy to understand.