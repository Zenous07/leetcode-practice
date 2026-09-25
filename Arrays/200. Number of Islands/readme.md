# Number of Islands

## 🧩 Problem Overview

You are given a 2D grid containing `'1'`s and `'0'`s.

* `'1'` represents land.
* `'0'` represents water.

An island is formed by connecting adjacent land cells horizontally or vertically.

Your task is to find and return the total number of islands in the grid.

Each island is a separate group of connected `'1'` cells.

---

## 💡 Solution: Depth-First Search (DFS)

### **Method Used**

Depth-First Search (DFS) + Grid Traversal

### **Main Idea**

Whenever we find a cell containing `'1'`, it represents a new island.

We then use DFS to visit all land cells connected to that cell.

During the DFS:

* Mark the current land cell as visited by changing `'1'` to `'0'`.
* Explore the cell above.
* Explore the cell below.
* Explore the cell to the left.
* Explore the cell to the right.

After the entire island has been visited, continue scanning the grid.

Every time an unvisited `'1'` is found, it means we have discovered a new island, so we increase the island count.

---

### **Detailed Explanation**

1. Get the dimensions of the grid:

   * `m` represents the number of rows.
   * `n` represents the number of columns.

2. Create a DFS function:

   * The DFS receives the current row and column.
   * First, check whether the position is outside the grid.
   * Also check whether the current cell is water or has already been visited.
   * If any of these conditions are true, stop the DFS.

3. Mark the current land cell as visited:

   * Change the current cell from `'1'` to `'0'`.
   * This prevents the same cell from being visited again.

4. Explore all four directions:

   * Move down.
   * Move up.
   * Move right.
   * Move left.

5. Traverse the entire grid:

   * Check every cell using nested loops.
   * If the current cell is `'1'`, a new island has been found.

6. Start DFS from the new island:

   * DFS visits every connected land cell belonging to that island.
   * Once DFS finishes, the entire island has been marked as visited.

7. Increase the island count:

   * Since we found a new island, increase the count by `1`.

8. Continue until the entire grid has been checked.

9. Return the final island count.

---

### **Why Do We Change `'1'` to `'0'`?**

Changing a visited land cell from `'1'` to `'0'` allows us to use the grid itself as the visited structure.

For example:

```text
1 1 0
1 0 0
0 0 1