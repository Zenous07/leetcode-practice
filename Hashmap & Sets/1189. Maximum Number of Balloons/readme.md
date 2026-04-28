# Max Number of Balloons

## 🧩 Problem Overview

You are given a string `text`.

Your task is to determine how many instances of the word **"balloon"** can be formed using the characters from the string.

Each character can be used only once per instance.

The goal is to return the maximum number of times the word `"balloon"` can be constructed.

---

## 💡 Solution: Frequency Counting Approach

### **Method Used**

Character Frequency Mapping

### **Main Idea**

The word `"balloon"` requires specific character frequencies:

- b → 1 time  
- a → 1 time  
- l → 2 times  
- o → 2 times  
- n → 1 time  

We count the frequency of each required character in the given string and then determine how many complete sets of `"balloon"` can be formed.

---

### **Detailed Explanation**

1. Create a reference string `"balloon"` to identify required characters.

2. Traverse the input string and count occurrences of only relevant characters (`b, a, l, o, n`).

3. Store these counts in a frequency dictionary.

4. Ensure all required characters are present:
   - If any required character is missing, return `0`.

5. Adjust counts for characters that repeat in `"balloon"`:
   - `l` must be divided by 2
   - `o` must be divided by 2

6. The final answer is the minimum value among all adjusted frequencies.

   - This ensures the limiting character determines the result.

---

### **Example Walkthrough**

Input: `"nlaebolko"`

Step-by-step:

- Count relevant characters:
  - b = 1
  - a = 1
  - l = 2
  - o = 2
  - n = 1

- Adjust for repetition:
  - l → 2 / 2 = 1
  - o → 2 / 2 = 1

- Final frequencies: [1, 1, 1, 1, 1]

Result: **1 instance of "balloon"**

---

### **Complexity**

Time Complexity: O(n)

- One pass through the string

Space Complexity: O(1)

- Fixed number of characters stored (b, a, l, o, n)

---

## 🏁 Conclusion

This approach efficiently counts character frequencies and determines the limiting factor in forming the word `"balloon"`.

By focusing only on required characters and adjusting for duplicates, we can compute the result in linear time with constant space.