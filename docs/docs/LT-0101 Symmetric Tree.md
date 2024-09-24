---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-search
- topics/breadth-first-search
- topics/binary-tree
---

# 0101 Symmetric Tree

<https://leetcode.com/problems/symmetric-tree>

## Description

- Problem statement
    - Given the `root` of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its centre).
- Constraints
    - The number of nodes in the tree is in the range $[1, 1000]$.
    - $-100 <= Node.val <= 100$
- Examples
    - Example 1
        - Input: `root = [1,2,2,3,4,4,3]`
        - Output: `true`
    - Example 2
        - Input: `root = [1,2,2,null,3,null,3]`
        - Output: `false`
- Follow up
    - Could you solve it both recursively and iteratively?

## Solutions

### Modified recursive DFS approach

```python
def is_symmetric(root: Optional[TreeNode]) -> bool:
    def traverse(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None or n1.val != n2.val:
            return False
        return traverse(n1.left, n2.right) and traverse(n1.right, n2.left)
        
    return traverse(root.left, root.right)
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Modified queue-based BFS approach

```python
def is_symmetric1(root: Optional[TreeNode]) -> bool:
    q = [root.left, root.right]
    while q:
        n1 = q.pop(0)
        n2 = q.pop(0)
        
        if n1 is None and n2 is None:
            continue
        if n1 is None or n2 is None or n1.val != n2.val:
            return False
            
        q.append(n1.left)
        q.append(n2.right)
        q.append(n1.right)
        q.append(n2.left)
        
    return True
```

Time complexity: $O(n)$
Space complexity: $O(n)$
