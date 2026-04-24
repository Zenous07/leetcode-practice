# Contains Duplicate

## 🧩 Problem Overview

You are given an array of integers.

Your task is to determine whether any value appears at least twice in the array.

* Return `True` if any element appears more than once.
* Return `False` if all elements are distinct.

---

## 💡 Solution: Hash Set Lookup

### **Method Used**

Hash Set (Using Python `set`)

### **Main Idea**

A set only stores unique elements.

As you iterate through the array:

* If an element is already in the set, it means it has appeared before → duplicate found.
* If not, add the element to the set and continue.

---

### **Detailed Explanation**

1. Initialize an empty set:

   * This will store elements we've already seen.

2. Traverse the array:

   * For each element:
     * Check if it exists in the set.
     * If yes → return `True` (duplicate found).
     * If no → add it to the set.

3. If the loop finishes:

   * No duplicates were found → return `False`.

---

### **Example Walkthrough**

Input: [1, 2, 3, 4, 5]

Step-by-step:

* Add 1 → set = {1}
* Add 2 → set = {1, 2}
* Add 3 → set = {1, 2, 3}
* Add 4 → set = {1, 2, 3, 4}
* Add 5 → set = {1, 2, 3, 4, 5}

No element repeats → return False

---

### **Complexity**

Time Complexity: O(n)

* Each lookup and insertion in a set takes O(1) on average.

Space Complexity: O(n)

* In the worst case, all elements are stored in the set.

---

## 🏁 Conclusion

Using a set allows us to efficiently detect duplicates in a single pass.

This approach is simple, fast, and works well for large inputs.