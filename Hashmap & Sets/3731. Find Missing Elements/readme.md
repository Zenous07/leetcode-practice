# Find Missing Elements

## 🧩 Problem Overview

You are given an array of **unique integers**. Originally, the array contained every integer within a continuous range, but some numbers may have been removed.

The smallest and largest numbers of the original range are guaranteed to still be present.

Your task is to return all the missing integers between the minimum and maximum values in **sorted order**.

---

## 💡 Solution: Hash Set Lookup

### **Method Used**

Hash Set + Range Traversal

### **Main Idea**

A hash set allows us to check whether a number exists in constant time.

The approach is:

* Find the smallest and largest numbers in the array.
* Store all numbers in a hash set for fast lookup.
* Traverse every integer from the minimum value to the maximum value.
* If a number is not present in the hash set, add it to the result list.
* Return the list of missing numbers.

---

### **Detailed Explanation**

1. Find the minimum and maximum values in the array.

   * These define the complete range of numbers.

2. Convert the array into a hash set.

   * This allows checking whether a number exists in **O(1)** average time.

3. Traverse the entire range.

   * Start from the minimum value.
   * Continue until the maximum value.
   * For every number:
     * If it exists in the set, continue.
     * Otherwise, add it to the answer list.

4. Return the list of missing numbers.

---

### **Example Walkthrough 1**

Input:

```
[3, 4, 5, 6, 8]
```

Minimum = 3

Maximum = 8

Complete range:

```
3 4 5 6 7 8
```

Numbers present:

```
3 4 5 6 8
```

Missing number:

```
7
```

Output:

```
[7]
```

---

### **Example Walkthrough 2**

Input:

```
[1, 4, 2, 5]
```

Complete range:

```
1 2 3 4 5
```

Missing number:

```
3
```

Output:

```
[3]
```

---

### **Example Walkthrough 3**

Input:

```
[5, 1]
```

Complete range:

```
1 2 3 4 5
```

Missing numbers:

```
2 3 4
```

Output:

```
[2, 3, 4]
```

---

### **Example Walkthrough 4**

Input:

```
[6, 7, 8, 9]
```

Complete range:

```
6 7 8 9
```

No numbers are missing.

Output:

```
[]
```

---

### **Complexity**

**Time Complexity:** O(n + R)

* Finding the minimum and maximum takes **O(n)**.
* Creating the hash set takes **O(n)**.
* Traversing the range from minimum to maximum takes **O(R)**, where **R = max(nums) - min(nums) + 1**.

Overall:

```
O(n + R)
```

---

**Space Complexity:** O(n)

* The hash set stores all elements from the input array.

---

## 🏁 Conclusion

Using a hash set makes membership checking extremely efficient.

By scanning every value between the smallest and largest numbers, we can easily identify every missing integer while maintaining the required sorted order.

This approach is simple, efficient, and easy to understand.