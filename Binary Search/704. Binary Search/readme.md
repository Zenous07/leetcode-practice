# 🔍 Binary Search

## 🧩 Problem Overview
Given a **sorted array of integers** `nums` (in ascending order) and an integer `target`, the task is to find the index of `target` using a **binary search algorithm**.  
If the target value does not exist in the array, return `-1`.

The algorithm must run in **O(log n)** time complexity.

---

## 💡 Solution Explanation

### **Main Idea**
Binary Search efficiently locates an element in a sorted list by repeatedly dividing the search range in half.  
- Begin with two pointers at the start and end of the array.  
- Compare the middle element with the target.  
- If the target is greater, focus on the right half; if smaller, focus on the left half.  
- Continue halving the range until the element is found or the search range becomes invalid.

---

## 🧩 Step-by-Step Breakdown
1. **Initialization**  
   - Left pointer `l` at the start (`0`)  
   - Right pointer `r` at the end (`len(nums) - 1`)

2. **Search Process**  
   - Find the midpoint: `m = (l + r) // 2`  
   - If `nums[m] == target`, return the index `m`.  
   - If `nums[m] < target`, move the left pointer to `m + 1`.  
   - If `nums[m] > target`, move the right pointer to `m - 1`.

3. **Termination**  
   - If pointers cross (`l > r`), the target doesn’t exist → return `-1`.

---

## ⏱️ Complexity Analysis

| Aspect | Complexity |
|--------|-------------|
| **Time Complexity** | O(log n) — halves the search space each iteration |
| **Space Complexity** | O(1) — uses constant extra space |

---

## 🏁 Conclusion
Binary Search is a fundamental algorithm for efficiently locating elements in sorted collections.  
It provides logarithmic performance and is widely used in searching, optimization, and divide-and-conquer problems.
