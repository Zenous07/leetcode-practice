# 771. Jewels and Stones

## 🧩 Problem Overview
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

---

## 💡 Solution 1: Hash Set Lookup (Optimized)

### **Method Used**
Hash Set (O(1) Lookup)

### **Main Idea**
This method first converts the `jewels` string into a Hash Set. This allows us to check if any given stone is a jewel in constant time. We then iterate through the `stones` and increment our counter whenever a stone exists in the set.

---

### **Detailed Explanation**
1. Create a set `s` from the string `jewels`.
2. Initialize a counter `count` to 0.
3. Iterate through each character `i` in the string `stones`.
4. For every character, check if `i` exists in the set `s`.
5. If it exists, increment `count`.
6. Return the final `count`.

---

### **Complexity**
- **Time Complexity:** O(n + m) — Where *n* is the length of jewels and *m* is the length of stones.
- **Space Complexity:** O(n) — To store the jewels in a set.

---

## ⚙️ Solution 2: Brute Force Nested Search

### **Method Used**
Linear Search (Nested Iteration)

### **Main Idea**
For every stone you have, this method checks if it exists in the `jewels` string by performing a linear scan. In Python, the `if i in jewels` syntax on a string results in an O(n) search per stone.

---

### **Detailed Explanation**
1. Initialize a counter `count` to 0.
2. Iterate through each character `i` in the string `stones`.
3. For each stone, check if it is present in the `jewels` string using a linear search.
4. If found, increment the counter.
5. Return the total count.

---

### **Complexity**
- **Time Complexity:** O(n * m) — For every stone (m), we potentially scan all jewels (n).
- **Space Complexity:** O(1) — No extra data structures are used.

---

## 🆚 Comparison Summary

| Aspect | Hash Set Method | Brute Force Method |
| :--- | :--- | :--- |
| **Time Complexity** | O(n + m) | O(n * m) |
| **Space Complexity** | O(n) | O(1) |
| **Lookup Speed** | O(1) Average | O(n) Linear |
| **Performance** | Very Fast | Slow for large strings |
| **Recommended** | Yes | No |

---

## 🏁 Conclusion
The Hash Set approach is significantly more efficient because it reduces the lookup time from linear to constant. While the brute force method uses less memory, the speed gain of the optimized version is preferred for almost all scenarios.