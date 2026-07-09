# Unique Number of Occurrences

## 🧩 Problem Overview

You are given an integer array where each value may appear multiple times.

Your task is to determine whether the number of occurrences of every distinct value is unique.

If no two values have the same occurrence count, return `True`; otherwise, return `False`.

---

## 💡 Solution: Dictionary and Set

### **Method Used**

Dictionary (Hash Map) + Set

### **Main Idea**

The solution uses a dictionary to count how many times each number appears in the array.

Once all frequencies are calculated, a set is used to verify whether any frequency has already been seen.

* If a frequency is already present in the set, two numbers have the same occurrence count, so return `False`.
* Otherwise, add the frequency to the set and continue checking.
* If all frequencies are unique, return `True`.

---

### **Detailed Explanation**

1. Create an empty dictionary.

   * Store each unique number as the key.
   * Store its occurrence count as the value.

2. Traverse the array.

   * If the number already exists in the dictionary, increase its count.
   * Otherwise, add it to the dictionary with its initial count.

3. Create an empty set.

   * This will store all occurrence counts that have already been encountered.

4. Traverse all frequency values stored in the dictionary.

   * If the current frequency already exists in the set, return `False`.
   * Otherwise, insert the frequency into the set.

5. If all frequencies are checked without finding duplicates, return `True`.

---

### **Example Walkthrough**

Input:

[1, 2, 2, 1, 1, 3]

Frequency Count:

* 1 → 3 occurrences
* 2 → 2 occurrences
* 3 → 1 occurrence

Checking frequencies:

* Add 3 to the set
* Add 2 to the set
* Add 1 to the set

No duplicate frequencies are found.

Output:

True

---

### **Complexity**

**Time Complexity:** O(n)

* Counting frequencies takes O(n).
* Checking uniqueness of frequencies also takes O(n).

Overall Time Complexity: **O(n)**

**Space Complexity:** O(n)

* Dictionary stores frequencies of distinct elements.
* Set stores occurrence counts.

---

## 🏁 Conclusion

This approach efficiently solves the problem by using a dictionary to count occurrences and a set to detect duplicate frequencies.

Since both insertion and lookup operations in a dictionary and set take constant time on average, the overall solution runs in linear time and is well suited for large input arrays.