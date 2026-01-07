# Merge Strings Alternately

## 🧩 Problem Overview
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If one string is longer than the other, append the remaining letters to the end of the merged string.

Return the merged string.

---

## 💡 Solution 1: Two-Pointer with List Append Method

### **Method Used**
Two-Pointer Technique with List Accumulation

### **Main Idea**
This approach iterates over both strings simultaneously up to the length of the shorter string.
Characters are appended alternately to a list, which is later joined into a final string.
Any remaining characters from the longer string are appended at the end.

---

### **Detailed Explanation**
1. Find the minimum length of the two strings.
2. Iterate from index `0` to `min_len - 1`:
   - Append `word1[i]` and `word2[i]` alternately to a list.
3. Append the remaining substring of `word1` (if any).
4. Append the remaining substring of `word2` (if any).
5. Join the list into a single string and return it.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

---

## ⚙️ Solution 2: Conditional Loop & String Concatenation Method

### **Method Used**
Conditional Iteration with String Concatenation

### **Main Idea**
This approach compares the lengths of the two strings and iterates based on the shorter one.
Characters are concatenated alternately using string addition.
After the loop, remaining characters from the longer string are appended.

---

### **Detailed Explanation**
1. Store the lengths of `word1` and `word2`.
2. Compare the lengths:
   - If `word1` is longer, iterate up to `len(word2)`.
   - If `word2` is longer, iterate up to `len(word1)`.
   - If both are equal, iterate through all characters.
3. During iteration:
   - Append one character from each string alternately.
4. Append the remaining part of the longer string.
5. Return the merged string.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

---

## 🆚 Comparison Summary

| Aspect | Solution 1 | Solution 2 |
|------|-----------|-----------|
| Method Used | Two-Pointer + List | Conditional Loop |
| String Building | List + join | String concatenation |
| Readability | High | Moderate |
| Performance | Faster | Slightly slower |
| Recommended | Yes | Acceptable |

---

## 🏁 Conclusion
Both solutions correctly merge the strings alternately.

The **Two-Pointer with List Append Method** is preferred because it is more readable, efficient, and avoids repeated string concatenation overhead in Python.
