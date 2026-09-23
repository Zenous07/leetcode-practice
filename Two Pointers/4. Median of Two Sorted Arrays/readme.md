# Median of Two Sorted Arrays

## 🧩 Problem Overview

You are given two sorted arrays `nums1` and `nums2` of sizes `m` and `n` respectively.

Your task is to find and return the median of the two sorted arrays.

The median is defined as:
* If the total number of elements is **even**: the average of the two middle elements
* If the total number of elements is **odd**: the middle element

The overall runtime complexity should be optimal.

---

## 💡 Solution: Merge and Find Middle Elements

### **Method Used**

Two-Pointer Merge + Middle Element Selection

### **Main Idea**

Instead of fully merging the arrays (which would be O(m+n) space), we:

1. Use two pointers to traverse both sorted arrays simultaneously
2. Merge elements in sorted order into a result list
3. Stop merging once we've collected enough elements to find the median
4. Calculate the median from the last one or two elements collected

By only collecting elements up to the middle position, we avoid unnecessary iterations.

---

### **Algorithm Breakdown**

**Step 1: Determine How Many Elements to Collect**

* If total length is even: collect `(m+n)/2 + 1` elements
* If total length is odd: collect `(m+n)//2 + 1` elements

This ensures we have the median element(s) in our result list.

**Step 2: Two-Pointer Merge**

* Initialize pointers `l` and `r` at the start of each array
* Compare elements at both pointers:
  * If `nums1[l] <= nums2[r]`, append `nums1[l]` and increment `l`
  * Otherwise, append `nums2[r]` and increment `r`
* If one pointer reaches the end, continue with the remaining array

**Step 3: Calculate Median**

* If total length is even: return average of last two elements
* If total length is odd: return the last element as a float

---

### **Example Walkthrough**

**Example 1: Odd Total Length**

```
nums1 = [1, 3]
nums2 = [2]
Total length = 3 (odd)
Elements to collect = 3//2 + 1 = 2

Merging process:
- Compare 1 and 2 → append 1 → res = [1]
- Compare 3 and 2 → append 2 → res = [1, 2]
- Collected 2 elements, stop

Median = res[-1] = 2.0
```

**Example 2: Even Total Length**

```
nums1 = [1, 2]
nums2 = [3, 4]
Total length = 4 (even)
Elements to collect = 4/2 + 1 = 3

Merging process:
- Compare 1 and 3 → append 1 → res = [1]
- Compare 2 and 3 → append 2 → res = [1, 2]
- Compare 2 and 3 → append 3 → res = [1, 2, 3]
- Collected 3 elements, stop

Median = (res[-1] + res[-2]) / 2 = (3 + 2) / 2 = 2.5
```

**Example 3: Empty Array**

```
nums1 = []
nums2 = [1, 2, 3]
Total length = 3 (odd)
Elements to collect = 2

Merging process:
- nums1 is empty, so append from nums2
- res = [1, 2]

Median = 2.0
```

**Example 4: All Elements from First Array**

```
nums1 = [1, 2, 3, 4, 5]
nums2 = []
Total length = 5 (odd)
Elements to collect = 3

Merging process:
- nums2 is empty, append from nums1
- res = [1, 2, 3]

Median = 3.0
```

---

### **Complexity Analysis**

**Time Complexity: O(m + n)**
* We iterate through both arrays in the worst case (when collecting elements)
* Typically, we only iterate up to the middle position, so in practice it's O((m+n)/2)

**Space Complexity: O(m + n)**
* We use a result list that stores up to m+n elements
* In the worst case (when total length is even), we store (m+n)/2 + 1 elements

---

## 🔍 Optimized Approach (Optional)

For O(log(min(m, n))) time complexity, a binary search approach can be used:

* Binary search on the smaller array to partition both arrays
* Ensure left partition elements ≤ right partition elements
* Calculate median from partition edges

However, the merge approach is more intuitive and practical for most use cases.

---

## 🏁 Conclusion

The two-pointer merge approach:
* ✅ Simple and intuitive to understand
* ✅ Handles all edge cases naturally (empty arrays, different sizes)
* ✅ Works efficiently for most practical scenarios
* ✅ Easy to implement without complex binary search logic

Perfect for interviews when clarity and correctness matter more than optimal complexity.