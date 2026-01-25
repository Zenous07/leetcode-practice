# Two Sum II – Input Array Is Sorted

## 🧩 Problem Overview
Given a **1-indexed sorted array** of integers `numbers` and an integer `target`, find two numbers such that they add up to `target`.

Return the indices of the two numbers as `[index1, index2]`, where:
- `1 <= index1 < index2 <= numbers.length`
- Exactly **one valid solution** exists
- You must use **constant extra space**

---

## 💡 Solution 1: Two Pointers Method (Optimized)

### **Method Used**
Two Pointers Technique

### **Main Idea**
Since the array is already sorted:
- Use one pointer starting from the **left**
- Use another pointer starting from the **right**
- Adjust pointers based on whether the current sum is **greater than**, **less than**, or **equal to** the target

This avoids unnecessary comparisons and achieves optimal performance.

---

### **Detailed Explanation**
1. Initialize two pointers:
   - `l` at the beginning of the array
   - `r` at the end of the array
2. While `l < r`:
   - If `numbers[l] + numbers[r] == target`, return `[l+1, r+1]`
   - If the sum is greater than `target`, move the right pointer left (`r -= 1`)
   - If the sum is less than `target`, move the left pointer right (`l += 1`)
3. If no pair is found, return `False` (though the problem guarantees a solution).

---

### **Code Implementation**
```python
def twoSum(numbers, target):
    length = len(numbers)
    if length <= 1:
        return False

    l = 0
    r = length - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

    return False

print(twoSum([2, 7, 11, 15], 9))
