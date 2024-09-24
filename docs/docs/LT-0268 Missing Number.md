---
tags:
- difficulty/easy
- topics/tree
- topics/array
- topics/hash-table
- topics/math
- topics/binary-search
- topics/bit-manipulation
- topics/sorting
---

# 0268 Missing Number

<https://leetcode.com/problems/missing-number>

## Description

- Problem statement
    - Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.
- Constraints
    - $n == nums.length$
    - $1 <= n <= 10^4$
    - $0 <= nums[i] <= n$
    - All the numbers of nums are unique.
- Examples
    - Example 1
        - Input: `nums = [3,0,1]`
        - Output: `2`
    - Example 2
        - Input: `nums = [0,1]`
        - Output: `2`
    - Example 3
        - Input: `nums = [9,6,4,2,3,5,7,0,1]`
        - Output: `8`
- Follow up
    - Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

## Solutions

### Sort and check

```python
def missing_number(nums: List[int]) -> int:
    nums.sort()
    missing = 0
    for n in nums:
        if n != missing:
            return missing
        missing += 1
    return missing
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Modified sum of natural numbers from 1 to n

take advantage of sum(0..n) series formula (a.k.a. triangle numbers)

```text
sum(0..n) = n*(n+1)/2
```

example 1

```text
nums = [3,0,1]
sum(0..len(nums)) = sum(0..3) = 3*(3+1)/2 = 6
sum(nums) = 3+0+1 = 4
6-4 = 2
```

example 2

```text
nums = [0,1]
sum(0..len(nums)) = sum(0..2) = 2*(2+1)/2 = 3
sum(nums) = 0+1 = 1
3-1 = 2
```

code

```python
def missing_number(nums: List[int]) -> int:
    n = len(nums)
    n_sum = (n * (n + 1)) // 2
    return n_sum - sum(nums)
```

Time complexity: $O(n)$
Space complexity: $O(1)$
