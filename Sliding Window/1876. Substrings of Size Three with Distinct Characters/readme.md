# Substrings of Size Three with Distinct Characters

## 🧩 Problem Overview

You are given a string `s`.

A substring is considered **good** if it has exactly **three characters** and all three characters are **distinct** (no repeated characters).

Your task is to count how many such good substrings exist in the given string.

If the same substring appears multiple times at different positions, each occurrence should be counted separately.

---

## 💡 Solution: Sliding Window with a Set

### **Method Used**

Sliding Window + Hash Set

### **Main Idea**

Maintain a sliding window containing unique characters using a hash set.

As you move through the string:

* Expand the window by adding new characters.
* If a duplicate character is encountered, shrink the window from the left until the duplicate is removed.
* Whenever the window contains exactly three distinct characters, increment the count.
* Continue sliding the window until the end of the string.

This ensures every valid substring of length three with distinct characters is counted efficiently.

---

### **Detailed Explanation**

1. Handle the edge case:

   * If the string length is less than 3, no valid substring can exist, so return `0`.

2. Initialize:

   * A set to store the current unique characters.
   * Two pointers (`left` and `right`) representing the sliding window.
   * A counter to store the number of good substrings.

3. Traverse the string using the right pointer:

   * If the current character is not already in the set:
     * Add it to the set.
     * If the window now contains exactly three distinct characters, increment the counter.

4. If the current character is already present:

   * Continuously remove characters from the left side of the window until the duplicate is removed.
   * Add the current character back into the set.
   * If the window again contains exactly three distinct characters, increment the counter.

5. Continue until all characters have been processed.

6. Return the final count.

---

### **Example Walkthrough**

Input:

```
"aababcabc"
```

Window progression:

* `"a"` → less than 3 characters
* `"aa"` → duplicate found
* `"ab"` → two distinct characters
* `"aba"` → duplicate present
* `"abc"` → valid → count = 1
* `"bca"` → valid → count = 2
* `"cab"` → valid → count = 3
* `"abc"` → valid → count = 4

Final Answer:

```
4
```

---

### **Complexity**

**Time Complexity:** O(n)

* Each character is added to and removed from the sliding window at most once.

**Space Complexity:** O(1)

* The set stores at most three distinct lowercase characters at any time.

---

## 🏁 Conclusion

Using a sliding window with a hash set allows us to efficiently maintain a window of unique characters.

By expanding and shrinking the window as needed, every good substring of length three is counted in linear time while using constant extra space.