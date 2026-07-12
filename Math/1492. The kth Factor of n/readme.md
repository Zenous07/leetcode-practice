# The kth Factor of n

## 🧩 Problem Overview

You are given two positive integers `n` and `k`.

A factor of an integer `n` is any integer `i` such that `n % i == 0`.

Your task is to return the `k`th factor of `n` when all factors are arranged in ascending order.

If `n` has fewer than `k` factors, return `-1`.

---

## 💡 Solution: Brute Force Factor Collection

### **Method Used**

Linear Iteration + Factor List

### **Main Idea**

Iterate through every integer from `1` to `n`.

Whenever a number divides `n` without leaving a remainder, it is a factor, so store it.

After collecting all factors:

* If there are fewer than `k` factors, return `-1`.
* Otherwise, return the factor at the `(k-1)`th index since lists are zero-indexed.

---

### **Detailed Explanation**

1. Create an empty list to store the factors.

2. Iterate from `1` to `n` (inclusive).

   * For every number `i`, check whether `n % i == 0`.
   * If true, add `i` to the list of factors.

3. After the loop finishes:

   * If the total number of factors is less than `k`, return `-1`.

4. Otherwise:

   * Return the factor at index `k - 1`.

---

### **Example Walkthrough**

Input:

`n = 12`, `k = 3`

Step-by-step:

* Check 1 → factor → store
* Check 2 → factor → store
* Check 3 → factor → store
* Check 4 → factor → store
* Check 5 → not a factor
* Check 6 → factor → store
* Check 7–11 → not factors
* Check 12 → factor → store

Factor list:

`[1, 2, 3, 4, 6, 12]`

The 3rd factor is `3`.

Return `3`.

---

### **Complexity**

**Time Complexity:** `O(n)`

* We iterate through every number from `1` to `n`.

**Space Complexity:** `O(f)`

* Where `f` is the number of factors of `n`, since all factors are stored in a list.

---

## 🏁 Conclusion

This approach checks every possible divisor of `n` and stores all valid factors in ascending order.

It is straightforward, easy to understand, and works efficiently within the given constraint (`n ≤ 1000`).