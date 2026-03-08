# First Bad Version

## 🧩 Problem Overview
You are given multiple product versions where each version builds upon the previous one. At some point, a version becomes faulty, and all versions after it are also faulty.

The task is to determine the **first version where the failure begins**.

An external API is available that tells whether a given version is bad. The challenge is to find the first bad version while making **as few API calls as possible**.

Because the versions are sequential and once a bad version appears all later versions remain bad, the versions follow a **monotonic pattern**:
- Good versions → followed by → Bad versions.

---

## 💡 Solution: Binary Search

### **Method Used**
Binary Search

### **Main Idea**
Since the versions follow a pattern where all good versions come first and all bad versions come afterward, we can apply **Binary Search** to efficiently locate the first bad version.

Instead of checking each version sequentially, we repeatedly divide the search space into halves and eliminate the portion that cannot contain the first bad version.

---

### **Detailed Explanation**
1. Two pointers define the current search range of versions:
   - One pointing to the start of the range.
   - One pointing to the end of the range.

2. The algorithm repeatedly checks the **middle version** of the current range.

3. Using the API, we determine whether this middle version is bad.

4. Based on the result:
   - If the version is **bad**, the first bad version could either be this version or somewhere **before it**, so the search continues in the **left half**.
   - If the version is **good**, the first bad version must be **after it**, so the search continues in the **right half**.

5. The search space keeps shrinking until the two pointers converge.

6. At the end of the process, the pointer representing the start of the range will point to the **first bad version**.

---

### **Why This Works**
Because once a bad version appears, all versions after it are also bad. This property allows us to discard half of the remaining versions after each check.

This dramatically reduces the number of API calls required.

---

### **Complexity**

**Time Complexity:** O(log n)  
Each step halves the search space.

**Space Complexity:** O(1)  
Only a few variables are used regardless of input size.

---

## 🏁 Conclusion
Binary Search is the optimal approach for this problem because it efficiently exploits the **ordered transition from good versions to bad versions**. By repeatedly narrowing the search space, the first bad version can be identified with minimal API calls.