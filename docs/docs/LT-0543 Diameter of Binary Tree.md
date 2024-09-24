---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-search
- topics/binary-tree
---

# 0543 Diameter of Binary Tree

<https://leetcode.com/problems/diameter-of-binary-tree>

## Description

- Problem statement
    - Given the `root` of a binary tree, return the length of the diameter of the tree.
        - The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the `root`.
        - The length of a path between two nodes is represented by the number of edges between them.
- Constraints
    - The number of nodes in the tree is in the range $[1, 10^4]$.
    - $-100 <= Node.val <= 100$
- Examples
    - Example 1
        - Input: `root = [1,2,3,4,5]`
        - Output: `3`
    - Example 2
        - Input: `root = [1,2]`
        - Output: `1`

## Solutions

### DFS approach

- Reminder: The height of a node is the number of edges present in the longest path connecting that node to a leaf node.

```python
def diameter_binary_tree(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return (0, 0)
            
        lh, ld = dfs(node.left)
        rh, rd = dfs(node.right)
        
        height = 1 + max(lh, rh)
        diameter = max(lh + rh, ld, rd)
        
        return (height, diameter)
        
    return dfs(root)[1]
```

Time complexity: $O(n)$
Space complexity: $O(n)$
