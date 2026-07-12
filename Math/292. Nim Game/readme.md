# Nim Game

## 🧩 Problem Overview

You are given an integer `n` representing the number of stones in a heap.

Two players take turns removing **1 to 3 stones**, and you always make the first move. The player who removes the last stone wins.

Assuming both players play optimally, determine whether you can guarantee a win.

---

## 💡 Solution: Mathematical Observation

### **Method Used**

Modulo (`%`) Operation

### **Main Idea**

The key observation is that whenever the number of stones is a **multiple of 4**, the current player is in a losing position if the opponent plays optimally.

Why?

- If there are exactly **4 stones**, no matter whether you remove 1, 2, or 3 stones, your opponent can always remove the remaining stones and win.
- For every multiple of 4 (8, 12, 16, ...), whatever move you make, your opponent can always remove enough stones to make the remaining pile a multiple of 4 again.
- This strategy continues until you are eventually forced to leave the last stones for your opponent.

Therefore:

- If `n % 4 == 0`, you **cannot** win.
- Otherwise, you **can** win.

---

### **Detailed Explanation**

1. Check if the number of stones is a multiple of 4.

   * If `n % 4 == 0`, return `False` because the opponent can always mirror your moves and maintain the winning strategy.

2. Otherwise, return `True`.

   * You can remove enough stones on your first move to leave a multiple of 4 for your opponent, putting them in the losing position.

---

### **Example Walkthrough**

Input: `n = 7`

Step-by-step:

* 7 is not divisible by 4.
* Remove 3 stones.
* Remaining stones = 4.
* Your opponent is now forced into the losing position.
* Therefore, you can guarantee a win.

Output: `True`

---

### **Complexity**

Time Complexity: **O(1)**

* Only one modulo operation is performed.

Space Complexity: **O(1)**

* No extra space is used.

---

## 🏁 Conclusion

The Nim Game has a simple mathematical pattern.

Every multiple of **4** is a losing position for the current player if both players play optimally.

By checking whether `n` is divisible by 4, we can determine the answer instantly without using recursion or dynamic programming.