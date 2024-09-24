---
tags:
- difficulty/easy
- topics/hash-table
- topics/string
- topics/greedy
---

# 0409 Longest Palindrome

<https://leetcode.com/problems/longest-palindrome>

## Description

- Problem statement
    - Given a string `s` which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
    - Letters are case sensitive, for example, `"Aa"` is not considered a palindrome here.
- Constraints
    - $1 <= s.length <= 2000$
    - `s` consists of lowercase and/or uppercase English letters only.
- Examples
    - Example 1
        - Input: `s = "abccccdd"`
        - Output: `7`
    - Example 2
        - Input: `s = "a"`
        - Output: `1`

## Solutions

### Build a histogram

create a map counter all the letters `{ch:cnt}`
the highest odd count is the centre of the palindrome
all other letters (both odd/even counts) get halved and tacked onto the sides
counts of 1 are ignored

Note: the palindrome doesn't need to be built: we can simply sum up the counts (with a bit of added bookkeeping to keep track off the largest odd count).

```python
def longest_palindrome(s: str) -> int:
    d = {}
    for ch in s:
        d[ch] = 1 + d.get(ch, 0)
        
    ans = 0
    has_odd = False
    for ch in d.keys():
        nb = d[ch]
        if nb % 2 == 1:
            ans += nb - 1
            has_odd = True
        else:
            ans += nb
            
    if has_odd:
        ans += 1
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(1)$
