# Climbing Stairs

## 🧩 Problem Overview

You are climbing a staircase with `n` steps.

At every move, you can either climb **1 step** or **2 steps**.

Your task is to determine the total number of **distinct ways** to reach the top of the staircase.

---

## 💡 Solution: Recursion with Memoization (Dynamic Programming)

### **Method Used**

Recursion + Memoization (Top-Down Dynamic Programming)

### **Main Idea**

The number of ways to reach a particular step depends on the number of ways to reach the previous two steps.

This follows the recurrence relation:

- Ways(n) = Ways(n - 1) + Ways(n - 2)

Instead of solving the same subproblems repeatedly, previously computed results are stored in a dictionary (memoization). Whenever a value is needed again, it is retrieved directly from memory instead of being recalculated.

---

### **Detailed Explanation**

1. Initialize a memoization dictionary:

   * There is **1 way** to reach step 1.
   * There are **2 ways** to reach step 2.

2. Create a recursive function to calculate the number of ways for any step.

3. Before computing a value:

   * Check whether it already exists in the memoization dictionary.
   * If it does, return the stored value immediately.

4. Otherwise:

   * Compute the answer using the previous two steps.
   * Store the computed result in the dictionary.
   * Return the stored value.

5. The final answer is the number of ways to reach step `n`.

---

### **Example Walkthrough**

Input: `n = 7`

Step-by-step:

* Ways(1) = 1
* Ways(2) = 2
* Ways(3) = 3
* Ways(4) = 5
* Ways(5) = 8
* Ways(6) = 13
* Ways(7) = 21

Output: `21`

---

### **Complexity**

Time Complexity: **O(n)**

* Each step is computed only once because of memoization.

Space Complexity: **O(n)**

* The memoization dictionary stores one result for each step.
* The recursive call stack can also grow up to `n`.

---

## 🏁 Conclusion

Using recursion with memoization eliminates repeated calculations by storing previously computed results.

This transforms an exponential recursive solution into a much more efficient linear-time solution while keeping the implementation simple and easy to understand.