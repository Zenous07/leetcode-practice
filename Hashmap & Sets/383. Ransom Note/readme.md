# 383. Ransom Note

## 🧩 Problem Overview

You are given two strings: **ransomNote** and **magazine**.

Your task is to determine whether the ransomNote can be constructed using the characters from magazine.

Each character in magazine can only be used once.

Return `True` if it is possible to construct the ransomNote, otherwise return `False`.

---

## 💡 Solution: Frequency Counting Approach

### **Method Used**

Hash Map (Dictionary) / Character Frequency Counting

### **Main Idea**

We count how many times each character appears in the magazine, then try to "build" the ransomNote by consuming those characters.

If at any point a required character is missing or used up, we return `False`.

---

## 🧠 Detailed Explanation

### 1. Count characters in magazine
- Create a dictionary to store frequency of each character.
- Traverse the magazine string.
- For each character, increase its count in the dictionary.

---

### 2. Validate ransomNote construction
- Traverse the ransomNote string.
- For each character:
  - If it exists in the dictionary and count is greater than 0, reduce its count by 1.
  - Otherwise, return `False` immediately (character not available).

---

### 3. Final check
- If all characters in ransomNote are successfully matched, return `True`.

---

## 🧾 Example Walkthrough

### Example:
Input: ransomNote = "aa", magazine = "aab"

Step 1: Count magazine characters  
- a → 2 times  
- b → 1 time  

Step 2: Process ransomNote  
- Take 'a' → available → reduce count (a = 1)  
- Take 'a' → available → reduce count (a = 0)  

All characters matched successfully → return `True`

---

## ⚙️ Complexity Analysis

### ⏱ Time Complexity: O(n + m)
- n = length of ransomNote  
- m = length of magazine  
- We traverse both strings once

### 🧠 Space Complexity: O(1)
- At most 26 lowercase English letters stored in the dictionary

---

## 🏁 Conclusion

This approach efficiently solves the problem using frequency counting.

By tracking available characters in the magazine, we ensure each letter is used only once and validate whether the ransomNote can be formed successfully.