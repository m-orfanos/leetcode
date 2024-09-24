---
tags:
- difficulty/easy
- topics/array
- topics/binary-search
---

# 0704 Binary Search

<https://leetcode.com/problems/binary-search>

## Description

- Problem statement
    - Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.
    - You must write an algorithm with `O(log n)` runtime complexity.
- Constraints
    - $1 <= nums.length <= 10^4$
    - $-10^4 < nums[i], target < 10^4$
    - All the integers in `nums` are unique.
    - `nums` is sorted in ascending order.
- Examples
    - Example 1
        - Input: `nums = [-1,0,3,5,9,12]`, `target = 9`
        - Output: `4`
    - Example 2
        - Input: `nums = [-1,0,3,5,9,12]`, `target = 2`
        - Output: `-1`

## Solutions

### Binary search

compute mid, adjust left/right, repeat

```python
def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        # avoids upcasting (or int overflow in other languages)
        mid = high - (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    # insertion point
    return -(low + 1)
```

Time complexity: $O(log(n))$
Space complexity: $O(1)$
