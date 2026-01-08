# Is Subsequence

## 🧩 Problem Overview
Given two strings s and t, determine whether s is a subsequence of t.

A subsequence is formed by deleting some (or none) characters from the original string
without changing the relative order of the remaining characters.

Return true if s is a subsequence of t, otherwise return false.

---

## 💡 Solution: Two-Pointer Greedy Method

### **Method Used**
Two-Pointer Technique (Greedy)

### **Main Idea**
This approach uses two pointers to traverse both strings.
One pointer moves through string t, while the other tracks matching characters in string s.
If all characters of s are found in order within t, then s is a subsequence of t.

---

### **Detailed Explanation**
1. Initialize two pointers:
   - `l` for traversing string `t`
   - `r` for traversing string `s`
2. While both pointers are within their respective string lengths:
   - If `t[l]` matches `s[r]`, move both pointers forward.
   - Otherwise, move only the pointer of `t`.
3. After the loop:
   - If `r` has reached the length of `s`, all characters were matched in order.
4. Return `true` if all characters matched, otherwise return `false`.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(1)

Where n is the length of string `t`.

---

## 🏁 Conclusion
The Two-Pointer Greedy approach efficiently checks whether one string is a subsequence of another.
It runs in linear time, uses constant space, and is the most optimal solution for this problem.
