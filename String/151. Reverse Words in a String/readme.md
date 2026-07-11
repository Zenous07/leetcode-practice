# Reverse Words in a String

## 🧩 Problem Overview

You are given a string that may contain leading spaces, trailing spaces, or multiple spaces between words.

Your task is to reverse the order of the words and return them as a single string.

The final string should contain only one separator between consecutive words.

---

## 💡 Solution: Split, Reverse, and Join

### **Method Used**

Split + Reverse + Join

### **Main Idea**

The solution first separates the string into individual words, automatically removing extra spaces.

Then, it reverses the list of words.

Finally, it combines the reversed words into a single string using a separator.

---

### **Detailed Explanation**

1. Split the string into words:

   * The split operation separates the string into individual words.
   * It automatically ignores leading, trailing, and multiple spaces.

2. Reverse the list of words:

   * Reverse the order of all extracted words.

3. Join the reversed words:

   * Combine the reversed words into a single string using the desired separator.

4. Return the final string.

---

### **Example Walkthrough**

Input:

```
"  hello   world  "
```

After splitting:

```
["hello", "world"]
```

After reversing:

```
["world", "hello"]
```

After joining:

```
"world*hello"
```

---

### **Complexity**

Time Complexity: O(n)

* Splitting processes each character once.
* Reversing the list takes linear time.
* Joining the words also takes linear time.

Overall Time Complexity: **O(n)**

Space Complexity: O(n)

* Extra space is required to store the list of words.

---

## 🏁 Conclusion

By splitting the string into words, reversing their order, and joining them back together, the solution efficiently reverses the words while automatically handling extra spaces.

This approach is simple, readable, and runs in linear time.