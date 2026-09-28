# Maximum Nesting Depth of the Parentheses

## 🧩 Problem Overview

You are given a valid parentheses string `s`.

Your task is to find the maximum nesting depth of the parentheses.

The nesting depth represents the maximum number of parentheses that are open at the same time.

For example:

`((()))`

has a maximum nesting depth of `3`.

---

## 💡 Solution: Counting Open Parentheses

### **Method Used**

Counting + Tracking Maximum Depth

### **Main Idea**

We can keep track of how many opening parentheses `(` are currently active.

* When we encounter `(`, increase the current depth.
* When we encounter `)`, the current depth represents how deeply nested we are before closing that parenthesis.
* Keep track of the largest depth encountered.
* Decrease the current depth after processing `)`.

The largest value reached by the current depth is the answer.

---

### **Detailed Explanation**

1. Initialize two variables:

    * `count` keeps track of the current nesting depth.
    * `maxDepth` keeps track of the maximum nesting depth seen so far.

2. Traverse the string character by character:

    * If the character is `(`, increase `count` by `1`.
    * If the character is `)`, compare the current `count` with `maxDepth`.
    * After processing the closing parenthesis, decrease `count` by `1`.

3. Keep updating `maxDepth`:

    * `maxDepth` stores the greatest nesting level reached during the traversal.

4. Return `maxDepth`:

    * After processing the entire string, `maxDepth` contains the maximum number of nested parentheses.

---

### **Example Walkthrough**

Input:

`(1+(2*3)+((8)/4))+1`

Track the nesting depth:

* `(` → depth becomes `1`
* `(` → depth becomes `2`
* `)` → depth goes back to `1`
* `(` → depth becomes `2`
* `(` → depth becomes `3`
* `)` → depth goes back to `2`
* `)` → depth goes back to `1`
* `)` → depth becomes `0`

The maximum depth reached was `3`.

Output:

`3`

---

### **Another Example**

Input:

`()(())((()()))`

The deepest section is:

`((()))`

At that point, there are three opening parentheses active at the same time.

Therefore:

Output: `3`

---

### **Why We Don't Need a Stack**

We only need to know how many parentheses are currently open.

Because the string is guaranteed to be a valid parentheses string, every closing parenthesis corresponds to an opening parenthesis.

Therefore, a simple counter is enough.

We do not need to store the actual parentheses in a stack.

---

### **Complexity**

Time Complexity: O(n)

* We traverse the string once.
* Each character is processed only once.

Space Complexity: O(1)

* Only two variables are used to keep track of the current and maximum depth.

---

## 🏁 Conclusion

The problem can be solved by maintaining a counter for the current nesting depth.

Opening parentheses increase the depth, while closing parentheses decrease it.

By keeping track of the largest depth reached during the traversal, we can find the maximum nesting depth in O(n) time and O(1) extra space.