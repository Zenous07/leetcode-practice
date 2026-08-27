# Valid Perfect Square

## 🧩 Problem Overview

You are given a positive integer `num`. 

Your task is to return `True` if `num` is a perfect square, or `False` otherwise.

A perfect square is an integer that is the square of an integer (in other words, it is the product of an integer with itself). You must not use any built-in library functions like `sqrt`.

---

## 💡 Solution: Binary Search

### **Method Used**

Binary Search

### **Main Idea**

Since the square root of a number `num` (where `num >= 1`) will always lie between `1` and `num // 2`, we can use binary search to efficiently find if an integer square exists.

By narrowing down the search space:

* Calculate the middle element `mid`.
* Find its square (`mid * mid`).
* If `square == num`, we found the exact square root, return `True`.
* If `square < num`, the square root must be larger, so move the `left` pointer to `mid + 1`.
* If `square > num`, the square root must be smaller, so move the `right` pointer to `mid - 1`.

---

### **Detailed Explanation**

1. Handle edge cases:

    * If `num < 1`, it cannot be a perfect square, return `False`.
    * If `num == 1`, it is a perfect square, return `True`.

2. Initialize search boundaries:

    * `left = 1`, `right = num // 2`.

3. Use a binary search loop:

    * Loop while `left <= right`.
    * Compute `mid = left + (right - left) // 2` to prevent potential integer overflow.
    * Compare `square = mid * mid` with `num`.

4. Termination:

    * If the loop finishes without finding a match, return `False`.

---

### **Example Walkthrough**

Input: `num = 16`

* Initial bounds: `left = 1`, `right = 8`
* Iteration 1: `mid = 4`, `square = 16`
    * `16 == 16` → return `True`

Input: `num = 14`

* Initial bounds: `left = 1`, `right = 7`
* Iteration 1: `mid = 4`, `square = 16` (`16 > 14` → `right = 3`)
* Iteration 2: `mid = 2`, `square = 4` (`4 < 14` → `left = 3`)
* Iteration 3: `mid = 3`, `square = 9` (`9 < 14` → `left = 4`)
* Loop ends (`left > right`) → return `False`

---

### **Complexity**

Time Complexity: O(log n)

* The search space is halved in each step using binary search.

Space Complexity: O(1)

* Only a few variables (`left`, `right`, `mid`, `square`) are used.

---

## 🏁 Conclusion

Binary search provides an optimal and efficient approach to finding whether a number is a perfect square without needing heavy mathematical functions or linear scanning.