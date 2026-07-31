# Compute Alternating Sum

## 🧩 Problem Overview

You are given an integer array `nums`.

The **alternating sum** is calculated by adding elements at even indices and subtracting elements at odd indices.

In other words:

`nums[0] - nums[1] + nums[2] - nums[3] + ...`

Your task is to compute and return the alternating sum of the given array.

---

## 💡 Solution: Single Traversal with Index Parity

### **Method Used**

Linear Traversal + Index Parity Check

### **Main Idea**

Traverse the array from left to right.

For each index:

- If the index is **even**, add the element to the answer.
- If the index is **odd**, subtract the element from the answer.

Continue until all elements have been processed.

---

### **Detailed Explanation**

1. Initialize a variable to store the alternating sum.

2. Traverse the array from index `0` to `n - 1`.

3. For each index:

   * If the index is even, add the current element.
   * If the index is odd, subtract the current element.

4. After processing every element, return the final alternating sum.

---

### **Example Walkthrough**

Input:

`[1, 3, 5, 7]`

Step-by-step:

* Index 0 (even): `0 + 1 = 1`
* Index 1 (odd): `1 - 3 = -2`
* Index 2 (even): `-2 + 5 = 3`
* Index 3 (odd): `3 - 7 = -4`

Final Answer:

`-4`

---

### **Another Example**

Input:

`[10, 20, 30, 40, 50]`

Calculation:

`10 - 20 + 30 - 40 + 50`

Answer:

`30`

---

### **Edge Case**

Input:

`[100]`

Since there is only one element (at an even index), the alternating sum is simply:

`100`

---

### **Complexity**

**Time Complexity:** `O(n)`

- The array is traversed exactly once.

**Space Complexity:** `O(1)`

- Only one variable is used to store the running sum.

---

## 🏁 Conclusion

This approach processes each element exactly once while checking whether its index is even or odd.

It is simple, efficient, and requires constant extra space, making it an optimal solution for computing the alternating sum.