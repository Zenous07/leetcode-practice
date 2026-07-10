# Majority Element

## 🧩 Problem Overview

You are given an array of integers where one element appears more than ⌊n / 2⌋ times.

Your task is to find and return that majority element.

The problem guarantees that a majority element always exists in the array.

---

## 💡 Solution: Boyer-Moore Voting Algorithm

### **Method Used**

Boyer-Moore Voting Algorithm

### **Main Idea**

The algorithm maintains a candidate for the majority element and a counter.

- If the counter becomes zero, choose the current element as the new candidate.
- If the current element matches the candidate, increase the counter.
- Otherwise, decrease the counter.

Since the majority element appears more than half the time, it cannot be completely canceled out by the other elements. Therefore, the final candidate is guaranteed to be the majority element.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the array contains only one element, return that element.

2. Initialize two variables:

   * `candidate` to store the current majority candidate.
   * `count` to keep track of its vote balance.

3. Traverse the array:

   * If `count` becomes zero, select the current element as the new candidate and set `count` to 1.
   * If the current element equals the candidate, increment `count`.
   * Otherwise, decrement `count`.

4. After processing all elements:

   * Return the final candidate, which is guaranteed to be the majority element.

---

### **Example Walkthrough**

Input: [2, 5, 5]

Step-by-step:

* Start with `count = 0`
* Choose `2` as the candidate → `candidate = 2`, `count = 1`
* Next element is `5` → different from candidate → `count = 0`
* Since `count` is now 0, choose the next element `5` as the new candidate → `candidate = 5`, `count = 1`
* End of traversal → return `5`

---

### **Complexity**

Time Complexity: O(n)

* The array is traversed only once.

Space Complexity: O(1)

* Only two variables (`candidate` and `count`) are used.

---

## 🏁 Conclusion

The Boyer-Moore Voting Algorithm is an optimal solution for finding the majority element.

It works by canceling out different elements while keeping track of a potential majority candidate. Because the majority element appears more than half the time, it always survives the cancellation process.

This approach achieves linear time complexity with constant extra space, making it the most efficient solution for this problem.