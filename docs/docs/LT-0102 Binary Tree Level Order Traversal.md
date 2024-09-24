---
tags:
- difficulty/medium
- topics/tree
- topics/breadth-first-search
- topics/binary-tree
---

# 0102 Binary Tree Level Order Traversal

<https://leetcode.com/problems/binary-tree-level-order-traversal>

## Description

- Problem statement
    - Given the `root` of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
- Constraints
    - The number of nodes in the tree is in the range $[0, 2000]$.
    - $-1000 <= Node.val <= 1000$
- Examples
    - Example 1
        - Input: $root = [3,9,20,null,null,15,7]$
        - Output: $[[3],[9,20],[15,7]]$
    - Example 2
        - Input: $root = [1]$
        - Output: $[ [1] ]$
    - Example 3
        - Input: $root = []$
        - Output: $[]$

## Solutions

### Iterative level order traversal

```python
def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
        
    q = deque()
    q.append((root, 0))
    
    ans = []
    tmp = []
    curr = 0
    while q:
        n, level = q.popleft()
        
        if curr != level:
            ans.append(tmp)
            tmp = []
            curr += 1
            
        tmp.append(n.val)
        
        if n.left:
            q.append((n.left, level + 1))
        if n.right:
            q.append((n.right, level + 1))
            
    if len(tmp) > 0:
        ans.append(tmp)
        
    return ans
```

Time complexity: $O(n)$
Space complexity: $O(n)$
