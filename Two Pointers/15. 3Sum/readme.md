# 3Sum

## 🧩 Problem Overview
Given an integer array `nums`, return all unique triplets  
`[nums[i], nums[j], nums[k]]` such that:

- `i ≠ j`, `i ≠ k`, `j ≠ k`
- `nums[i] + nums[j] + nums[k] == 0`

The solution must not contain duplicate triplets.  
The order of the output and the order of the triplets does not matter.

---

## 💡 Solution: Sorting + Two-Pointer Method

### **Method Used**
Sorting + Two-Pointer Technique

### **Main Idea**
This approach sorts the array first and then fixes one element at a time.
For each fixed element, the problem reduces to finding two numbers using the
two-pointer technique that sum up to the negative of the fixed element.
Duplicate triplets are avoided by skipping repeated values.

---

### **Detailed Explanation**
1. If the array length is less than or equal to 2, return an empty list.
2. Sort the array to make duplicate handling and pointer movement easier.
3. Iterate through the array using index `curr`:
   - If `nums[curr] > 0`, break early since no valid triplet can sum to zero.
   - Skip duplicate values for `curr` to avoid repeating triplets.
4. For each `curr`, initialize two pointers:
   - `l = curr + 1`
   - `r = len(nums) - 1`
5. While `l < r`:
   - Compute the sum of `nums[curr] + nums[l] + nums[r]`.
   - If the sum is `0`:
     - Add the triplet to the result list.
     - Move both pointers inward.
     - Skip duplicate values for `l` and `r`.
   - If the sum is greater than `0`, decrement `r`.
   - If the sum is less than `0`, increment `l`.
6. Continue until all valid unique triplets are found.

---

### **Complexity**
Time Complexity: O(n²)  
Space Complexity: O(1) *(excluding output list)*

---

## 🆚 Comparison Summary

| Aspect | Brute Force | Sorting + Two Pointers |
|------|------------|------------------------|
| Time Complexity | O(n³) | O(n²) |
| Space Complexity | O(1) | O(1) |
| Duplicate Handling | Manual | Efficient |
| Performance | Very Slow | Fast |
| Recommended | ❌ No | ✅ Yes |

---

## 🏁 Conclusion
The **Sorting + Two-Pointer Method** is the optimal approach for solving the 3Sum problem.

It significantly reduces time complexity, efficiently avoids duplicate triplets,
and works well within the given constraints.
