# Find Closest Number to Zero

## 🧩 Problem Overview
Given an array of integers, the task is to find the number closest to zero.  
If two numbers are equally close to zero (e.g., `-x` and `x`), the positive number should be returned.

---

## 💡 Solution 1: Manual Absolute Comparison

### **Main Idea**
This approach manually computes the absolute value of each number by multiplying negative numbers by `-1`.  
It compares these values to determine which number is closest to zero and updates the result accordingly.  
If two numbers have the same absolute value, the larger (positive) one is selected using the `max()` function.

### **Detailed Explanation**
1. Initialize the first number as the result and compute its absolute value manually.
2. Iterate through each number in the list:
   - Convert the current number to its absolute equivalent (multiply by `-1` if negative).
   - Compare it with the stored closest absolute value.
   - If a smaller absolute value is found, update both the result and the temporary closest absolute value.
   - If an equal absolute value is found, use `max()` to prefer the positive number.
3. Return the result after all numbers are processed.

### **Complexity**
- **Time Complexity:** O(n) — Each element is checked once.  
- **Space Complexity:** O(1) — Uses constant additional memory.

---

## ⚙️ Solution 2: Using Built-in `abs()` Function

### **Main Idea**
This approach simplifies the comparison logic by using Python’s built-in `abs()` function to handle absolute value computation.  
It keeps track of the number closest to zero and updates it during iteration.  
When two numbers have equal distance from zero, it selects the positive one.

### **Detailed Explanation**
1. Start with the first number in the list as the initial result.
2. Loop through the array:
   - Compare the absolute value of the current number with that of the current result using `abs()`.
   - If a smaller absolute value is found, update the result.
   - If an equal absolute value is found, use `max()` to keep the positive number.
3. After traversing the entire list, return the number closest to zero.

### **Complexity**
- **Time Complexity:** O(n) — Single pass through the list.  
- **Space Complexity:** O(1) — No extra data structures used.

---

## 🆚 Comparison Summary

| Aspect | Solution 1 | Solution 2 |
|--------|-------------|-------------|
| Absolute Value Handling | Manual calculation | Built-in `abs()` |
| Readability | Moderate | High |
| Code Length | Longer | Shorter |
| Efficiency | O(n) | O(n) |
| Maintainability | Lower | Higher |

---

## 🏁 Conclusion
Both solutions accurately determine the number closest to zero.  
However, **Solution 2** is more concise, readable, and Pythonic, making it the recommended approach for practical use.
