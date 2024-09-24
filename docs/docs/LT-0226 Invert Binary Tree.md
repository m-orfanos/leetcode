---
tags:
- difficulty/easy
- topics/depth-first-search
- topics/breadth-first-search
- topics/binary-tree
---

# 0226 Invert Binary Tree

<https://leetcode.com/problems/invert-binary-tree>

## Description

- Problem statement
    - Given the root of a binary tree, invert the tree, and return its root.
- Constraints
    - The number of nodes in the tree is in the range `[0, 100]`.
    - $-100 <= Node.val <= 100$
- Examples
    - Example 1
        - Input: `root = [4,2,7,1,3,6,9]`
        - Output: `[4,7,2,9,6,3,1]`
    - Example 2
        - Input: `root = [2,1,3]`
        - Output: `[2,3,1]`
    - Example 3
        - Input: `root = []`
        - Output: `[]`

## Solutions

### Recursive approach

- traverse the tree using DFS
- when visiting a node, swap its leaves

```python
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if node is None:
            return None
            
        # swap tree nodes
        temp = node.left
        node.left = node.right
        node.right = temp
        
        # traverse
        dfs(node.left)
        dfs(node.right)
        
        return node
        
    return dfs(root)
```

Time complexity: $O(n)$
tree traversal

Space complexity: $O(n)$
function call stack

### Stack approach

Same as above, but uses a stack/loop instead of recursion.

```python
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    s = [root]
    while s:
        n = s.pop()
        
        # base case
        if n is None:
            continue
            
        # swap
        tmp = n.left
        n.left = n.right
        n.right = tmp
        
        # traverse
        s.append(n.left)
        s.append(n.right)
        
    return root
```

Time complexity: $O(n)$
Space complexity: $O(n)$
