---
tags:
- difficulty/easy
- topics/string
- topics/trie
---

# 0014 Longest Common Prefix

<https://leetcode.com/problems/longest-common-prefix>

## Description

- Problem statement
    - Write a function to find the longest common prefix string amongst an array of strings.
    - If there is no common prefix, return an empty string `""`.
- Constraints
    - $1 <= strs.length <= 200$
    - $0 <= strs[i].length <= 200$
    - `strs[i]` consists of only lowercase English letters.
- Examples
    - Example 1
        - Input: `strs = ["flower","flow","flight"]`
        - Output: `"fl"`
    - Example 2
        - Input: `strs = ["dog","racecar","car"]`
        - Output: `""`

## Solutions

### Compare characters by taking a vertical slice

```python
def longest_common_prefix(ws: List[str]) -> str:
    if len(ws) == 0:
        return ""
        
    # length of shortest word
    l = min(map(len, ws))

    for k in range(l):
        ch = ws[0][k]
        for i in range(1, len(ws)):
            w = ws[i]
            if ch != w[k]:
                return ws[0][:k]
                
    # occurs when ws has only 1 element or
    # when all elements are the empty string
    return ws[0][:l]
```

Time complexity: $O(kn)$
Space complexity: $O(k)$

where

- `n` is the number of words, and
- `k` is the length of the shortest word

### Sort and compare first/last

```python
def longest_common_prefix(ws: List[str]) -> str:
    if len(ws) == 0:
        return ""
        
    if len(ws) == 1:
        return ws[0]
        
    # sort string alphabetically
    ws = sorted(ws)
    word1 = ws[0]
    word2 = ws[-1]
    
    # compare only the first and last words
    ans = ""
    l = min(len(word1), len(word2))
    for i in range(l):
        if word1[i] != word2[i]:
            break
        ans += word1[i]
        
    return ans
```

Time complexity: $O(k*n*log(n))$
The sort is $O(n*log(n))$ but each comparison in the sort is $O(k)$…

Space complexity: $O(kn)$

where

- `n` is the number of words, and
- `k` is the length of the shortest word
