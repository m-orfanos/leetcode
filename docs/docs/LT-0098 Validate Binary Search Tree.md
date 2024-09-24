---
tags:
- difficulty/medium
- topics/tree
- topics/depth-first-search
- topics/binary-search-tree
- topics/binary-tree
---

# 0098 Validate Binary Search Tree

<https://leetcode.com/problems/validate-binary-search-tree>

## Description

- Problem statement
    - Given the `root` of a binary tree, determine if it is a valid binary search tree (BST).
    - A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be binary search trees.
- Constraints
    - The number of nodes in the tree is in the range $[1, 104]$.
    - $-2^{31} <= Node.val <= 2^{31} - 1$
- Examples
    - Example 1
        - Input: $root = [2,1,3]$
        - Output: $true$
    - Example 2
        - Input: $root = [5,1,4,null,null,3,6]$
        - Output: $false$

## Solutions

### Ancestry-list approach

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    LHS = 0
    RHS = 1
    
    def dfs(node: Optional[TreeNode], ancestry: List[int]) -> bool:
        if not node:
            return True
            
        for cmp, ancestor in ancestry:
            if cmp == LHS and node.val >= ancestor:
                return False
            if cmp == RHS and node.val <= ancestor:
                return False
                
        l = ancestry[:]
        l.append((LHS, node.val))
        
        r = ancestry[:]
        r.append((RHS, node.val))
        
        return dfs(node.left, l) and dfs(node.right, r)
        
    return dfs(root, [])
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Split ancestry-list approach

Similar to above approach, except the LHS/RHS are partitioned into separate collections.

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode], lhs: List[int], rhs: List[int]) -> bool:
        if not node:
            return True
            
        for l in lhs:
            if node.val >= l:
                return False
        for r in rhs:
            if node.val <= r:
                return False
                
        clhs = lhs[:]
        clhs.append(node.val)
        
        crhs = rhs[:]
        crhs.append(node.val)
        
        return dfs(node.left, clhs, rhs) and dfs(node.right, lhs, crhs)
        
    return dfs(root, [], [])
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Recursive DFS approach

Extension of previous solution.

The ancestry lists aren't required since at every recursive we know the min/max values and what direction to travel next.

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def dfs(node: Optional[TreeNode], cmin: int, cmax: int) -> bool:
        if not node:
            return True
        if cmin <= node.val or node.val <= cmax:
            return False
        return dfs(node.left, node.val, cmax) and dfs(node.right, cmin, node.val)
        
    return dfs(root, 2**63 - 1, -(2**63) + 1)
```

Time complexity: $O(n)$
Space complexity: $O(n)$
