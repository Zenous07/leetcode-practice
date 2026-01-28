# Daily Temperatures

## 🧩 Problem Overview
Given an array `temperatures` where each element represents the daily temperature,
return an array `answer` such that `answer[i]` is the number of days you have to wait
after the `i`th day to get a warmer temperature.

If no warmer day exists in the future, `answer[i]` should be `0`.

---

## 💡 Solution: Monotonic Stack Method

### **Method Used**
Monotonic Decreasing Stack

### **Main Idea**
This approach uses a stack to keep track of indices of days with unresolved temperatures.
The stack is maintained in **decreasing order of temperatures**.
When a warmer temperature is found, previous colder days are resolved by calculating
the difference in indices.

---

### **Detailed Explanation**
1. Initialize:
   - `result` array filled with `0` (default when no warmer day exists).
   - An empty stack to store pairs `[temperature, index]`.
2. Push the first day's temperature and index onto the stack.
3. Iterate through the temperature list starting from index `1`:
   - If the current temperature is lower than the top of the stack:
     - Push it onto the stack.
   - Otherwise:
     - While the stack is not empty and the current temperature is higher:
       - Pop the top element.
       - Update `result[prev_index] = current_index - prev_index`.
     - Push the current temperature and index onto the stack.
4. Remaining elements in the stack have no warmer future day, so their values remain `0`.
5. Return the `result` array.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

---

## 🆚 Comparison Summary

| Aspect | Brute Force | Monotonic Stack |
|------|------------|----------------|
| Time Complexity | O(n²) | O(n) |
| Space Complexity | O(1) | O(n) |
| Technique | Nested Loops | Stack |
| Performance | Slow | Fast |
| Recommended | ❌ No | ✅ Yes |

---

## 🏁 Conclusion
The **Monotonic Stack Method** efficiently solves the Daily Temperatures problem
by processing each element only once.

It is optimal for large inputs and is the preferred approach for this problem.
