# Trapping Rain Water

## 🧩 Problem Overview
Given an array `height` representing the elevation map where the width of each bar is 1, determine how much rainwater can be trapped after raining.

The goal is to calculate the total amount of water that can be stored between the bars.

---

## ⚙️ Solution 1: Prefix Maximum & Suffix Maximum Arrays (Brute Force)

### **Method Used**
Prefix Maximum and Suffix Maximum Precomputation

### **Main Idea**
For every index, the amount of trapped water depends on the shorter of the tallest bar on its left and the tallest bar on its right.

This method first computes the highest bar on the left and right of every position using two auxiliary arrays. Then, it calculates the trapped water at each index.

---

### **Detailed Explanation**
1. Create two arrays:
   - `left[]` stores the maximum height from the left up to each index.
   - `right[]` stores the maximum height from the right up to each index.
2. Traverse the array from left to right:
   - Keep updating the maximum height seen so far.
   - Store it in the `left[]` array.
3. Simultaneously traverse from right to left:
   - Keep updating the maximum height from the right.
   - Store it in the `right[]` array.
4. Traverse the array once more:
   - The water trapped at each position is:
     - `min(left[i], right[i]) - height[i]`
   - Add this value to the total answer.
5. Return the total trapped water.

---

### **Complexity**
Time Complexity: **O(n)**  
Space Complexity: **O(n)**

---

## 💡 Solution 2: Two Pointer Method (Optimal)

### **Method Used**
Two Pointer Technique

### **Main Idea**
Instead of storing prefix and suffix maximum arrays, maintain two pointers from both ends of the array along with the maximum heights seen so far.

At every step, move the pointer corresponding to the smaller height because the trapped water is limited by the shorter boundary.

---

### **Detailed Explanation**
1. Initialize two pointers:
   - `left` at the beginning.
   - `right` at the end.
2. Maintain:
   - `leftMax` as the tallest bar seen from the left.
   - `rightMax` as the tallest bar seen from the right.
3. While the pointers have not crossed:
   - Update `leftMax` and `rightMax`.
   - Compare the heights at both pointers.
4. If the right bar is smaller:
   - Water trapped depends on `rightMax`.
   - Add `rightMax - height[right]`.
   - Move the right pointer left.
5. Otherwise:
   - Water trapped depends on `leftMax`.
   - Add `leftMax - height[left]`.
   - Move the left pointer right.
6. Continue until both pointers meet.
7. Return the total trapped water.

---

### **Complexity**
Time Complexity: **O(n)**  
Space Complexity: **O(1)**

---

## 🆚 Comparison Summary

| Aspect | Prefix & Suffix Arrays | Two Pointer Method |
|--------|-------------------------|--------------------|
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(n) | O(1) |
| Extra Arrays | Yes | No |
| Performance | Good | Best |
| Recommended | Good for understanding | ✅ Yes |

---

## 🏁 Conclusion
The Prefix & Suffix Maximum approach is easy to understand and demonstrates the core logic behind the problem. However, it requires additional memory to store two auxiliary arrays.

The Two Pointer Method achieves the same result in linear time while using constant extra space, making it the optimal solution for the Trapping Rain Water problem.