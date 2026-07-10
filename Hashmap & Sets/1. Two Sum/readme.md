# Two Sum

## 🧩 Problem Overview

You are given an array of integers `nums` and an integer `target`.

Your task is to find the indices of the two numbers whose sum equals the target.

You may assume that:

- Exactly one valid solution exists.
- The same element cannot be used twice.
- The answer can be returned in any order.

---

## 💡 Solution: Hash Map (Dictionary)

### **Method Used**

Hash Map (Dictionary) for Constant-Time Lookup

### **Main Idea**

As we traverse the array, we store each number along with its index in a dictionary.

For every current element:

- Compute the value needed to reach the target (called the complement).
- Check whether this complement has already been seen.
- If it exists, return the stored index and the current index.
- Otherwise, store the current number and continue.

This avoids checking every possible pair and makes the solution much faster than the brute-force approach.

---

### **Detailed Explanation**

1. Create an empty dictionary.

   - It will store each number as the key and its index as the value.

2. Traverse the array from left to right.

3. For each element:

   - Calculate the complement using:

     `complement = target - current_number`

4. Check whether the complement already exists in the dictionary.

   - If it exists, return the stored index and the current index.
   - Otherwise, store the current number with its index.

5. Since the problem guarantees exactly one solution, the correct pair will always be found during traversal.

---

### **Example Walkthrough**

Input:

nums = [2, 7, 11, 15]

target = 9

Step-by-step:

- Index 0 → Number = 2
  - Complement = 7
  - Not found
  - Store {2: 0}

- Index 1 → Number = 7
  - Complement = 2
  - Found in dictionary at index 0
  - Return [0, 1]

---

### **Complexity**

Time Complexity: **O(n)**

- Each element is visited only once.
- Dictionary lookup takes O(1) on average.

Space Complexity: **O(n)**

- The dictionary may store up to all elements in the array.

---

## 🏁 Conclusion

Using a hash map allows us to find the required pair in a single pass through the array.

Instead of comparing every pair of numbers, we use constant-time lookups to efficiently locate the complement of each element.

This approach is optimal, easy to implement, and achieves linear time complexity.