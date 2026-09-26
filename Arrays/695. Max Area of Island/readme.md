# Max Area of Island

## 🧩 Problem Overview

You are given an `m x n` binary matrix called `grid`.

An island is a group of `1`s representing land that are connected 4-directionally:

* Up
* Down
* Left
* Right

Diagonal connections do not count.

The area of an island is the total number of `1` cells that belong to that island.

Your task is to find and return the maximum area among all islands in the grid.

If there is no island, return `0`.

---

## 💡 Solution: Depth-First Search (DFS)

### **Method Used**

Depth-First Search (DFS) + Grid Traversal

### **Main Idea**

Whenever we find a cell containing `1`, we have discovered an unvisited island.

We use DFS to explore the entire island starting from that cell.

During the DFS:

* Mark the current land cell as visited.
* Count the current cell as `1` area.
* Recursively explore all four neighboring cells.
* Add the areas returned by those four recursive calls.

The DFS therefore returns the total area of the island connected to the starting cell.

After finding the area of an island, compare it with the current maximum area and keep the larger value.

---

### **Detailed Explanation**

1. Initialize `maxArea` to `0`:

    * This stores the largest island area found so far.

2. Find the dimensions of the grid:

    * `m` represents the number of rows.
    * `n` represents the number of columns.

3. Create a DFS function:

    * The DFS receives the current row and column.
    * It checks whether the position is outside the grid.
    * It also checks whether the current cell is water or has already been visited.
    * If any of these conditions are true, return `0`.

4. Mark the current land cell as visited:

    * Change the current cell from `1` to `0`.
    * This prevents the same cell from being counted again.
    * It also prevents the DFS from repeatedly moving between already visited cells.

5. Count the current cell:

    * The current land cell contributes `1` to the island area.

6. Explore all four directions:

    * Move down.
    * Move right.
    * Move up.
    * Move left.

    The areas returned from these four directions are added to the current cell's area.

7. Traverse the entire grid:

    * Check every cell using nested loops.
    * Whenever a `1` is found, start a DFS from that cell.
    * The DFS returns the complete area of that island.

8. Update the maximum area:

    * Compare the current island's area with `maxArea`.
    * Keep whichever value is larger.

9. Return `maxArea`:

    * After every cell has been processed, `maxArea` contains the largest island area.

---

### **Why Do We Mark Cells as `0`?**

Suppose an island contains several connected cells.

While DFS is exploring the island, it may reach a cell from multiple directions.

If we do not mark visited cells, the DFS could visit the same cell repeatedly.

By changing a visited `1` into `0`, that cell becomes treated as water.

Therefore:

* Each land cell is counted exactly once.
* The DFS does not get stuck revisiting cells.
* No separate `visited` set is required.

---

### **How Does the DFS Calculate the Area?**

Consider a small island:
