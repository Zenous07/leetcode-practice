# Container With Most Water

## 🧩 Problem Overview
You are given an integer array height where each element represents the height of a vertical line.
Two lines together with the x-axis form a container that can hold water.

The task is to find the maximum amount of water that can be stored.
The container cannot be slanted.

---

## 💡 Solution: Two-Pointer Technique

### **Method Used**
Two-Pointer Approach

### **Main Idea**
This approach uses two pointers starting at both ends of the array.
The area is determined by the shorter line and the distance between the two pointers.
To potentially find a larger area, the pointer pointing to the shorter line is moved inward.

---

### **Detailed Explanation**
1. Initialize two pointers:
   - `l` at the beginning of the array.
   - `r` at the end of the array.
2. While `l` is less than or equal to `r`:
   - Calculate the height of the container as the minimum of `height[l]` and `height[r]`.
   - Calculate the width as `r - l`.
   - Compute the area and update the maximum area found so far.
3. Move the pointer pointing to the shorter line:
   - If `height[l] <= height[r]`, increment `l`.
   - Otherwise, decrement `r`.
4. Continue until the pointers meet.
5. Return the maximum area.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(1)

---

## 🏁 Conclusion
The Two-Pointer technique efficiently solves the problem in linear time and constant space.
It avoids unnecessary comparisons and is the optimal solution for this problem.
