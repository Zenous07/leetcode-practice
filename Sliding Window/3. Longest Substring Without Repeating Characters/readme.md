# Longest Substring Without Repeating Characters

## 🧩 Problem Overview

You are given a string `s`.

Your task is to find the length of the longest substring that contains no repeating characters.

A substring is a contiguous sequence of characters, so characters cannot be skipped.

---

## 💡 Solution: Sliding Window with Hash Set

### **Method Used**

Sliding Window + Hash Set

### **Main Idea**

Maintain a sliding window that always contains unique characters.

Use a hash set to keep track of the characters currently inside the window.

As you expand the window by moving the right pointer:

* If the current character is not in the set, add it and update the maximum length.
* If the character already exists, repeatedly remove characters from the left side of the window until the duplicate is removed.
* Continue expanding the window while maintaining the uniqueness of all characters.

This ensures that every character is processed efficiently without unnecessary rechecking.

---

### **Detailed Explanation**

1. Initialize an empty hash set to store the unique characters in the current window.

2. Maintain two pointers:

   * Left pointer marks the beginning of the current window.
   * Right pointer expands the window one character at a time.

3. For each character:

   * If it is already present in the set, remove characters from the left side until the duplicate is eliminated.
   * Add the current character to the set.

4. After each expansion:

   * Calculate the current window length.
   * Update the maximum length found so far.

5. Continue until the right pointer reaches the end of the string.

6. Return the maximum length obtained.

---

### **Example Walkthrough**

Input: `"ababcbb"`

Step-by-step:

* Window = `"a"` → Length = 1
* Window = `"ab"` → Length = 2
* Next character is `"a"` (duplicate)
  * Remove `"a"` from the left
  * Window becomes `"ba"`
* Add `"b"` (duplicate again)
  * Remove `"b"` from the left
  * Window becomes `"ab"`
* Add `"c"` → Window = `"abc"` → Length = 3
* Next `"b"` is duplicate
  * Shrink the window until `"b"` is removed
* Continue until the end of the string

Maximum substring without repeating characters:

`"abc"`

Answer = **3**

---

### **Complexity**

**Time Complexity:** O(n)

* Each character is added to the set once and removed at most once.

**Space Complexity:** O(min(n, m))

* The hash set stores only the unique characters currently inside the window.
* Here, `m` is the size of the character set.

---

## 🏁 Conclusion

The Sliding Window technique efficiently maintains a substring with unique characters while scanning the string only once.

Using a hash set allows constant-time lookup, insertion, and deletion, making the overall algorithm optimal with linear time complexity.