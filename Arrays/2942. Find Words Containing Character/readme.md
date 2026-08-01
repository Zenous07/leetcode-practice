# Find Words Containing Character

## 🧩 Problem Overview

You are given a list of strings `words` and a character `x`.

Your task is to return a list containing the indices of all words that contain the character `x`.

If no word contains the given character, return an empty list.

---

## 💡 Solution: Set Membership Check

### **Method Used**

Set + Linear Traversal

### **Main Idea**

Traverse each word one by one.

For every word:

* Convert the word into a set of unique characters.
* Check whether the character `x` exists in the set.
* If it exists, add the current index to the result list.

After checking every word, return the list of collected indices.

---

### **Detailed Explanation**

1. Create an empty list to store the answer.

2. Traverse the list of words using their indices.

3. For every word:

   * Convert the word into a set.
   * This stores only the unique characters of the word.
   * Check whether `x` is present in the set.

4. If the character is found:

   * Append the current index to the result list.

5. Continue until all words have been checked.

6. Return the final list of indices.

---

### **Example Walkthrough**

Input:

```text
words = ["leet", "code"]
x = "e"
```

Step-by-step:

* Index 0 → "leet"
  * Unique characters = {l, e, t}
  * 'e' exists → add 0

* Index 1 → "code"
  * Unique characters = {c, o, d, e}
  * 'e' exists → add 1

Result:

```text
[0, 1]
```

---

### **Another Example**

Input:

```text
words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
```

Processing:

* "abc" → contains 'a' → add 0
* "bcd" → does not contain 'a'
* "aaaa" → contains 'a' → add 2
* "cbc" → does not contain 'a'

Result:

```text
[0, 2]
```

---

### **Example with No Match**

Input:

```text
words = ["abc", "bcd", "aaaa", "cbc"]
x = "z"
```

None of the words contain `'z'`.

Result:

```text
[]
```

---

### **Why Use a Set?**

A set provides fast membership checking.

Instead of scanning every character repeatedly, converting the word into a set allows checking whether `x` exists efficiently.

Although creating the set takes time proportional to the length of the word, membership testing itself is very fast.

---

### **Complexity**

**Time Complexity:** O(n × m)

* `n` = number of words
* `m` = average length of each word
* Creating a set for every word takes O(m)

**Space Complexity:** O(m)

* A temporary set is created for each word.
* The result list stores only the matching indices.

---

## 🏁 Conclusion

The solution checks every word exactly once.

By converting each word into a set, checking whether the required character exists becomes simple and efficient.

This approach is clean, easy to understand, and works well within the given constraints.