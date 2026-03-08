# Search Insert Position

## 🧩 Problem Overview
Given a sorted array of distinct integers `nums` and a target value, return the index if the target is found.  
If not, return the index where it would be if it were inserted in order.

The solution must run in **O(log n)** time complexity.

---

## 💡 Solution 1: Binary Search (Optimized)

### **Method Used**
Binary Search

### **Main Idea**
Since the array is already sorted in ascending order, Binary Search can be used to efficiently locate the target element.  
If the target is not present, the final position of the left pointer represents the correct insertion index.

---

### **Detailed Explanation**
1. Initialize two pointers:
   - One at the beginning of the array.
   - One at the end of the array.
2. Repeatedly calculate the middle index.
3. Compare the middle element with the target:
   - If equal → return the middle index.
   - If the middle element is smaller → search in the right half.
   - If the middle element is larger → search in the left half.
4. If the loop finishes without finding the target:
   - The left pointer will indicate the correct position where the target should be inserted.

---

### **Complexity**
Time Complexity: O(log n)  
Space Complexity: O(1)

---

## ⚙️ Solution 2: Brute Force Linear Scan

### **Method Used**
Linear Search

### **Main Idea**
Traverse the array from left to right and stop when:
- The current element becomes greater than or equal to the target.
- Or the end of the array is reached.

The stopping index is the correct insert position.

---

### **Detailed Explanation**
1. Start from the first index.
2. Compare each element with the target.
3. Continue moving forward while the target is greater than the current element.
4. When the condition fails, return the current index as the insertion position.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(1)

---

## 🆚 Comparison Summary

| Aspect | Binary Search | Brute Force |
|--------|--------------|-------------|
| Time Complexity | O(log n) | O(n) |
| Space Complexity | O(1) | O(1) |
| Performance | Fast | Slower |
| Recommended | ✅ Yes | ❌ No |

---

## 🏁 Conclusion
The Binary Search approach is the optimal solution because it satisfies the required **O(log n)** runtime complexity.

The Brute Force method is easier to understand but not efficient for large inputs.