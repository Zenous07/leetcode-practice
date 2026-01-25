# Valid Palindrome

## 🧩 Problem Overview
Given a string s, determine whether it is a palindrome after:
- Converting all uppercase letters to lowercase
- Removing all non-alphanumeric characters

A string is a palindrome if it reads the same forward and backward after cleaning.

---

## 💡 Solution: String Cleanup + Reverse Comparison

### **Method Used**
String Normalization and Reverse Check

### **Main Idea**
The idea is to normalize the string by converting it to lowercase and removing all
non-alphanumeric characters. After cleaning, the string is compared with its reverse.
If both are equal, the string is a palindrome.

---

### **Detailed Explanation**
1. Convert the string to lowercase.
2. Remove all non-alphanumeric characters using a character filter.
3. Compare the cleaned string with its reversed version.
4. If both are equal, return true; otherwise, return false.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

Where n is the length of the input string.

---

## 🏁 Conclusion
This approach is simple, readable, and effective for checking palindromes.
By leveraging Python’s built-in string handling, the solution remains clean and efficient.
