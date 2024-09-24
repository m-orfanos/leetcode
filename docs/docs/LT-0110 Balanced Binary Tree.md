---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-search
- topics/binary-tree
---

# 0110 Balanced Binary Tree

<https://leetcode.com/problems/balanced-binary-tree>

## Description

- Problem statement
    - Given a binary tree, determine if it is height-balanced.
    - A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
- Constraints
    - The number of nodes in the tree is in the range `[0, 5000]`.
    - $-10^4 <= Node.val <= 10^4$
- Examples
    - Example 1
        - Input: `root = [3,9,20,null,null,15,7]`
        - Output: `true`
    - Example 2
        - Input: `root = [1,2,2,3,3,null,null,4,4]`
        - Output: `false`
    - Example 3
        - Input: `root = []`
        - Output: `true`

## Solutions

### Modified DFS

```python
def is_balanced(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode]) -> int:
        # base case
        if node is None:
            return 0
            
        # depth-first traversal
        dl = dfs(node.left)
        dr = dfs(node.right)
        
        # short-circuit
        if dl == -1 or dr == -1 or abs(dl - dr) > 1:
            return -1
            
        # accumulator
        return 1 + max(dl, dr)
        
    return is_balanced0(root) != -1
```

Time complexity: $O(n)$
Space complexity: $O(n)$
