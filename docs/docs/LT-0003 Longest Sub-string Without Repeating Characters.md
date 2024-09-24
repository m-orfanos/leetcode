---
tags:
- difficulty/medium
- topics/hash-table
- topics/string
- topics/sliding-window
---

# 0003 Longest Sub-string Without Repeating Characters

<https://leetcode.com/problems/longest-substring-without-repeating-characters>

## Description

- Problem statement
    - Given a string $s$, find the length of the longest substring without repeating characters.
- Constraints
    - $0 <= s.length <= 5*10^4$
    - $s$ consists of English letters, digits, symbols and spaces.
- Examples
    - Example 1
        - Input: `s = "abcabcbb"`
        - Output: `3`
    - Example 2
        - Input: `s = "bbbbb"`
        - Output: `1`
    - Example 3
        - Input: `s = "pwwkew"`
        - Output: `3`

## Solutions

### Modified sliding window

Use a window (list) and cache (map) to store the sub-string.
Add characters to both until a repeat is hit.
Before a repeat is added, shrink the window/cache to the previous char before adding it.

```python
def longest_substring(s: str) -> int:
    best = 0
    curr = deque()
    d = {}
    for i, ch in enumerate(s):
        while ch in d:
            d.pop(curr.popleft())
            
        d[ch] = i
        curr.append(ch)
        
        best = max(len(curr), best)
        
    return best
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Maintain a visited list

A list is used to keep track of character indices.
An additional variable, `left`, is used to reflect the index of the first character in the "window".
All characters before `left` can be ignored when calculating the new sub-string.
When processing a character, either "add it to the window" or a repeated is found.

```python
def longest_substring(s: str) -> int:
    letters = [-1] * 128
    
    best = 0
    left = 0
    for i, ch in enumerate(s):
        if letters[ord(ch)] >= left:
            left = letters[ord(ch)] + 1
        else:
            best = max(best, i - left + 1)
        letters[ord(ch)] = i
        
    return best
```

Time complexity: $O(n)$
Space complexity: $O(1)$
