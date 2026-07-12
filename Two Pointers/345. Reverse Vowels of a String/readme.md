# Reverse Vowels of a String

## 🧩 Problem Overview
Given a string `s`, reverse only the vowels while keeping all consonants and other characters in their original positions.

The vowels are `a`, `e`, `i`, `o`, and `u` in both lowercase and uppercase.

---

## 💡 Solution 1: Two-Pointer Method (Optimized)

### **Method Used**
Two Pointers

### **Main Idea**
Use two pointers, one starting from the beginning and the other from the end of the string. Move both pointers toward each other until they point to vowels, then swap those vowels and continue. This reverses the vowels in a single traversal without using extra storage for vowels.

---

### **Detailed Explanation**
1. Convert the string into a list since strings are immutable.
2. Initialize two pointers:
   - `l` at the beginning.
   - `r` at the end.
3. Move `l` forward until it points to a vowel.
4. Move `r` backward until it points to a vowel.
5. Swap the vowels at `l` and `r`.
6. Move both pointers inward and repeat until they meet or cross.
7. Convert the list back into a string and return it.

---

### **Complexity**
Time Complexity: **O(n)**  
Space Complexity: **O(n)** (because the string is converted into a list)

---

## ⚙️ Solution 2: Brute Force Vowel Collection Method

### **Method Used**
Extra Storage with Reverse Replacement

### **Main Idea**
First collect all the vowels in their original order. Then traverse the string again and replace each vowel with the last collected vowel, effectively reversing their order.

---

### **Detailed Explanation**
1. Convert the string into a list.
2. Traverse the string and store every vowel in a separate list.
3. Traverse the string again.
4. Whenever a vowel is found:
   - Remove the last vowel from the stored list.
   - Replace the current vowel with it.
5. Convert the modified list back into a string and return it.

---

### **Complexity**
Time Complexity: **O(n)**  
Space Complexity: **O(n)**

---

## 🆚 Comparison Summary

| Aspect | Two-Pointer Method | Brute Force Collection Method |
|--------|---------------------|-------------------------------|
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(n) | O(n) |
| Extra Storage | No separate vowel list | Uses an additional vowel list |
| Performance | Faster and more memory efficient | Slightly less efficient |
| Recommended | Yes | Good for understanding |

---

## 🏁 Conclusion
The Two-Pointer Method is the preferred solution because it reverses vowels in a single pass without requiring an additional list to store vowels. Although both approaches have linear time complexity, the two-pointer technique uses less auxiliary memory and is cleaner for this problem.