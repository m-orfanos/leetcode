---
tags:
- difficulty/medium
- topics/prefix-sum
---

# 0238 Product of Array Except Self

<https://leetcode.com/problems/product-of-array-except-self>

## Description

- Problem statement
    - Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
    - The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
    - You must write an algorithm that runs in $O(n)$ time and without using the division operation.
- Constraints
    - $2 <= nums.length <= 10^5$
    - $-30 <= nums[i] <= 30$
    - The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.
- Examples
    - Example 1
        - Input: $nums = [1,2,3,4]$
        - Output: $[24,12,8,6]$
    - Example 2
        - Input: $nums = [-1,1,0,-3,3]$
        - Output: $[0,0,9,0,0]$

## Solutions

### Brute-force approach

```python
def product_except_self(nums: List[int]) -> List[int]:
    ans = []
    for i in range(len(nums)):
        tmp = 1
        for j in range(len(nums)):
            if i == j:
                continue
            tmp *= nums[j]
        ans.append(tmp)
    return ans
```

Time complexity: $O(n^2)$
Space complexity: $O(n)$

### Forward and backward passes

Create two arrays holding the pair-wise product of elements as follows

$forward[i] = a[0]*a[1]*…*a[i]$
$backward[i] = a[i]*a[i+1]*…*a[n]$

then for a given i, $forward[i-1] * backward[i+1]$ skips $a[i]$
e.g. $(a[0]*a[1]*…*a[i-1]) * (a[i+1]*a[i+2]*…*a[n])$

```python
def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    
    forward = [1] * n
    forward[0] = nums[0]
    
    backward = [1] * n
    backward[n - 1] = nums[n - 1]
    
    for i in range(1, n):
        forward[i] = forward[i - 1] * nums[i]
        backward[n - 1 - i] = backward[n - 1 - i + 1] * nums[n - 1 - i]
        
    ans = [0] * n
    ans[0] = backward[1]
    ans[n - 1] = forward[n - 1 - 1]
    for i in range(1, n - 1):
        ans[i] = forward[i - 1] * backward[i + 1]
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(n)$
