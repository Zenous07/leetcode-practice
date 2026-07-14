# Unique Morse Code Words

## 🧩 Problem Overview

You are given an array of lowercase English words.

Each letter has a unique Morse code representation. A word can be transformed by replacing every character with its corresponding Morse code and concatenating the results into a single string.

Your task is to determine how many **unique Morse code transformations** exist among all the given words.

---

## 💡 Solution: Hash Set for Unique Transformations

### **Method Used**

Dictionary (Hash Map) + Hash Set

### **Main Idea**

Create a mapping from each lowercase English letter (`a` to `z`) to its Morse code equivalent.

For every word:

* Convert each character into its Morse code.
* Concatenate all Morse codes to form the word's transformation.
* Store the transformation in a set.

Since a set automatically removes duplicates, the final size of the set represents the number of unique Morse code transformations.

---

### **Detailed Explanation**

1. Create a dictionary containing the Morse code for every lowercase English letter.

2. Initialize an empty set to store unique Morse code transformations.

3. Traverse each word in the input array.

4. For every character in the word:

   * Find its Morse code using the dictionary.
   * Append it to build the transformed string.

5. Add the completed transformation to the set.

6. After processing all words, return the size of the set.

---

### **Example Walkthrough**

Input:

["gin", "zen", "gig", "msg"]

Transformations:

* "gin" → "--...-."
* "zen" → "--...-."
* "gig" → "--...--."
* "msg" → "--...--."

Unique transformations:

* "--...-."
* "--...--."

Answer: **2**

---

### **Complexity**

**Time Complexity:** O(n × m)

* `n` = number of words
* `m` = average length of each word
* Each character is processed exactly once.

**Space Complexity:** O(n)

* A set is used to store unique Morse code transformations.

---

## 🏁 Conclusion

Using a dictionary allows fast lookup of each character's Morse code, while a set automatically eliminates duplicate transformations.

This approach is simple, efficient, and processes each word only once, making it an ideal solution for finding the number of unique Morse code representations.