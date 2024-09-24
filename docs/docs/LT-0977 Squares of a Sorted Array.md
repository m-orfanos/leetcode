---
tags:
- difficulty/easy
- topics/array
- topics/two-pointers
- topics/sorting
---

# 0977 Squares of a Sorted Array

<https://leetcode.com/problems/squares-of-a-sorted-array>

## Description

- Problem statement
    - Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
- Constraints
    - $1 <= nums.length <= 10^4$
    - $-10^4 <= nums[i] <= 10^4$
    - $nums$ is sorted in non-decreasing order.
- Examples
    - Example 1
        - Input: `nums = [-4,-1,0,3,10]`
        - Output: `[0,1,9,16,100]`
    - Example 2
        - Input: `nums = [-7,-3,2,3,11]`
        - Output: `[4,9,9,49,121]`
- Follow up
    - Squaring each element and sorting the new array is very trivial, could you find an $O(n)$ solution using a different approach?

## Solutions

### Map and sort

```python
def sorted_squares(nums: List[int]) -> List[int]:
    return sorted(map(lambda x: x**2, nums))
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Two-pointer approach

Take advantage of

1. the fact that the input list is sorted and
2. the square of any integer will always be positive.

Use 2 indices, left and right
Iterate from both sides, storing the largest to the response starting from the end (index i)
Update indices, left/right/i accordingly
Repeat while left <= right

```python
def sorted_squares(nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
    
    ans = [0] * len(nums)
    
    i = len(nums) - 1
    while left <= right:
        lhs = nums[left] ** 2
        rhs = nums[right] ** 2
        
        if lhs > rhs:
            ans[i] = lhs
            left += 1
        else:
            ans[i] = rhs
            right -= 1
            
        i -= 1
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(n)$
