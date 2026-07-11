# Contains Duplicate II

## 🧩 Problem Overview

You are given an integer array `nums` and an integer `k`.

Your task is to determine whether there are two distinct indices `i` and `j` such that:

- `nums[i] == nums[j]`
- `|i - j| <= k`

Return `True` if such a pair exists; otherwise, return `False`.

---

## 💡 Solution: Hash Map for Tracking Latest Index

### **Method Used**

Hash Map (Dictionary)

### **Main Idea**

Use a dictionary to store the most recent index of every number encountered while traversing the array.

For each element:

- If it has not been seen before, store its index.
- If it has been seen before, compare the current index with its previously stored index.
- If the difference between the two indices is less than or equal to `k`, return `True`.
- Otherwise, update the stored index to the current one and continue checking.

This ensures that we always compare with the closest previous occurrence of the same value.

---

### **Detailed Explanation**

1. Create an empty dictionary.

   - The dictionary stores each number as the key and its latest index as the value.

2. Traverse the array from left to right.

3. For every element:

   - If the number is not in the dictionary:
     - Store its current index.

   - Otherwise:
     - Calculate the difference between the current index and the stored index.
     - If the difference is less than or equal to `k`, return `True`.
     - Otherwise, update the stored index to the current index.

4. If the traversal completes without finding a valid pair, return `False`.

---

### **Example Walkthrough**

Input:

`nums = [1, 2, 3, 1]`

`k = 3`

Step-by-step:

- Index 0 → Value 1 → Store `{1: 0}`
- Index 1 → Value 2 → Store `{1: 0, 2: 1}`
- Index 2 → Value 3 → Store `{1: 0, 2: 1, 3: 2}`
- Index 3 → Value 1
  - Previous index = 0
  - Difference = 3
  - Since `3 <= k`, return `True`.

---

### **Complexity**

**Time Complexity:** O(n)

- Traverse the array once.
- Dictionary lookups and updates take O(1) on average.

**Space Complexity:** O(n)

- In the worst case, every element is unique and stored in the dictionary.

---

## 🏁 Conclusion

Using a hash map allows us to efficiently track the latest occurrence of each element while traversing the array only once.

This approach avoids unnecessary nested loops, making it an optimal solution with linear time complexity.