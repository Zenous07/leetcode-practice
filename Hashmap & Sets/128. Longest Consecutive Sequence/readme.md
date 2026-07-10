# Longest Consecutive Sequence

## 🧩 Problem Overview

You are given an unsorted array of integers.

Your task is to find the length of the longest sequence of consecutive integers, regardless of their order in the array.

The solution must run in **O(n)** time.

---

## 💡 Solution: Hash Set

### **Method Used**

Hash Set + Sequence Expansion

### **Main Idea**

Store all numbers in a hash set for **O(1)** average lookup time.

Instead of starting a count from every number, only start counting when the current number is the **beginning of a sequence**. A number is considered the beginning if `num - 1` is not present in the set.

From each starting number, keep checking whether the next consecutive number exists, increasing the sequence length until the sequence ends.

Track the maximum sequence length encountered during the process.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the array is empty, return `0`.

2. Store all numbers in a hash set:

   * This allows constant-time existence checks.

3. Traverse every unique number in the set:

   * Ignore numbers that have a predecessor (`num - 1`) because they are already part of another sequence.
   * Only process numbers that are the start of a new sequence.

4. Expand the sequence:

   * Keep checking whether the next consecutive number exists.
   * Increase the sequence length until the sequence breaks.

5. Update the maximum length:

   * Compare the current sequence length with the maximum found so far.

6. Return the maximum sequence length.

---

### **Example Walkthrough**

Input:

[100, 4, 200, 1, 3, 2]

Hash Set:

{100, 4, 200, 1, 3, 2}

Step-by-step:

* 100 has no predecessor → sequence: 100 → length = 1
* 4 has predecessor (3) → skip
* 200 has no predecessor → sequence: 200 → length = 1
* 1 has no predecessor → sequence: 1 → 2 → 3 → 4 → length = 4
* 3 has predecessor (2) → skip
* 2 has predecessor (1) → skip

Maximum sequence length = **4**

---

### **Complexity**

**Time Complexity:** O(n)

* Building the hash set takes O(n).
* Each number is visited at most once while expanding sequences.
* Overall complexity is O(n).

**Space Complexity:** O(n)

* The hash set stores all unique elements.

---

## 🏁 Conclusion

Using a hash set allows constant-time lookups, making it possible to detect consecutive sequences efficiently.

By only starting from numbers that are the beginning of a sequence, unnecessary work is avoided, ensuring an overall **O(n)** time complexity.

This approach is both efficient and widely considered the optimal solution for the problem.