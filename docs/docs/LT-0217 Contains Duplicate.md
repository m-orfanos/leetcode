---
tags:
- difficulty/easy
- topics/array
- topics/hash-table
- topics/sorting
---

# 0217 Contains Duplicate

<https://leetcode.com/problems/contains-duplicate>

## Description

- Problem statement
    - Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.
- Constraints
    - $1 <= nums.length <= 10^5$
    - $-10^9 <= nums[i] <= 10^9$
- Examples
    - Example 1
        - Input: `nums = [1,2,3,1]`
        - Output: `true`
    - Example 2
        - Input: `nums = [1,2,3,4]`
        - Output: `false`
    - Example 3
        - Input: `nums = [1,1,1,3,3,4,3,2,4,2]`
        - Output: `true`

## Solutions

### Sort and check adjacent

```python
def contains_duplicate(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return True
    return False
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Use map to track discovered

```python
def contains_duplicate(nums: List[int]) -> bool:
    seen = {}
    for x in nums:
        if x in seen:
            return True
        seen[x] = True
    return False
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Use set to track discovered

```python
def contains_duplicate(nums: List[int]) -> bool:
    s = set()
    for x in nums:
        if x in s:
            return True
        s.add(x)
    return False
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Convert list to set and check length

```python
def contains_duplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
```

Time complexity: $O(n)$
Space complexity: $O(n)$
