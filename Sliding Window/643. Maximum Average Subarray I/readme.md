# Maximum Average Subarray I

## 🧩 Problem Overview

You are given an integer array `nums` and an integer `k`.

Your task is to find the contiguous subarray of length exactly `k` that has the maximum average value and return that average.

A brute-force approach would compute the sum of every possible subarray of size `k`, but that would repeatedly calculate overlapping sums, making it inefficient.

---

## 💡 Solution: Sliding Window

### **Method Used**

Sliding Window

### **Main Idea**

Since every subarray has the same fixed size (`k`), there is no need to compute the sum from scratch for every window.

Instead:

* Compute the sum of the first window of size `k`.
* Slide the window one element at a time.
* Add the new element entering the window.
* Remove the element leaving the window.
* Keep track of the maximum average seen so far.

This reduces unnecessary repeated calculations.

---

### **Detailed Explanation**

1. Check if the array length is smaller than `k`.

   * If so, return `0` since no valid subarray exists.

2. Compute the sum of the first `k` elements.

   * This becomes the sum of the initial window.

3. Compute the average of this first window.

   * Store it as the current maximum average.

4. Slide the window through the array.

   * Add the next element entering the window.
   * Subtract the element leaving the window.
   * Compute the new average.
   * Update the maximum average if the current one is larger.

5. Continue until every possible window has been processed.

6. Return the maximum average found.

---

### **Example Walkthrough**

Input:

`nums = [1, 12, -5, -6, 50, 3]`

`k = 4`

First window:

`[1, 12, -5, -6]`

Sum = 2

Average = 0.5

Slide the window:

Remove `1`, Add `50`

Window:

`[12, -5, -6, 50]`

Sum = 51

Average = 12.75

Slide again:

Remove `12`, Add `3`

Window:

`[-5, -6, 50, 3]`

Sum = 42

Average = 10.5

The maximum average encountered is **12.75**.

---

### **Complexity**

Time Complexity: **O(n)**

* Computing the initial window sum takes **O(k)**.
* Sliding the window across the remaining elements takes **O(n - k)**.
* Overall complexity is **O(n)**.

Space Complexity: **O(1)**

* Only a few variables are used regardless of the input size.

---

## 🏁 Conclusion

The Sliding Window technique is ideal for problems involving contiguous subarrays of fixed size.

Instead of recalculating each window's sum from scratch, the algorithm updates the sum in constant time by adding the incoming element and removing the outgoing one.

This achieves an optimal **O(n)** time complexity while using only **O(1)** extra space.