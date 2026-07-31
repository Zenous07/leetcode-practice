# Insert Interval

## 🧩 Problem Overview

You are given a list of non-overlapping intervals sorted by their starting values and a new interval.

Your task is to insert the new interval into the correct position while maintaining the sorted order and ensuring that no overlapping intervals remain.

If the new interval overlaps with one or more existing intervals, they should be merged into a single interval.

---

## 💡 Solution: Linear Traversal and Interval Merging

### **Method Used**

Linear Traversal + Interval Merging

### **Main Idea**

The algorithm processes the intervals in three phases:

* Add all intervals that come completely before the new interval.
* Merge every interval that overlaps with the new interval.
* Add all remaining intervals that come after the merged interval.

Since the intervals are already sorted and non-overlapping, a single traversal is sufficient.

---

### **Detailed Explanation**

1. Create an empty result list.

   * This will store the final list of intervals.

2. Add all non-overlapping intervals before the new interval.

   * If an interval ends before the new interval starts, it cannot overlap.
   * Add it directly to the result.

3. Merge overlapping intervals.

   * While the current interval overlaps with the new interval:
     * Update the start of the new interval to the smaller starting value.
     * Update the end of the new interval to the larger ending value.
   * This continuously expands the new interval until all overlaps are merged.

4. Add the merged interval.

   * After all overlapping intervals have been processed, append the merged interval to the result.

5. Add the remaining intervals.

   * Any intervals left after the merge cannot overlap.
   * Append them directly to the result.

6. Return the result list.

---

### **Example Walkthrough**

Input:

```
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
```

Step-by-step:

* Add `[1,2]` since it ends before the new interval starts.
* `[3,5]` overlaps → merge → new interval becomes `[3,8]`.
* `[6,7]` overlaps → merged interval remains `[3,8]`.
* `[8,10]` overlaps → merged interval becomes `[3,10]`.
* Add the merged interval `[3,10]`.
* Add the remaining interval `[12,16]`.

Final Output:

```
[[1,2],[3,10],[12,16]]
```

---

### **Complexity**

**Time Complexity:** O(n)

* Each interval is visited only once.

**Space Complexity:** O(n)

* A new result list is created to store the final intervals.

---

## 🏁 Conclusion

Because the intervals are already sorted and non-overlapping, the insertion can be completed in a single pass.

By first collecting non-overlapping intervals, then merging all overlapping ones, and finally appending the remaining intervals, the algorithm efficiently produces the correct list of intervals with only one traversal.