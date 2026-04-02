# 58. Length of Last Word

## 🧩 Problem Overview
Given a string `s` consisting of words and spaces, return the length of the last word in the string.  

A word is a maximal substring consisting of non-space characters only.

---

## 💡 Solution: Reverse Traversal (Count Last Word)

### **Method Used**
Reverse Traversal Algorithm

### **Main Idea**
Start from the end of the string and skip any trailing spaces.  
Count the number of consecutive non-space characters until the beginning of the last word or the start of the string is reached.  
This gives the length of the last word directly without extra space.

---

### **Detailed Explanation**
1. Initialize:
   - `count` as 0 to track the length of the last word.
   - `l` as the index of the last character in the string.
2. Skip trailing spaces:
   - Move `l` backward while `s[l]` is a space `' '`.
3. Count the last word length:
   - While `l >= 0` and `s[l]` is not a space, increment `count` and move `l` backward.
4. Return `count`.

This method ensures we only traverse the string once from the end and avoid extra memory usage.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(1)  

Where n is the length of the string.

---

## 🏁 Conclusion
Reverse traversal provides a simple and efficient way to determine the length of the last word.  
It handles trailing spaces naturally and works in linear time with constant space.