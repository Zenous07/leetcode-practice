# Move Zeroes

## 🧩 Problem Overview

You are given an integer array `nums`. Your task is to move all the `0`s to the end of the array while maintaining the relative order of the non-zero elements.

The operation must be performed **in-place**, meaning no additional array should be created.

---

## 💡 Solution: Two-Pointer Approach

### **Method Used**

Two Pointers + In-Place Swapping

### **Main Idea**

Use one pointer to keep track of the position where the next non-zero element should be placed.

Traverse the array from left to right:

* If the current element is non-zero, swap it with the element at the current placement pointer.
* Move the placement pointer forward.
* Ignore zero elements during traversal.

By the end of the traversal, all non-zero elements will be shifted to the front while preserving their original order, and all zeroes will naturally move to the end.

---

### **Detailed Explanation**

1. Initialize a pointer (`curr`) to `0`.

   * This pointer represents the position where the next non-zero element should be placed.

2. Traverse the array from left to right.

3. For each element:

   * If the element is non-zero:
     * Swap it with the element at index `curr`.
     * Increment `curr` by `1`.
   * If the element is zero:
     * Do nothing and continue to the next element.

4. Once the traversal is complete:

   * All non-zero elements will appear at the beginning in their original order.
   * All zeroes will be moved to the end.

---

### **Example Walkthrough**

Input:

[1, 3, 0, 12, 0]

Step-by-step:

* `1` is non-zero → swap with itself → `curr = 1`
* `3` is non-zero → swap with itself → `curr = 2`
* `0` → ignore
* `12` is non-zero → swap with the zero at index `2`
* Array becomes: `[1, 3, 12, 0, 0]`
* `curr = 3`
* Last element is `0` → ignore

Final Output:

[1, 3, 12, 0, 0]

---

### **Complexity**

**Time Complexity:** O(n)

* The array is traversed only once.

**Space Complexity:** O(1)

* Only a single pointer variable is used.
* No extra array is created.

---

## 🏁 Conclusion

The two-pointer approach efficiently moves all non-zero elements to the front while preserving their relative order.

Since the algorithm performs the operation in-place with a single traversal, it achieves optimal **O(n)** time complexity and **O(1)** extra space.