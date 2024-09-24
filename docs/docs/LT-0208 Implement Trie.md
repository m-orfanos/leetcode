---
tags:
- difficulty/medium
- topics/hash-table
- topics/string
- topics/design
- topics/trie
---

# 0208 Implement Trie

<https://leetcode.com/problems/implement-trie-prefix-tree>

## Description

- Problem statement
    - A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
    - Implement the Trie class:
        - `Trie()`
            - Initialises the trie object.
        - `void insert(String word)`
            - Inserts the string `word` into the trie.
        - `boolean search(String word)`
            - Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
        - `boolean startsWith(String prefix)`
            - Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
- Constraints
    - $1 <= word.length$, $prefix.length <= 2000$
    - `word` and `prefix` consist only of lowercase English letters.
    - At most $3*10^4$ calls in total will be made to `insert`, `search`, and `startsWith`.

## Solutions

### Use a graph

one node = one letter
use a marker to denote a word (below an integer)

```python
class Trie:
    
    def __init__(self):
        self.g = [-1, {}]
        self.n = 0
        
    def insert(self, word: str) -> None:
        """
        Time complexity: O(k)
        Space complexity: O(k)
        """
        if len(word) <= 0:
            return
            
        curr = self.g
        for ch in word:
            _, d = curr
            if ch not in d:
                d[ch] = [-1, {}]
            curr = d[ch]
            
        v, _ = curr
        if v < 0:
            curr[0] = self.n
            self.n += 1
            
    def search(self, word: str) -> bool:
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """
        curr = self.g
        for ch in word:
            _, d = curr
            if ch not in d:
                return False
            curr = d[ch]
            
        v, _ = curr
        return v >= 0
        
    def startsWith(self, prefix: str) -> bool:
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """
        curr = self.g
        for ch in prefix:
            _, d = curr
            if ch not in d:
                return False
            curr = d[ch]
            
        return True
```
