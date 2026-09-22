# Guess Number Higher or Lower

## 🧩 Problem Overview

You are given a number `n`, and a hidden number called `pick` is chosen between `1` and `n`.

Your task is to find the hidden number by repeatedly making guesses.

For every guess, the `guess()` API tells you whether your guess is:

* Higher than the picked number → `-1`
* Lower than the picked number → `1`
* Equal to the picked number → `0`

The goal is to return the picked number while minimizing the number of guesses.

---

## 💡 Solution: Binary Search

### **Method Used**

Binary Search

### **Main Idea**

The possible answer lies within a range from `1` to `n`.

Instead of checking every number one by one, we check the middle number of the current range.

Based on the result of the `guess()` API:

* If the guess is correct (`0`), return the current number.
* If the guess is too high (`-1`), search the left half.
* If the guess is too low (`1`), search the right half.

This repeatedly cuts the search space approximately in half.

---

### **Detailed Explanation**

1. Initialize the search range:

   * `l = 1`
   * `n` represents the upper boundary.

2. Find the middle of the current range:

   * The middle value is calculated using integer division.
   * This gives the number that will be tested.

3. Call the `guess()` API:

   * If it returns `0`, the current number is the answer.
   * If it returns `-1`, the current guess is greater than the picked number.

4. When the guess is too high:

   * The picked number must be smaller than the current guess.
   * Therefore, move the upper boundary to `curr - 1`.

5. When the guess is too low:

   * The picked number must be greater than the current guess.
   * Therefore, move the lower boundary to `curr + 1`.

6. Calculate the new middle value:

   * After updating the boundaries, calculate the middle again.
   * Continue until the correct number is found.

---

### **Example Walkthrough**

Input:

`n = 10`

Suppose:

`pick = 6`

Initial range:

`1 → 10`

Middle:

`5`

The API returns `1`, meaning the picked number is higher than `5`.

New range:

`6 → 10`

Middle:

`8`

The API returns `-1`, meaning the picked number is lower than `8`.

New range:

`6 → 7`

Middle:

`6`

The API returns `0`.

Therefore:

`6` is the answer.

---

### **Why Binary Search Works**

At every step, the `guess()` API tells us which side of the current guess contains the answer.

For example:

`1 2 3 4 5 6 7 8 9 10`

If we guess `5` and the answer is higher:

`1 2 3 4 5 | 6 7 8 9 10`

There is no need to search `1` through `5` anymore.

We only search:

`6 7 8 9 10`

The search space keeps getting smaller until only the correct number remains.

---

### **Important Boundary Detail**

When the current guess is known to be incorrect, it should be removed from the search range.

If the guess is too high:

`upper = curr - 1`

If the guess is too low:

`lower = curr + 1`

The `+1` and `-1` are important because `curr` has already been tested.

---

### **Complexity**

Time Complexity: O(log n)

* Each guess eliminates approximately half of the remaining possibilities.
* Therefore, at most O(log n) guesses are needed.

Space Complexity: O(1)

* Only a few variables are used.
* No additional data structures are required.

---

## 🏁 Conclusion

Binary search is ideal for this problem because every response from the `guess()` API tells us which half of the search range can be discarded.

By repeatedly checking the middle value and adjusting the boundaries, the picked number can be found in O(log n) time using O(1) extra space.