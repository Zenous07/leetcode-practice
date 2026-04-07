# Hamming Distance

## 🧩 Problem Overview

The Hamming distance between two integers is defined as the number of positions at which the corresponding bits are different.

Given two integers, the goal is to compute how many bit positions differ between them.

---

## 💡 Solution: Bitwise XOR and Bit Counting

### **Method Used**

Bitwise XOR + Counting Set Bits

### **Main Idea**

When two numbers are XORed:

- Bits that are the same result in `0`
- Bits that are different result in `1`

So, performing `x ^ y` gives a number whose binary representation contains `1`s exactly at positions where the bits differ.

By counting the number of `1`s in this result, we get the Hamming distance.

---

### **Detailed Explanation**

1. Perform XOR operation on the two numbers:

   - This highlights differing bit positions.

2. Convert the result to binary:

   - This helps in examining each bit.

3. Count the number of `'1'`s:

   - Each `'1'` represents a differing bit.

4. Return the count:

   - This count is the Hamming distance.

---

### **Example Walkthrough**

Input: x = 3, y = 7

Binary representation:

3 → 011  
7 → 111  

XOR result:

3 ^ 7 → 100  

Count of `1`s → 1

Output → 1

---

### **Complexity**

Time Complexity: O(k)

- Where k is the number of bits (up to 32 for integers)

Space Complexity: O(1)

- Uses only a few variables

---

## 🏁 Conclusion

Using XOR is an efficient way to directly identify differing bits.
Counting the set bits in the XOR result gives the Hamming distance in a simple and optimized manner.

This approach is fast, clean, and leverages bit manipulation effectively.