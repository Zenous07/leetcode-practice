# Add Digits

## 🧩 Problem Overview
Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

---

## 💡 Solution 1: Digital Root Formula (Optimized)

### **Method Used**
Mathematical Digital Root Formula

### **Main Idea**
Instead of repeatedly adding digits, this method uses the mathematical property of the digital root.

- If the number is a single digit, return it.
- If the number is divisible by 9, the answer is 9.
- Otherwise, the answer is the remainder when divided by 9.

This produces the final single-digit result in constant time.

---

### **Detailed Explanation**
1. Check if the number is already a single digit.
   - If yes, return it immediately.
2. Check whether the number is divisible by 9.
   - If true, return 9.
3. Otherwise, return `num % 9`.
4. This works because every positive integer has a unique digital root based on modulo 9 arithmetic.

---

### **Complexity**
**Time Complexity:** O(1)  
**Space Complexity:** O(1)

---

## ⚙️ Solution 2: Repeated Digit Sum (Brute Force)

### **Method Used**
Repeated Digit Extraction

### **Main Idea**
This method repeatedly extracts each digit of the number, adds them together, and continues the process until only a single digit remains.

It directly simulates the process described in the problem statement.

---

### **Detailed Explanation**
1. If the number is already a single digit, return it.
2. While the number has more than one digit:
   - Initialize a variable to store the digit sum.
   - Extract each digit using modulo (`% 10`).
   - Add the extracted digit to the running sum.
   - Remove the last digit using integer division (`// 10`).
3. Replace the original number with the computed sum.
4. Repeat until the number becomes a single digit.
5. Return the final single-digit result.

---

### **Complexity**
**Time Complexity:** O(log n) per iteration (overall very small due to shrinking digits)  
**Space Complexity:** O(1)

---

## 🆚 Comparison Summary

| Aspect | Digital Root Formula | Repeated Digit Sum |
|--------|-----------------------|--------------------|
| Time Complexity | O(1) | O(log n) |
| Space Complexity | O(1) | O(1) |
| Uses Mathematics | Yes | No |
| Simulates Process | No | Yes |
| Performance | Fastest | Slower |
| Recommended | Yes | Good for understanding |

---

## 🏁 Conclusion
The **Digital Root Formula** is the optimal solution because it computes the answer in constant time using a simple mathematical observation.

The **Repeated Digit Sum** approach is intuitive and closely follows the problem statement, making it useful for understanding the underlying process, but it is less efficient than the mathematical solution.