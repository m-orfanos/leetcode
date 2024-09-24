---
tags:
- difficulty/easy
- topics/hash-table
- topics/string
- topics/counting
---

# 0383 Ransom Note

<https://leetcode.com/problems/ransom-note>

## Description

- Problem statement
    - Given two strings `ransomNote` and `magazine`, return true if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
    - Each letter in magazine can only be used once in `ransomNote`.
- Constraints
    - $1 <= ransomNote.length, magazine.length <= 10^5$
    - `ransomNote` and `magazine` consist of lowercase English letters.
- Examples
    - Example 1
        - Input: `ransomNote = "a"`, `magazine = "b"`
        - Output: `false`
    - Example 2
        - Input: `ransomNote = "aa"`, `magazine = "ab"`
        - Output: `false`
    - Example 3
        - Input: `ransomNote = "aa"`, `magazine = "aab"`
        - Output: `true`

## Solutions

### Build a histogram

create counter from `magazine`
iterate over `randomNote`
exit if mismatch (false) or when done (true)

```python
def can_construct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine):
        return False
        
    letters = {}
    for ch in magazine:
        letters[ch] = letters.get(ch, 0) + 1
        
    for ch in ransomNote:
        if letters.get(ch, 0) > 0:
            letters[ch] -= 1
        else:
            return False
            
    return True
```

Time complexity: $O(n)$
While we iterate over two string, we are limited by the size of the magazine.

Space complexity: $O(1)$
While we build a map, it's essentially `O(1)` since the map is a histogram of English letters to a count.
