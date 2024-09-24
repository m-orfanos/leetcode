---
tags:
- difficulty/medium
- topics/array
- topics/divide-and-conquer
- topics/dynamic-programming
---

# 0053 Maximum Sub-array

<https://leetcode.com/problems/maximum-subarray>

## Description

- Problem statement
    - Given an integer array nums, find the subarray with the largest sum, and return its sum.
- Constraints
    - $1 <= nums.length <= 10^5$
    - $-10^4 <= nums[i] <= 10^4$
- Examples
    - Example 1
        - Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
        - Output: `6`
    - Example 2
        - Input: `nums = [1]`
        - Output: `1`
    - Example 3
        - Input: `nums = [5,4,-1,7,8]`
        - Output: `23`

## Solutions

### Kadane's algorithm

Almost the same as [[LT-0121 Best Time to Buy and Sell Stock]]

```python
def max_sub_array(nums: List[int]) -> int:
    best = -(2**31)
    curr = 0
    for n in nums:
        curr = max(n, curr + n)
        best = max(curr, best)
        
    return best
```

Time complexity: $O(n)$
Space complexity: $O(1)$
