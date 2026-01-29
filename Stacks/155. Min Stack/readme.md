# Min Stack

## 🧩 Problem Overview
Design a stack that supports the following operations in constant time:

- Push an element onto the stack
- Pop the top element from the stack
- Retrieve the top element
- Retrieve the minimum element in the stack

All operations must run in **O(1)** time.

---

## 💡 Solution: Two Stack Method

### **Method Used**
Auxiliary Minimum Stack

### **Main Idea**
This approach uses **two stacks**:
- A main stack to store all pushed values
- A secondary stack to keep track of the minimum value at each level

The minimum stack mirrors the main stack in size and stores the minimum value
up to that point. This allows retrieving the minimum element in constant time.

---

## 🛠️ Detailed Explanation
1. Initialize:
   - One stack to store all elements.
   - One stack to track the minimum value corresponding to each element.

2. **Push Operation**
   - Push the value into the main stack.
   - Compare the value with the current minimum:
     - Push the smaller value into the minimum stack.

3. **Pop Operation**
   - Pop elements from both stacks to keep them synchronized.

4. **Top Operation**
   - Return the top element from the main stack.

5. **Get Minimum Operation**
   - Return the top element from the minimum stack, which represents
     the minimum value currently in the stack.

---

## ⏱️ Complexity
Time Complexity: O(1)  
Space Complexity: O(n)

---

## 🆚 Comparison Summary

| Aspect | Brute Force Stack | Two Stack Method |
|------|------------------|----------------|
| Get Minimum | O(n) | O(1) |
| Extra Space | O(1) | O(n) |
| Performance | Slow | Fast |
| Recommended | ❌ No | ✅ Yes |

---

## 🏁 Conclusion
The **Two Stack Method** efficiently supports all stack operations,
including retrieving the minimum element in constant time.

This approach is optimal and widely used for implementing a Min Stack.
