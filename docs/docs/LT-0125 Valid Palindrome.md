---
tags:
- difficulty/easy
- topics/two-pointers
- topics/string
---

# 0125 Valid Palindrome

<https://leetcode.com/problems/valid-palindrome>

## Description

- Problem description
    - Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.
    - A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
    - Alphanumeric characters include letters and numbers.
- Constraints
    - $1 <= s.length <= 2 * 10^5$
    - `s` consists only of printable ASCII characters.
- Examples
    - Example 1
        - Input: `s = "A man, a plan, a canal: Panama"`
        - Output: `true`
    - Example 2
        - Input: `s = "race a car"`
        - Output: `false`
    - Example 3
        - Input: `s = " "`
        - Output: `true`

## Solutions

### Escape, reverse and check

```python
def is_palindrome(s: str) -> bool:
    t = [ch.lower() for ch in s if ch.isalnum()]
    return t == t[::-1]
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Single-pass, two-pointers

```python
def is_palindrome(s: str) -> bool:
    lhs = 0
    rhs = len(s) - 1
    
    while lhs <= rhs:
        if not s[lhs].isalnum():
            lhs += 1
            continue
        if not s[rhs].isalnum():
            rhs -= 1
            continue
        if s[lhs].lower() != s[rhs].lower():
            return False
        lhs += 1
        rhs -= 1
        
    return True
```

Time complexity: $O(n)$
Space complexity: $O(1)$
