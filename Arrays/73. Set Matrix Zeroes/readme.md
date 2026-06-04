# Set Matrix Zeroes

## 🧩 Problem Overview
You are given an m x n matrix.

If any element in the matrix is 0, you must set its entire row and entire column to 0.

The modification must be performed in-place on the matrix.

---

## 💡 Solution: Row and Column Tracking Using Sets

### **Method Used**
Hash Set Tracking

### **Main Idea**
The idea is to first identify all rows and columns that contain a zero.

Instead of modifying the matrix immediately (which could create additional zeros and affect future decisions), store:
- All row indices containing a zero
- All column indices containing a zero

After collecting this information, traverse the matrix again and set every cell to zero if its row or column is marked.

---

### **Detailed Explanation**
1. Create two sets:
   - `rows` to store row indices containing a zero.
   - `cols` to store column indices containing a zero.

2. Traverse the matrix:
   - Whenever a zero is found, store its row index in `rows`.
   - Store its column index in `cols`.

3. Traverse the matrix again:
   - If the current row exists in `rows`, set the element to zero.
   - If the current column exists in `cols`, set the element to zero.

4. The matrix is now updated according to the problem requirements.

---

### **Complexity**
Time Complexity: O(m × n)

Space Complexity: O(m + n)

Where:
- m = number of rows
- n = number of columns

The additional space is used to store the rows and columns that must be zeroed.

---

## 🏁 Conclusion
This approach cleanly separates the detection and modification phases.

By storing the affected rows and columns first, it avoids accidental propagation of zeros during traversal.

It is simple to understand, runs in linear matrix time, and is an effective solution using extra space.