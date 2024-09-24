---
tags:
- difficulty/easy
- topics/array
- topics/dynamic-programming
---

# 0121 Best Time to Buy and Sell Stock

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock>

## Description

- Problem statement
    - You are given an array `prices` where `prices[i]` is the price of a given stock on the $i^{th}$ day.
    - You want to maximise your profit by choosing a _single day_ to buy one stock and choosing a different day in the future to sell that stock.
    - Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.
- Constraints
    - $1 <= prices.length <= 10^5$
    - $0 <= prices[i] <= 10^4$
- Examples
    - Example 1
        - Input: `prices = [7,1,5,3,6,4]`
        - Output: `5`
    - Example 2
        - Input: `prices = [7,6,4,3,1]`
        - Output: `0`

## Solutions

### Brute force - check all the things

- This approach timed out for python submissions.

```python
def max_profit(prices: List[int]) -> int:
    profit = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            profit = max(profit, prices[j] - prices[i])
    return profit
```

Time complexity: $O(n^2)$
Space complexity: $O(1)$

### Kadane's algorithm

Begin by plotting the prices on a graph looking for a pattern.

![[Pasted image 20240412173748.png|800]]

- We are trying to find the largest height different between two points. In the image above it's day 1 and 4.
- The purple line shows the sum of differences, `(d2-d1) + (d3-d2) + (d4-d3)`.
- This simplifies to `(d4-d1)`.

Calculate the difference between neighbouring elements.

```text
given `[7, 1, 5, 3, 6, 4]`

1 - 7 = -6
5 - 1 = +4
3 - 5 = -2
6 - 3 = +3
4 - 6 = -2

[-6, +4, -2, +3, -2]
```

Use a rolling window and keep track of the "best" and "current" sums.

when to shift the window edges (LHS/RHS)?

- Keep growing window from RHS until it reaches a negative sum while keeping track of the largest sum found so far.
- When negative -> set current to zero, now conceptually the "LHS is the current index" and continue to grow from RHS (no need to keep track of the indices directly).
- Why not try to incrementally shrink window from LHS?
    - 2 cases, either LHS contains a negative or positive number
        - negative number: can never happen, the first value will always be positive or zero
        - positive number: you would never want to remove a positive value as it would reduce the sum
    - There are other cases, but they are all subsets of the above and thus covered by the base case (e.g. best/current sums are always greater or equal to 0)

```typescript
function max_profit(prices: number[]): number {
    if (prices.length <= 1) {
        return 0;
    }
    
    let best = 0;
    let curr = 0;
    
    // iteration begins at 1
    for (let i = 1; i < prices.length; i += 1) {
        const diff = prices[i] - prices[i - 1];
        curr += diff;
        if (curr < 0) {
            curr = 0;
        }
        if (curr > best) {
            best = curr;
        }
    }
    
    return best;
}
```

Time complexity: $O(n)$
Space complexity: $O(1)$
