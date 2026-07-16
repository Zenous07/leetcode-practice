# Isomorphic Strings

## 🧩 Problem Overview

You are given two strings `s` and `t`.

Your task is to determine whether the two strings are **isomorphic**.

Two strings are isomorphic if every character in the first string can be replaced by exactly one unique character in the second string while preserving the order of characters.

A character cannot map to multiple different characters, and two different characters cannot map to the same character.

---

## 💡 Solution: Two Hash Maps (Dictionaries)

### **Method Used**

Two Dictionaries (Hash Maps)

### **Main Idea**

To verify whether two strings are isomorphic, we need to maintain a one-to-one mapping between their characters.

The algorithm uses two dictionaries:

* The first dictionary stores the mapping from characters in `s` to characters in `t`.
* The second dictionary stores the reverse mapping from characters in `t` to characters in `s`.

Using both dictionaries guarantees that:

* One character in `s` always maps to the same character in `t`.
* No two different characters in `s` map to the same character in `t`.

---

### **Detailed Explanation**

1. Compare the lengths of both strings.

   * If the lengths are different, they cannot be isomorphic.

2. Create two empty dictionaries.

   * One stores mappings from `s` to `t`.
   * The other stores mappings from `t` to `s`.

3. Traverse both strings simultaneously.

   * If the current character from `s` has not been mapped yet:
     * Check whether the current character from `t` is already mapped to another character.
     * If it is, return `False`.
     * Otherwise, create mappings in both dictionaries.

4. If the current character from `s` is already mapped:

   * Verify that it maps to the current character in `t`.
   * If not, return `False`.

5. If every character satisfies the mapping rules, return `True`.

---

### **Example Walkthrough**

Input:

```
s = "egg"
t = "add"
```

Step-by-step:

* Map `e → a`
* Map `g → d`
* Next `g` also maps to `d` ✔
* All mappings are valid

Return `True`

---

### **Another Example**

Input:

```
s = "f11"
t = "b23"
```

Step-by-step:

* Map `f → b`
* Map `1 → 2`
* Next `1` tries to map to `3`
* Existing mapping is `1 → 2`
* Mapping becomes inconsistent

Return `False`

---

### **Complexity**

**Time Complexity:** O(n)

* Each character is processed exactly once.

**Space Complexity:** O(n)

* Two dictionaries are used to store character mappings.

---

## 🏁 Conclusion

Using two dictionaries ensures a valid one-to-one mapping between characters in both strings.

By checking both forward and reverse mappings simultaneously, the algorithm efficiently detects invalid mappings while traversing the strings only once.

This approach is simple, efficient, and works for all valid ASCII characters.