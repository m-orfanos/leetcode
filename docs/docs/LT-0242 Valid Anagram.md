---
tags:
- difficulty/easy
- topics/hash-table
- topics/string
- topics/sorting
---

# 0242 Valid Anagram

<https://leetcode.com/problems/valid-anagram>

## Description

- Problem statement
    - Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
    - An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
- Constraints
    - $1 <= s.length, t.length <= 5 * 10^4$
    - `s` and `t` consist of lowercase English letters.
- Follow up
    - What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
    - Note: This only applies to languages that do not support Unicode strings OOTB… we don't use those :))
- Examples
    - Example 1
        - Input: `s = "anagram"`, `t = "nagaram"`
        - Output: `true`
    - Example 2
        - Input: `s = "rat"`, `t = "car"`
        - Output: `false`

## Solutions

### Sort and compare

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)
```

Time complexity: $O(n*log(n))$
Space complexity: $O(n)$

### Build a histogram

```python
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    d = defaultdict(int)
    for i in range(len(s)):
        d[s[i]] += 1
        d[t[i]] -= 1
        
    return all(map(lambda x: x == 0, d.values()))
```

Time complexity: $O(n)$
Space complexity: $O(n)$
