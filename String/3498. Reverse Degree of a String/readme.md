# Reverse Degree of a String

## 🧩 Problem Overview

You are given a lowercase English string `s`.

For every character in the string:

- Find its position in the **reversed alphabet**:
  - `'a' = 26`
  - `'b' = 25`
  - ...
  - `'z' = 1`
- Multiply this value by the character's **1-indexed position** in the string.
- Add the result for every character.

Return the final sum, known as the **reverse degree** of the string.

---

## 💡 Solution: Reverse Alphabet Mapping

### **Method Used**

Reverse Alphabet Value Mapping + Single Traversal

### **Main Idea**

Every lowercase letter has a fixed value based on its position in the reversed alphabet.

Instead of calculating this value repeatedly, create a mapping for all lowercase letters.

Then:

- Traverse the string from left to right.
- For each character:
  - Look up its reversed alphabet value.
  - Multiply it by its position in the string (starting from 1).
  - Add the result to the running total.
- Return the accumulated sum.

---

### **Detailed Explanation**

1. Create a mapping for every lowercase letter.

   - `'a'` maps to `26`
   - `'b'` maps to `25`
   - ...
   - `'z'` maps to `1`

2. Initialize a variable to store the answer.

3. Traverse the string one character at a time.

4. For each character:

   - Find its reversed alphabet value.
   - Multiply it by its 1-indexed position.
   - Add the product to the total.

5. After processing every character, return the total reverse degree.

---

### **Example Walkthrough 1**

Input:

```
s = "abc"
```

Calculation:

| Character | Reverse Value | Position | Product |
|-----------|--------------:|---------:|--------:|
| a | 26 | 1 | 26 |
| b | 25 | 2 | 50 |
| c | 24 | 3 | 72 |

Total:

```
26 + 50 + 72 = 148
```

Output:

```
148
```

---

### **Example Walkthrough 2**

Input:

```
s = "zaza"
```

Calculation:

| Character | Reverse Value | Position | Product |
|-----------|--------------:|---------:|--------:|
| z | 1 | 1 | 1 |
| a | 26 | 2 | 52 |
| z | 1 | 3 | 3 |
| a | 26 | 4 | 104 |

Total:

```
1 + 52 + 3 + 104 = 160
```

Output:

```
160
```

---

### **Example Walkthrough 3**

Input:

```
s = "leetcode"
```

Calculation:

| Character | Reverse Value | Position | Product |
|-----------|--------------:|---------:|--------:|
| l | 15 | 1 | 15 |
| e | 22 | 2 | 44 |
| e | 22 | 3 | 66 |
| t | 7 | 4 | 28 |
| c | 24 | 5 | 120 |
| o | 12 | 6 | 72 |
| d | 23 | 7 | 161 |
| e | 22 | 8 | 176 |

Total:

```
15 + 44 + 66 + 28 + 120 + 72 + 161 + 176 = 682
```

Output:

```
682
```

---

### **Complexity**

**Time Complexity:** `O(n)`

- The string is traversed exactly once.

**Space Complexity:** `O(1)`

- The reverse alphabet mapping has a fixed size (26 letters), so it uses constant extra space.

---

## 🏁 Conclusion

This approach computes the reverse degree efficiently by using a predefined reverse alphabet mapping and a single pass through the string.

Since each character is processed exactly once, the algorithm runs in linear time while using only constant extra space, making it an efficient and straightforward solution.