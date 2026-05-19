# Valid Sudoku

## 🧩 Problem Overview

Given a 9 × 9 Sudoku board, determine whether the board is valid according to Sudoku rules.

Only the filled cells need to be checked.

A valid Sudoku board must satisfy:

- Each row contains digits 1–9 without repetition.
- Each column contains digits 1–9 without repetition.
- Each 3 × 3 sub-box contains digits 1–9 without repetition.

The board may be partially filled and does not need to be solvable.

---

## 💡 Solution: Set-Based Validation Method

### **Method Used**

Hash Set Validation for Rows, Columns, and Sub-Boxes

### **Main Idea**

The solution checks the Sudoku board in three separate stages:

1. Validate every row.
2. Validate every column.
3. Validate every 3 × 3 sub-box.

A set is used to track already seen numbers.
If a duplicate digit is found in any row, column, or sub-box, the board is invalid.

---

### **Detailed Explanation**

### **Step 1: Validate Rows**

- Traverse each row one by one.
- Create an empty set for the current row.
- Ignore empty cells represented by `'.'`.
- If a number already exists in the set:
  - A duplicate is found.
  - Return `False`.
- Otherwise, add the number to the set.

This ensures every row contains unique digits.

---

### **Step 2: Validate Columns**

- Traverse each column one by one.
- Create a new empty set for each column.
- Check all values vertically.
- Ignore empty cells.
- If a duplicate digit appears:
  - Return `False`.

This ensures every column contains unique digits.

---

### **Step 3: Validate 3 × 3 Sub-Boxes**

The Sudoku board contains 9 smaller 3 × 3 boxes.

The starting positions of these boxes are:

- (0,0), (0,3), (0,6)
- (3,0), (3,3), (3,6)
- (6,0), (6,3), (6,6)

For each sub-box:

- Create a new empty set.
- Traverse all 9 cells inside the box.
- Ignore empty cells.
- If a digit already exists in the set:
  - Return `False`.

This ensures every sub-box contains unique digits.

---

### **Final Step**

- If no duplicates are found in rows, columns, or sub-boxes:
  - Return `True`.

The Sudoku board is valid.

---

### **Example Walkthrough**

Example Board:

[["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]]

Step-by-step:

- All rows contain unique digits.
- All columns contain unique digits.
- All 3 × 3 sub-boxes contain unique digits.

Result → `True`

---

### **Complexity**

Time Complexity: O(1)

- The board size is fixed at 9 × 9.
- Every cell is checked a constant number of times.

Space Complexity: O(1)

- Sets store at most 9 digits.

---

## 🏁 Conclusion

Using sets makes duplicate detection simple and efficient.

The algorithm separately validates:
- Rows
- Columns
- 3 × 3 sub-boxes

This approach is clean, easy to understand, and works efficiently for Sudoku validation.