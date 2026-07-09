# Valid Parentheses

## 🧩 Problem Overview

You are given a string containing only the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`.

Your task is to determine whether the string is valid.

A valid string satisfies the following conditions:

- Every opening bracket has a corresponding closing bracket of the same type.
- Brackets are closed in the correct order.
- Every closing bracket matches the most recently opened unmatched bracket.

---

## 💡 Solution: Stack with Bracket Mapping

### **Method Used**

Stack + Dictionary (Hash Map)

### **Main Idea**

A stack follows the **Last In, First Out (LIFO)** principle, making it ideal for matching nested brackets.

The algorithm keeps track of opening brackets using a stack.

- Whenever an opening bracket is encountered, it is pushed onto the stack.
- Whenever a closing bracket is encountered, it must match the most recent opening bracket stored at the top of the stack.
- If a mismatch occurs or there is no corresponding opening bracket, the string is invalid.
- After processing the entire string, the stack must be empty for the string to be valid.

---

### **Detailed Explanation**

1. Create a dictionary that maps each opening bracket to its matching closing bracket.

2. Initialize an empty stack.

3. Traverse each character in the string:

   - If it is an opening bracket, push it onto the stack.
   - Otherwise, it is a closing bracket:
     - If the stack is empty, return `False`.
     - Pop the top element from the stack.
     - Check whether the current closing bracket matches the expected closing bracket from the dictionary.
     - If it does not match, return `False`.

4. After processing all characters:

   - If the stack is not empty, some opening brackets were never closed, so return `False`.
   - Otherwise, return `True`.

---

### **Example Walkthrough**

Input: `"()[]{}"`

Step-by-step:

- Read `(` → push onto stack
- Read `)` → matches `(` → pop
- Read `[` → push onto stack
- Read `]` → matches `[` → pop
- Read `{` → push onto stack
- Read `}` → matches `{` → pop
- Stack is empty → return `True`

---

### **Another Example**

Input: `"([)]"`

Step-by-step:

- Read `(` → push
- Read `[` → push
- Read `)` → expected `]` but found `)` → mismatch
- Return `False`

---

### **Complexity**

**Time Complexity:** O(n)

- Each character is processed exactly once.

**Space Complexity:** O(n)

- In the worst case, all opening brackets are stored in the stack.

---

## 🏁 Conclusion

Using a stack is the standard and most efficient approach for validating parentheses.

The stack keeps track of unmatched opening brackets, while the dictionary allows quick verification of matching bracket pairs.

This solution is simple, efficient, and correctly handles nested as well as sequential brackets.