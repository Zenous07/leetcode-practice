# 13. Roman to Integer

## 🧩 Problem Overview

Roman numerals are represented using seven symbols: I, V, X, L, C, D, and M.

Each symbol has a fixed value, and numbers are formed by combining these symbols from left to right, usually from largest to smallest.

However, in certain cases, a smaller value placed before a larger value indicates subtraction instead of addition.

Your task is to convert a given Roman numeral string into its corresponding integer value.

---

## 💡 Solution: Greedy Traversal with Symbol Mapping

### **Method Used**

Greedy approach using a hash map (symbol-to-value mapping)

### **Main Idea**

We scan the Roman numeral from left to right and decide whether to add or subtract each symbol based on its value compared to the next symbol.

- If the current symbol is smaller than the next symbol, it should be subtracted.
- Otherwise, it should be added.

This handles both normal addition cases and special subtraction cases like IV, IX, XL, XC, CD, and CM.

---

## 🔍 Detailed Explanation

1. Create a mapping of Roman symbols to their integer values:
   Each symbol (I, V, X, L, C, D, M) is assigned its corresponding numeric value.

2. Traverse the string from left to right:
   For each character, compare its value with the next character (if it exists).

3. Apply decision rule:
   - If the current value is less than the next value → subtract it.
   - Otherwise → add it.

4. Accumulate the result:
   Maintain a running total while processing each symbol.

5. Final result:
   After processing all characters, the total gives the integer equivalent.

---

## 🧪 Example Walkthrough

### Example: "MCMXCIV"

Step-by-step breakdown:

- M = 1000 → add
- CM = 900 → C (100) is before M (1000), so subtract C and add M
- XC = 90 → X (10) before C (100), so subtract X and add C
- IV = 4 → I (1) before V (5), so subtract I and add V

Final result: 1994

---

## 📊 Complexity

Time Complexity: O(n)

- We traverse the string once.

Space Complexity: O(1)

- Only a fixed-size mapping is used.

---

## 🏁 Conclusion

This problem is efficiently solved using a single pass greedy approach.

By comparing each symbol with the next one, we can easily handle both addition and subtraction cases in Roman numerals without complex logic.

This makes the solution simple, fast, and optimal.