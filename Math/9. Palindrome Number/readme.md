# Palindrome Number

## 🧩 Problem Overview
Given an integer `x`, determine whether it is a palindrome.
An integer is a palindrome if it reads the same forward and backward.

Negative numbers are **not** palindromes.

---

## 💡 Solution: String Reversal Method

### **Method Used**
String Conversion + Two-Way Comparison

### **Main Idea**
The idea is simple:
- Negative numbers are immediately rejected.
- Convert the number into a string.
- Check whether the string is equal to its reverse.

If both match, the number is a palindrome.

---

### **Detailed Explanation**
1. Check if the number is negative:
   - If yes, return `False` because negative numbers cannot be palindromes.
2. Convert the integer to a string.
3. Reverse the string using slicing.
4. Compare the original string with the reversed string.
5. If they are equal, return `True`; otherwise, return `False`.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)  

Where `n` is the number of digits in the integer.

---

## 🏁 Conclusion
This approach is easy to implement and very readable.
Although it uses extra space due to string conversion, it works efficiently
within the given constraints and is ideal for clarity and simplicity.

> Note: The follow-up can be solved without converting to a string using
mathematical digit reversal, but this solution prioritizes simplicity.
