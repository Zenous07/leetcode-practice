# Minimum Size Subarray Sum

## 🧩 Problem Overview

You are given an array of positive integers `nums` and a positive integer `target`.

Your task is to find the minimum length of a contiguous subarray whose sum is greater than or equal to `target`.

If no such subarray exists, return `0`.

---

## 💡 Solution: Sliding Window

### **Method Used**

Sliding Window (Two Pointers)

### **Main Idea**

Since all elements in the array are positive, increasing the window size always increases the sum, and shrinking the window always decreases the sum.

Maintain a window using two pointers:

* Expand the window by moving the right pointer and adding elements to the current sum.
* Whenever the current sum becomes greater than or equal to the target, try shrinking the window from the left to find the smallest valid window.
* Keep updating the minimum window length found during the process.

---

### **Detailed Explanation**

1. Initialize two pointers:

   * `left` points to the beginning of the window.
   * `right` expands the window one element at a time.

2. Maintain a running sum:

   * Add the current right element to the window sum.

3. Check if the current window satisfies the condition:

   * While the window sum is greater than or equal to the target:
     * Update the minimum subarray length.
     * Remove the leftmost element from the sum.
     * Move the left pointer forward to shrink the window.

4. Continue until all elements have been processed.

5. If no valid window was found, return `0`; otherwise, return the minimum length.

---

### **Example Walkthrough**

Input:

`target = 7`

`nums = [2, 3, 1, 2, 4, 3]`

Step-by-step:

* Window = `[2]` → Sum = 2
* Window = `[2,3]` → Sum = 5
* Window = `[2,3,1]` → Sum = 6
* Window = `[2,3,1,2]` → Sum = 8 → Valid → Minimum length = 4
* Shrink window → `[3,1,2]` → Sum = 6
* Expand → `[3,1,2,4]` → Sum = 10 → Valid
* Shrink repeatedly:
  * `[1,2,4]` → Length = 3
  * `[2,4]` → Sum = 6
* Expand → `[2,4,3]` → Sum = 9
* Shrink:
  * `[4,3]` → Length = 2 (Best answer)

Return `2`.

---

### **Complexity**

Time Complexity: **O(n)**

* Each element is added to the window once.
* Each element is removed from the window at most once.

Space Complexity: **O(1)**

* Only a few extra variables are used regardless of input size.

---

## 🏁 Conclusion

The Sliding Window technique efficiently finds the minimum-length subarray by dynamically expanding and shrinking the window.

Because every element is processed at most twice, the algorithm runs in linear time while using constant extra space, making it the optimal solution for this problem.