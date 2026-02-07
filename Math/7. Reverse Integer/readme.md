# Reverse Integer

## 🧩 Problem Overview
Given a signed 32-bit integer `x`, reverse its digits.

If reversing `x` causes the value to go outside the signed 32-bit integer range  
`[-2³¹, 2³¹ - 1]`, return `0`.

The solution must not use 64-bit integers.

---

## 💡 Solution Approach

### **Method Used**
Digit Extraction with Sign Handling

### **Main Idea**
The integer is reversed digit by digit using modulo and division operations.
The sign of the number is handled separately to simplify the logic.
After reversing, the result is checked to ensure it stays within the 32-bit integer range.

---

## 🪜 Step-by-Step Explanation
1. Determine the sign of the number (`positive` or `negative`).
2. Convert the number to a positive value for easy digit extraction.
3. Initialize a variable to store the reversed number.
4. While the number is not zero:
   - Extract the last digit using modulo (`% 10`).
   - Append it to the reversed number.
   - Remove the last digit using integer division.
5. Restore the original sign.
6. Check if the reversed number lies within the 32-bit integer range.
7. Return the reversed number or `0` if it overflows.

---

## ⏱️ Complexity Analysis
**Time Complexity:** O(n)  
(where `n` is the number of digits in the integer)

**Space Complexity:** O(1)

---

## 🏁 Conclusion
This approach efficiently reverses an integer without using extra memory
and safely handles overflow conditions as required by the problem constraints.
It is optimal and suitable for all valid inputs within the given range.