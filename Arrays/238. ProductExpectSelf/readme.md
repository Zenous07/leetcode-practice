# Product of Array Except Self

## 🧩 Problem Overview
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The solution must run in O(n) time and division is not allowed.
The product of any prefix or suffix fits in a 32-bit integer.

---

## 💡 Solution 1: Prefix–Suffix Product Method (Optimized)

### **Method Used**
Prefix and Suffix Product Technique

### **Main Idea**
This method calculates the product of all elements to the left and right of each index separately.
By multiplying the prefix product and suffix product for each index, we get the required result without using division.

---

### **Detailed Explanation**
1. Initialize two arrays:
   - larr[] to store prefix products.
   - rarr[] to store suffix products.
2. Use two variables:
   - l to maintain the running left product.
   - r to maintain the running right product.
3. Traverse the array once:
   - Store the left product in larr[i].
   - Store the right product in rarr[j] using reverse indexing.
   - Update l and r at each step.
4. Traverse the array again:
   - Multiply larr[i] and rarr[i] to compute the final answer.
5. Return the result array.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

---

## ⚙️ Solution 2: Brute Force Nested Loop Method

### **Method Used**
Brute Force with Nested Loops

### **Main Idea**
For each index, this method multiplies all other elements except the current one.
It directly follows the problem statement but is inefficient for large inputs.

---

### **Detailed Explanation**
1. Use two pointers:
   - r represents the index to be excluded.
   - l iterates over the array.
2. For each r:
   - Multiply all elements except nums[r].
   - Store the result in a new list.
3. Repeat until all indices are processed.
4. Return the resulting list.

---

### **Complexity**
Time Complexity: O(n²)  
Space Complexity: O(1)

---

## 🆚 Comparison Summary

| Aspect | Prefix–Suffix Method | Brute Force Method |
|------|---------------------|-------------------|
| Time Complexity | O(n) | O(n²) |
| Space Complexity | O(n) | O(1) |
| Division Used | No | No |
| Performance | Fast | Slow |
| Recommended | Yes | No |

---

## 🏁 Conclusion
The Prefix–Suffix Product Method is the optimal solution as it satisfies all constraints efficiently.
The Brute Force method is useful for understanding but not suitable for large inputs.
