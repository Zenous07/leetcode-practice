# Restore Finishing Order

## 🧩 Problem Overview

You are given two integer arrays:

- **order** represents the finishing order of all participants in a race.
- **friends** contains the IDs of your friends, sorted in increasing order.

Your task is to return your friends' IDs in the exact order they finished the race.

Instead of sorting or rearranging the `friends` array, simply follow the race's finishing order and collect only the participants who are your friends.

---

## 💡 Solution: Hash Set + Single Traversal

### **Method Used**

Hash Set + Linear Scan

### **Main Idea**

The `friends` array contains only the IDs you care about.

To quickly determine whether a participant is your friend:

- Store all friend IDs in a **Hash Set**.
- Traverse the `order` array from beginning to end.
- Whenever the current participant exists in the set, add them to the answer.
- Since `order` already represents the finishing order, the collected IDs will automatically be in the correct order.

---

### **Detailed Explanation**

1. Store all friend IDs in a Hash Set.

   - This allows checking whether someone is your friend in constant time.

2. Create an empty result list.

   - This will store your friends in their finishing order.

3. Traverse the `order` array from left to right.

   - For each participant:
     - Check whether their ID exists in the Hash Set.
     - If yes, append it to the result.

4. Return the result.

   - The result already follows the race's finishing order.

---

### **Example Walkthrough 1**

**Input**

order = [3, 1, 2, 5, 4]

friends = [1, 3, 4]

**Step-by-step**

- Visit 3 → Friend → Add → [3]
- Visit 1 → Friend → Add → [3, 1]
- Visit 2 → Not a friend
- Visit 5 → Not a friend
- Visit 4 → Friend → Add → [3, 1, 4]

**Output**

[3, 1, 4]

---

### **Example Walkthrough 2**

**Input**

order = [1, 4, 5, 3, 2]

friends = [2, 5]

**Step-by-step**

- Visit 1 → Not a friend
- Visit 4 → Not a friend
- Visit 5 → Friend → Add → [5]
- Visit 3 → Not a friend
- Visit 2 → Friend → Add → [5, 2]

**Output**

[5, 2]

---

### **Example Walkthrough 3**

**Input**

order = [6, 2, 4, 1, 5, 3]

friends = [1, 3, 6]

**Step-by-step**

- Visit 6 → Friend → Add → [6]
- Visit 2 → Not a friend
- Visit 4 → Not a friend
- Visit 1 → Friend → Add → [6, 1]
- Visit 5 → Not a friend
- Visit 3 → Friend → Add → [6, 1, 3]

**Output**

[6, 1, 3]

---

### **Why Use a Hash Set?**

Without a Hash Set, checking whether each participant is a friend would require searching through the `friends` array every time.

A Hash Set allows each lookup to be performed in **O(1)** time on average, making the overall solution much more efficient.

---

### **Complexity**

**Time Complexity:** O(n)

- Building the Hash Set takes O(k), where `k` is the number of friends.
- Traversing the `order` array takes O(n).
- Overall complexity is O(n).

**Space Complexity:** O(k)

- The Hash Set stores all friend IDs.

---

## 🏁 Conclusion

The race order already provides the correct finishing sequence.

By storing the friend IDs in a Hash Set and scanning the finishing order once, we can efficiently collect only the required participants while preserving their finishing positions.

This approach is simple, intuitive, and runs in linear time.