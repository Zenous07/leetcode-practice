# Concatenation of Array

## 🧩 Problem Overview

You are given an integer array `nums`.

Your task is to create a new array by concatenating `nums` with itself, meaning all elements of the original array appear twice in the same order.

The returned array should have a length of `2n`, where `n` is the length of the original array.

---

## 💡 Solution: Array Multiplication

### **Method Used**

Array Multiplication (`nums * 2`)

### **Main Idea**

Python allows a list to be repeated using the multiplication (`*`) operator.

By multiplying the list by `2`, Python creates a new list that contains two consecutive copies of the original array.

This provides a concise and efficient way to concatenate the array with itself without manually copying each element.

---

### **Detailed Explanation**

1. Create an empty result array (optional).

   * This step is not necessary when using list multiplication.

2. Multiply the original array by `2`.

   * This duplicates every element while preserving the original order.

3. Return the newly created array.

   * The returned array contains two copies of the original array placed one after another.

---

### **Example Walkthrough**

Input:

```
[1, 2, 3]
```

Step-by-step:

* Original array → `[1, 2, 3]`
* Duplicate the array using list multiplication
* Concatenate both copies

Output:

```
[1, 2, 3, 1, 2, 3]
```

---

### **Another Example**

Input:

```
[5, 8]
```

Output:

```
[5, 8, 5, 8]
```

Explanation:

* The original array is repeated once.
* The order of elements remains unchanged.

---

### **Complexity**

**Time Complexity:** O(n)

* Every element is copied exactly once into the second half of the new array.

**Space Complexity:** O(n)

* A new array of size `2n` is created to store the result.

---

## 🏁 Conclusion

Using Python's list multiplication operator is one of the simplest and most readable ways to concatenate an array with itself.

It avoids manual loops, keeps the code short, and efficiently creates the required result while preserving the order of elements.