---
tags:
- difficulty/easy
- topics/array
- topics/bit-manipulation
---

# 0136 Single Number

<https://leetcode.com/problems/single-number>

## Description

- Problem statement
    - Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one.
    - You must implement a solution with a linear runtime complexity and use only constant extra space.
- Constraints:
    - $1 <= nums.length <= 3 * 10^4$
    - $-3 * 10^4 <= nums[i] <= 3 * 10^4$
    - Each element in the array appears twice except for one element which appears only once.
- Examples
    - Example 1
        - Input: `nums = [2,2,1]`
        - Output: `1`
    - Example 2
        - Input: `nums = [4,1,2,1,2]`
        - Output: `4`
    - Example 3
        - Input: `nums = [1]`
        - Output: `1`

## Solutions

### Build a histogram

```python
def single_number(xs: List[int]) -> int:
    hist = {}
    for x in xs:
        hist[x] = 1 + hist.get(x, 0)
        
    for k, cnt in hist.items():
        if cnt == 1:
            return k
            
    raise ValueError("List is empty")
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Bit twiddling

invoke some bit manipulation magic…

```text
1 ^ 1 ^ 2 = 2
1 ^ 2 ^ 1 = 2
2 ^ 1 ^ 1 = 2

0b01 ^ 0b10 = 1 ^ 2 = 3
0b11 ^ 0b01 = 3 ^ 1 = 2
```

code

```python
def single_number(xs: List[int]) -> int:
    ans = 0
    for x in xs:
        ans ^= x
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(1)$
