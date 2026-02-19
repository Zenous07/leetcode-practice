# Single Number

## 🧩 Problem Overview

You are given an array of integers where every element appears exactly twice except for one element which appears only once.

Your task is to find and return that single element.

The solution should correctly identify the element that does not have a duplicate.

---

## 💡 Solution: Sorting and Pair Comparison

### **Method Used**

Sorting + Pairwise Comparison

### **Main Idea**

When the array is sorted, duplicate elements will appear next to each other in pairs.

By iterating through the sorted array and checking elements in pairs:

* If two adjacent elements are equal, they form a valid pair, so skip both.
* If they are not equal, the current element is the single number.
* If all pairs are valid, the last remaining element is the single number.

---

### **Detailed Explanation**

1. Handle edge cases:

   * If the array has only one element, return that element.

2. Sort the array:

   * This ensures duplicate elements are placed next to each other.

3. Use a loop to traverse the array:

   * Start from index `0`.
   * Compare the current element with the next element.
   * If they are equal, move forward by 2 positions (skip the pair).
   * If they are not equal, return the current element.

4. If the loop completes, return the last element:

   * This handles the case where the single number is at the end.

---

### **Example Walkthrough**

Input: [4, 1, 2, 1, 2]

After sorting: [1, 1, 2, 2, 4]

Step-by-step:

* Compare 1 and 1 → pair → skip
* Compare 2 and 2 → pair → skip
* Remaining element → 4 → return 4

---

### **Complexity**

Time Complexity: O(n log n)

* Sorting takes O(n log n)
* Traversal takes O(n)

Space Complexity: O(1)

* No extra space is used apart from variables

---

## 🏁 Conclusion

Sorting makes it easy to group duplicate elements together.
By checking elements in pairs, we can efficiently identify the single element.

This approach is simple, easy to understand, and uses constant extra space.
