---
tags:
- difficulty/easy
- topics/two-pointers
- topics/string
- topics/stack
- topics/simulation
---

# 0844 Backspace String Compare

<https://leetcode.com/problems/backspace-string-compare>

## Description

- Problem statement
    - Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
    - Note that after backspacing an empty text, the text will continue empty.
- Constraints
    - $1 <= s.length, t.length <= 200$
    - `s` and `t` only contain lowercase letters and `'#'` characters.
- Examples
    - Example 1
        - Input: `s = "ab#c"`, `t = "ad#c"`
        - Output: `true`
    - Example 2
        - Input: `s = "ab##"`, `t = "c#d#"`
        - Output: `true`
    - Example 3
        - Input: `s = "a#c"`, `t = "b"`
        - Output: `false`
- Follow up
    - Can you solve it in $O(n)$ time and $O(1)$ space?

## Solutions

### Pre-process and compare

```python
def backspace_string_compare(s: str, t: str) -> bool:
    def cleanup(xs: str):
        ans = []
        for ch in xs:
            if ch == "#":
                if len(ans) > 0:
                    ans.pop()
            else:
                ans.append(ch)
        return "".join(ans)
        
    ss = cleanup(s)
    tt = cleanup(t)
    
    return ss == tt
```

Time complexity: $O(m+n)$
Space complexity: $O(m+n)$

### Single-pass iterative approach

```python
def backspace_string_compare(s: str, t: str) -> bool:
    def next(s: str, i: int) -> int:
        cnt = 0
        while i >= 0:
            if s[i] == "#":
                i -= 1
                cnt += 1
                continue
            if cnt > 0:
                i -= 1
                cnt -= 1
                continue
            return i
        return -1
        
    si = len(s) - 1
    ti = len(t) - 1
    while si >= 0 and ti >= 0:
        si = next(s, si)
        ti = next(t, ti)
        if si < 0 or ti < 0:
            break
        if s[si] != t[ti]:
            return False
        si -= 1
        ti -= 1
        
    if si >= 0 and s[si] == "#":
        si = next(s, si)
    if ti >= 0 and t[ti] == "#":
        ti = next(t, ti)
        
    return si < 0 and ti < 0
```

Time complexity: $O(m+n)$
Space complexity: $O(1)$
