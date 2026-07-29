# Fibonacci Number

## 🧩 Problem Overview

The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers.

It starts with:

* F(0) = 0
* F(1) = 1

For every value greater than 1:

* F(n) = F(n - 1) + F(n - 2)

The goal is to calculate the nth Fibonacci number efficiently.

---

## 💡 Solution: Dynamic Programming (Bottom-Up)

### **Method Used**

Dynamic Programming using an array (Tabulation)

### **Main Idea**

Instead of repeatedly calculating the same Fibonacci numbers through recursion, we build the sequence from the beginning.

We start with the known base values:

* F(0) = 0
* F(1) = 1

Then, for every index from 2 to n, we calculate the current Fibonacci number using the previous two values.

Each Fibonacci number is computed only once, making the solution efficient.

---

### **Detailed Explanation**

1. Handle the base cases:

   * If `n = 0`, return `0`.
   * If `n = 1` or `n = 2`, return `1`.

2. Create an array to store Fibonacci numbers:

   * The array stores values from `F(0)` to `F(n)`.

3. Initialize the first two Fibonacci numbers:

   * `F(0) = 0`
   * `F(1) = 1`

4. Build the sequence iteratively:

   * For every index from `2` to `n`,
     compute:

     `F(i) = F(i-1) + F(i-2)`

5. Return the value stored at index `n`.

---

### **Example Walkthrough**

Input:

`n = 7`

Build the sequence step by step:

* F(0) = 0
* F(1) = 1
* F(2) = 1
* F(3) = 2
* F(4) = 3
* F(5) = 5
* F(6) = 8
* F(7) = 13

Answer:

`13`

---

### **Complexity**

**Time Complexity:** O(n)

* Each Fibonacci number is calculated exactly once.

**Space Complexity:** O(n)

* An array of size `n + 1` is used to store the Fibonacci numbers.

---

## 🏁 Conclusion

Using Dynamic Programming (Tabulation) eliminates repeated calculations and builds the Fibonacci sequence from the smallest values up to the required value.

This approach is straightforward, efficient, and much faster than the recursive solution for larger values of `n`.