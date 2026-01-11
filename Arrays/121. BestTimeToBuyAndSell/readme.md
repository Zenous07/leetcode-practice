# Best Time to Buy and Sell Stock

## 🧩 Problem Overview
You are given an array prices where prices[i] represents the price of a stock on the ith day.

You are allowed to complete only one transaction:
- Buy one stock on one day
- Sell it on a future day

Return the maximum profit you can achieve.
If no profit is possible, return 0.

---

## 💡 Solution: One-Pass Greedy (Minimum Price Tracking)

### **Method Used**
One-Pass Greedy Algorithm

### **Main Idea**
The idea is to track the minimum stock price seen so far while iterating through the array.
At each step, calculate the profit that could be made by selling on the current day.
Update the maximum profit whenever a better profit is found.

---

### **Detailed Explanation**
1. Initialize:
   - `min_price` as the first day's price.
   - `max_profit` as 0.
2. Traverse the price array:
   - If the current price is lower than `min_price`, update `min_price`.
   - Otherwise, calculate the profit as `current_price - min_price`.
   - Update `max_profit` if the calculated profit is higher.
3. After the traversal, return `max_profit`.

---

### **Complexity**
Time Complexity: O(n)  
Space Complexity: O(1)

Where n is the number of days.

---

## 🏁 Conclusion
The One-Pass Greedy approach efficiently finds the maximum possible profit using a single transaction.
It runs in linear time, uses constant space, and is the optimal solution for this problem.
