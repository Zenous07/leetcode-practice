# Word Pattern

## 🧩 Problem Overview

You are given a pattern string and a sentence consisting of words separated by spaces.

Your task is to determine whether the sentence follows the given pattern.

A valid pattern requires a **one-to-one (bijective) mapping** between pattern characters and words:

- Each pattern character must map to exactly one unique word.
- Each unique word must map to exactly one pattern character.
- No two characters can map to the same word.
- No two words can map to the same character.

---

## 💡 Solution: Two Hash Maps (Dictionaries)

### **Method Used**

Hash Maps (Dictionary Mapping)

### **Main Idea**

The solution uses two dictionaries to maintain a one-to-one relationship:

- One dictionary maps each pattern character to its corresponding word.
- Another dictionary maps each word back to its corresponding pattern character.

Before creating a new mapping, the algorithm checks whether either the character or the word has already been mapped. This ensures the mapping remains bijective throughout the process.

---

### **Detailed Explanation**

1. Split the input sentence into individual words.

2. Compare the lengths of the pattern and the list of words.

   * If they are different, the pattern cannot match the sentence, so return `False`.

3. Create two empty dictionaries:

   * One for character → word mapping.
   * One for word → character mapping.

4. Traverse both the pattern and the words together.

   * If the current pattern character has not been seen before:
     * Check whether the current word has already been assigned to another character.
     * If yes, return `False`.
     * Otherwise, store both mappings.

5. If the pattern character already exists:

   * Verify that it maps to the current word.
   * If it does not, return `False`.

6. If the entire traversal finishes without conflicts, return `True`.

---

### **Example Walkthrough**

Input:

Pattern: `"abba"`

Sentence: `"dog cat cat dog"`

Step-by-step:

* 'a' → "dog" (new mapping)
* 'b' → "cat" (new mapping)
* 'b' → "cat" (matches previous mapping)
* 'a' → "dog" (matches previous mapping)

No conflicts are found, so the pattern is valid.

Output:

`True`

---

### **Complexity**

**Time Complexity:** O(n)

* Splitting the sentence takes O(n).
* Traversing the pattern and words takes O(n).
* Dictionary lookups and insertions are O(1) on average.

**Space Complexity:** O(n)

* Two dictionaries are used to store the mappings.

---

## 🏁 Conclusion

Using two hash maps guarantees a one-to-one relationship between pattern characters and words.

This approach efficiently detects duplicate or conflicting mappings while traversing the input only once, making it both simple and optimal.