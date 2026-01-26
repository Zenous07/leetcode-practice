# Baseball Game

## 🧩 Problem Overview
You are given a list of operations representing scores in a baseball game with special rules.
Starting from an empty record, each operation modifies the record based on predefined rules.

The goal is to return the **sum of all scores** after applying every operation.

---

## 💡 Solution: Stack Simulation Method

### **Method Used**
Stack (List) Simulation

### **Main Idea**
This approach uses a list to simulate the score record.
Each operation modifies the list according to the rules:
- Numbers are added directly.
- `"+"` adds the sum of the last two scores.
- `"D"` adds double of the last score.
- `"C"` removes the last score.

A running total is maintained to efficiently compute the final sum.

---

### **Detailed Explanation**
1. Initialize:
   - `result` list to store valid scores.
   - `answer` variable to track the running sum.
2. Iterate through each operation:
   - If operation is `"+"`:
     - Take the last two scores from the list.
     - Add their sum to the list and update `answer`.
   - If operation is `"D"`:
     - Double the last score.
     - Append it and update `answer`.
   - If operation is `"C"`:
     - Remove the last score from the list.
     - Subtract it from `answer`.
   - Otherwise:
     - Convert the operation to an integer.
     - Append it to the list and add it to `answer`.
3. Return `answer` after processing all operations.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(n)

---

## 🆚 Comparison Summary

| Aspect | Stack Simulation |
|------|------------------|
| Time Complexity | O(n) |
| Space Complexity | O(n) |
| Extra Data Structure | Yes (List) |
| Readability | High |
| Recommended | ✅ Yes |

---

## 🏁 Conclusion
The **Stack Simulation Method** cleanly models the baseball game rules.
It efficiently processes each operation in one pass and produces the correct total score.
