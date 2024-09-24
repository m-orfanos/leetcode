---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-tree
- topics/string-matching
- topics/binary-tree
- topics/hash-function
---

# 0572 Sub-tree of Another Tree

<https://leetcode.com/problems/subtree-of-another-tree>

## Description

- Problem statement
    - Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a sub-tree of `root` with the same structure and node values of `subRoot` and `false` otherwise.
    - A sub-tree of a binary `tree` tree is a tree that consists of a node in `tree` and all of this node's descendants. The tree `tree` could also be considered as a sub-tree of itself.
- Constraints
    - The number of nodes in the `root` tree is in the range `[1, 2000]`.
    - The number of nodes in the `subRoot` tree is in the range `[1, 1000]`.
    - $-10^4 <= root.val <= 10^4$
    - $-10^4 <= subRoot.val <= 10^4$
- Examples
    - Example 1
        - Input: `root = [3,4,5,1,2]`, `subRoot = [4,1,2]`
        - Output: `true`
    - Example 2
        - Input: `root = [3,4,5,1,2,null,null,null,null,0]`, `subRoot = [4,1,2]`
        - Output: `false`

## Solutions

### Check equals node-by-node

```python
def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def is_same(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        if h1 is None and h2 is None:
            return True
        elif (h1 is None) or (h2 is None):
            return False
        elif h1.val != h2.val:
            return False
        else:
            return is_same(h1.left, h2.left) and is_same(h1.right, h2.right)
            
    def traverse(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        if h1 is None:
            return False
        if is_same(h1, h2):
            return True
        return traverse(h1.left, h2) or traverse(h1.right, h2)
        
    return traverse(root, subRoot)
```

Time complexity: $O(n*m)$
Space complexity: $O(n)$

### Convert binary tree to array and pattern match #review

Create an array from each tree via DFS.
Apply the [Knuth-Morris-Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) with root as "text" and subtree as "pattern".

example

```text
root
        3
       / \
      4    5
     / \
    1   2

subroot
  4   
 / \
1   2

root = [3,4,1,2,5]
subroot = [4,1,2]
```

code

```python
def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # build array from tree
    def traverse(h: Optional[TreeNode]) -> List[int]:
        s = []
        q = [h]
        
        while q:
            n = q.pop()
            if n is None:
                s.append(None)
                continue
            s.append(n.val)
            q.append(n.left)
            q.append(n.right)
            
        return s
    
    # longest prefix suffix
    def compute_lps(pat: List[int]) -> None:
        lps = [0] * len(pat)
        l = 0
        i = 1
        
        while i < len(pat):
            if pat[i] == pat[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l != 0:
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        return lps
        
    # pattern match
    def kmp_search(pat: List[int], txt: List[int]) -> bool:
        lps = compute_lps(pat)
        plen = len(pat)
        tlen = len(txt)
        i = 0
        j = 0
        
        while (tlen - i) >= (plen - j):
            if pat[j] == txt[i]:
                i += 1
                j += 1
                
            if j == plen:
                return True
                
            if i < tlen and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                    
        return False
        
    return kmp_search(traverse(subRoot), traverse(root))
```

Time complexity: $O(n+m)$
Space complexity: $O(max(n,m))$
