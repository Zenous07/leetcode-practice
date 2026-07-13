# Max Consecutive Ones III

## 🧩 Problem Overview

You are given a binary array `nums` and an integer `k`.

You may flip at most `k` zeros into ones.

Your task is to determine the maximum number of consecutive `1`s that can be obtained after performing at most `k` flips.

---

## 💡 Solution: Sliding Window

### **Method Used**

Sliding Window (Two Pointers)

### **Main Idea**

Maintain a window that contains at most `k` zeros.

Expand the window by moving the right pointer. Whenever the number of zeros inside the window exceeds `k`, shrink the window from the left until it becomes valid again.

At every step, the current window represents the longest valid subarray ending at the current position. Keep track of the maximum window size encountered.

---

### **Detailed Explanation**

1. Initialize two pointers:

   * `left` marks the beginning of the current window.
   * `right` expands the window one element at a time.

2. Keep a counter for the number of zeros inside the current window.

3. Move the `right` pointer:

   * If the current element is `0`, increment the zero counter.

4. If the zero count becomes greater than `k`:

   * Move the `left` pointer forward.
   * Whenever a zero leaves the window, decrement the zero counter.
   * Continue until the window contains at most `k` zeros.

5. After every expansion, calculate the current window size.

6. Update the maximum window length if the current window is larger.

7. After traversing the entire array, return the maximum window length.

---

### **Example Walkthrough**

Input:

`nums = [1,1,1,0,0,0,1,1,1,1,0]`

`k = 2`

Step-by-step:

* Window expands through the array while counting zeros.
* The first two zeros are allowed.
* When the third zero enters the window, move the left pointer until only two zeros remain.
* Continue expanding and updating the maximum valid window.

Maximum consecutive ones obtained = **6**.

---

### **Complexity**

Time Complexity: **O(n)**

* Each element is visited at most twice (once by the right pointer and once by the left pointer).

Space Complexity: **O(1)**

* Only a few variables are used regardless of the input size.

---

## 🏁 Conclusion

The Sliding Window approach efficiently maintains a valid subarray containing at most `k` zeros.

Since each pointer moves only forward, the algorithm runs in linear time while using constant extra space, making it optimal for large input sizes.