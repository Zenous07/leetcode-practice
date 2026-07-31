# Merge Intervals

## 🧩 Problem Overview

You are given a list of intervals, where each interval is represented as `[start, end]`.

Some intervals may overlap with each other.

Your task is to merge all overlapping intervals and return a new list containing only the merged, non-overlapping intervals.

---

## 💡 Solution: Sorting and Interval Merging

### **Method Used**

Sorting + Greedy Merging

### **Main Idea**

The first step is to sort the intervals based on their starting values.

Once sorted:

* If the current interval overlaps with the previous one, merge them by extending the ending point.
* If there is no overlap, store the previous interval and start a new one.

This guarantees that every interval is processed only once after sorting.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the list contains zero or one interval, simply return it because no merging is required.

2. Sort the intervals:

   * Sorting arranges intervals in ascending order of their starting values.
   * This makes overlapping intervals appear next to each other.

3. Initialize the first interval:

   * Store the start and end of the first interval.

4. Traverse the remaining intervals:

   * If the current interval starts before or at the current ending point, the intervals overlap.
   * Update the ending point using the larger ending value.
   * Otherwise:
     * Store the current merged interval.
     * Begin tracking the new interval.

5. After the loop ends:

   * Add the final merged interval to the result.

6. Return the merged list.

---

### **Example Walkthrough**

Input:

```
[[1,3],[2,6],[8,10],[15,18]]
```

After sorting:

```
[[1,3],[2,6],[8,10],[15,18]]
```

Step-by-step:

* Start with `[1,3]`
* `[2,6]` overlaps with `[1,3]` → merge → `[1,6]`
* `[8,10]` does not overlap → store `[1,6]`
* Start new interval `[8,10]`
* `[15,18]` does not overlap → store `[8,10]`
* Store the final interval `[15,18]`

Output:

```
[[1,6],[8,10],[15,18]]
```

---

### **Another Example**

Input:

```
[[1,4],[4,5]]
```

Since the second interval starts exactly where the first one ends, they are considered overlapping.

Output:

```
[[1,5]]
```

---

### **Complexity**

**Time Complexity:** O(n log n)

* Sorting the intervals takes **O(n log n)**.
* Traversing the sorted list takes **O(n)**.

Overall:

```
O(n log n)
```

---

**Space Complexity:** O(n)

* A new list is used to store the merged intervals.

---

## 🏁 Conclusion

Sorting places overlapping intervals next to each other, making them easy to merge in a single traversal.

By updating the ending point whenever an overlap is found, we efficiently combine intervals while preserving the correct order.

This greedy approach is simple, efficient, and is one of the most commonly used solutions for the Merge Intervals problem.