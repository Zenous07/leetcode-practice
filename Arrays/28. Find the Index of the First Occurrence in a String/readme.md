# Find First Index of a Substring

## 🧩 Problem Overview

You are given two strings:

- **haystack** → the main string
- **needle** → the substring to search for

Your task is to return the index of the **first occurrence** of `needle` inside `haystack`.

If `needle` is not found, return **-1**.

---

## 💡 Solution: Brute Force String Matching

### **Method Used**

Nested Loop (Character-by-Character Comparison)

### **Main Idea**

The algorithm checks every possible starting position in the `haystack`.

Whenever the first character matches the first character of `needle`, it begins comparing the remaining characters one by one.

If every character matches consecutively, the current index is returned as the first occurrence.

If a mismatch occurs, it continues checking from the next position in the `haystack`.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the length of `needle` is greater than the length of `haystack`, return `-1`.

2. Traverse the `haystack`:

   * Check each character as a possible starting position.

3. Look for the first character match:

   * If the current character matches the first character of `needle`, begin checking the remaining characters.

4. Compare characters one by one:

   * Continue matching each character of `needle` with the corresponding character in `haystack`.
   * If all characters match successfully, return the current starting index.

5. Handle mismatches:

   * If any character does not match, stop checking that position and continue with the next index.

6. If no complete match is found:

   * Return `-1`.

---

### **Example Walkthrough**

Input:

haystack = "leetcode"

needle = "leeto"

Step-by-step:

* Start at index 0.
* Compare:
  * l = l ✔
  * e = e ✔
  * e = e ✔
  * t = t ✔
  * c ≠ o ✘
* Match fails.
* Continue checking the remaining positions.
* No complete match is found.
* Return `-1`.

---

### **Complexity**

Time Complexity: **O(n × m)**

* `n` = length of `haystack`
* `m` = length of `needle`
* In the worst case, every position in `haystack` is checked against every character in `needle`.

Space Complexity: **O(1)**

* Only a few variables are used.
* No additional data structures are required.

---

## 🏁 Conclusion

This brute force approach searches every possible starting position in the `haystack` and compares characters one by one until either a complete match is found or all possibilities are exhausted.

Although it is not the most optimized solution, it is straightforward, easy to understand, and works well for typical string matching problems.