---
tags:
- difficulty/easy
- topics/math
---

# 0009 Palindrome Number

<https://leetcode.com/problems/palindrome-number>

## Description

- Problem statement
    - Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.
    - An integer is a palindrome when it reads the same forward and backward.
- Constraints
    - $-2^{31} <= x <= 2^{31} - 1$
- Examples
    - Example 1
        - Input: `x = 121`
        - Output: `true`
    - Example 2
        - Input: `x = -121`
        - Output: `false`
    - Example 3
        - Input: `x = 10`
        - Output: `false`
- Follow up
    - Could you solve it without converting the integer to a string?

## Solutions

### Reverse and compare

```python
def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    rev = 0
    copy = x
    while copy > 0:
        rev = 10 * rev + copy % 10
        copy //= 10
    return x == rev
```

Time complexity: $O(n)$
Space complexity: $O(1)$

### Reverse half and compare

```python
def is_palindrome1(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        # ignore all negative numbers
        # ignore all numbers ending with 0, except 0 itself
        return False
        
    # even-length numbers
    #        x  rev
    # 12344321    0
    #  1234432    1
    #   123443   12
    #    12344  123
    #     1234 1234 <-- compare directly
    #
    # odd-length numbers
    #     x   rev
    # 12321     0
    #  1232     1
    #   123    12
    #    12   123 <-- drop last digit
    rev = 0
    while rev < x:
        rev = 10 * rev + x % 10
        x //= 10
    return x == rev or x == rev // 10
```

Time complexity: $O(n)$
Space complexity: $O(1)$
