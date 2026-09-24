# Smallest Index With Digit Sum Equal to Index

## 🧩 Problem Overview

You are given an array of integers.

For each element in the array:

* Calculate the sum of all its digits.
* Compare the digit sum with the element's index.
* Return the first index where the digit sum is equal to the index.

If no such index exists, return `-1`.

---

## 💡 Solution: Digit Sum Calculation

### **Method Used**

Iteration + Digit Sum Calculation

### **Main Idea**

Traverse the array from left to right.

For every element:

1. Calculate the sum of its digits.
2. Compare the digit sum with its current index.
3. If both are equal, return the index immediately.
4. If no index satisfies the condition, return `-1`.

The digit sum can be calculated by repeatedly extracting the last digit using the modulo operator `% 10`.

---

### **Detailed Explanation**

1. Iterate through every index of the array:

   * Use the index `i` to keep track of the current position.

2. Calculate the digit sum:

   * Take the last digit using `% 10`.
   * Add the digit to a temporary sum.
   * Remove the last digit using integer division `// 10`.
   * Continue until there are no digits left.

3. Compare the digit sum with the index:

   * If `digit_sum == i`, the required condition is satisfied.
   * Return `i` immediately because we need the smallest index.

4. If the entire array is checked:

   * No valid index was found.
   * Return `-1`.

---

### **Example Walkthrough**

Input:

`[1, 3, 2, 10, 5]`

Step-by-step:

* Index `0`, value `1`
  * Digit sum = `1`
  * `1 != 0`

* Index `1`, value `3`
  * Digit sum = `3`
  * `3 != 1`

* Index `2`, value `2`
  * Digit sum = `2`
  * `2 == 2`

The condition is satisfied at index `2`.

Output:

`2`

---

### **Another Example**

Input:

`[5, 11, 20, 30]`

Step-by-step:

* Index `0`, value `5`
  * Digit sum = `5`
  * `5 != 0`

* Index `1`, value `11`
  * Digit sum = `1 + 1 = 2`
  * `2 != 1`

* Index `2`, value `20`
  * Digit sum = `2 + 0 = 2`
  * `2 == 2`

Therefore, the answer is:

`2`

---

### **Example Where No Index Exists**

Input:

`[10, 20, 30]`

Digit sums:

* Index `0` → `10` → digit sum `1`
* Index `1` → `20` → digit sum `2`
* Index `2` → `30` → digit sum `3`

None of the digit sums match their corresponding indices.

Output:

`-1`

---

### **Important Operators**

The solution uses two important operators for calculating the digit sum.

#### `% 10`

Gets the last digit of a number.

Example:

`123 % 10 = 3`

#### `// 10`

Removes the last digit from a number.

Example:

`123 // 10 = 12`

So for `123`:

* `123 % 10` → `3`
* `123 // 10` → `12`
* `12 % 10` → `2`
* `12 // 10` → `1`
* `1 % 10` → `1`
* `1 // 10` → `0`

Digit sum:

`3 + 2 + 1 = 6`

---

### **Complexity**

Time Complexity: O(n × d)

* `n` is the number of elements in the array.
* `d` is the number of digits in each number.
* Each number is processed digit by digit.

For typical integer values, this is effectively close to O(n).

Space Complexity: O(1)

* Only a few temporary variables are used.
* No additional data structures are required.

---

## 🏁 Conclusion

The solution checks every index from left to right and calculates the digit sum of the corresponding number.

As soon as the digit sum matches the index, that index is returned.

Returning immediately ensures that the **smallest valid index** is found.

If no index satisfies the condition, the solution returns `-1`.