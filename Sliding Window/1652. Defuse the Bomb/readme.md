# Defuse the Bomb

## 🧩 Problem Overview
Given a circular array `code` and an integer `k`, replace every element simultaneously based on the following rules:

- If `k > 0`, replace each element with the sum of the next `k` elements.
- If `k < 0`, replace each element with the sum of the previous `|k|` elements.
- If `k == 0`, replace every element with `0`.

Since the array is circular, indices wrap around from the end to the beginning and vice versa.

---

## 💡 Solution 1: Sliding Window Method (Optimized)

### **Method Used**
Sliding Window Technique

### **Main Idea**
Instead of calculating the required sum separately for every index, maintain a running window sum.
As the window moves, subtract the element leaving the window and add the new element entering it.
This avoids repeated summation and reduces the time complexity to linear time.

---

### **Detailed Explanation**
1. If `k == 0`, return an array filled with `0`s.
2. Create an extended version of the array to simplify circular traversal.
3. Compute the initial window sum:
   - For positive `k`, sum the next `k` elements.
   - For negative `k`, sum the previous `|k|` elements.
4. Store the initial sum as the first answer.
5. Slide the window one position at a time:
   - Remove the element leaving the window.
   - Add the new element entering the window.
   - Store the updated sum.
6. Continue until all indices have been processed.
7. Return the resulting decrypted array.

---

### **Complexity**
Time Complexity: **O(n)**  
Space Complexity: **O(n)**

---

## ⚙️ Solution 2: Brute Force Traversal

### **Method Used**
Nested Loop Simulation

### **Main Idea**
For every index, directly compute the required sum by traversing either the next `k` elements or the previous `|k|` elements one by one.
Although simple and intuitive, this repeats many calculations.

---

### **Detailed Explanation**
1. If `k == 0`, return an array of zeros.
2. Create a result array initialized with zeros.
3. Traverse every index in the array.
4. If `k > 0`:
   - Visit the next `k` circular elements.
   - Add each value to the current answer.
5. If `k < 0`:
   - Visit the previous `|k|` circular elements.
   - Add each value to the current answer.
6. Repeat for every index.
7. Return the completed decrypted array.

---

### **Complexity**
Time Complexity: **O(n × |k|)** (Worst Case: **O(n²)**)  
Space Complexity: **O(n)**

---

## 🆚 Comparison Summary

| Aspect | Sliding Window Method | Brute Force Method |
|------|------------------------|--------------------|
| Time Complexity | O(n) | O(n × \|k\|) (Worst: O(n²)) |
| Space Complexity | O(n) | O(n) |
| Idea | Reuses previous window sum | Computes every sum independently |
| Performance | Fast | Slow |
| Recommended | ✅ Yes | ❌ No |

---

## 🏁 Conclusion
The **Sliding Window** approach is the optimal solution because it avoids repeatedly summing the same elements by updating the running window efficiently. It processes the array in linear time, making it suitable even when `k` is large.

The **Brute Force** approach is easier to understand and closely follows the problem statement, but it performs redundant calculations, resulting in significantly slower execution for larger inputs.