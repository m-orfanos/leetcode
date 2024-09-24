---
tags:
- difficulty/medium
- topics/tree
- topics/depth-first-search
- topics/binary-search-tree
- topics/binary-tree
---

# 0235 Lowest Common Ancestor of a Binary Search Tree

<https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree>

## Description

- Problem statement
    - Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
    - The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in `T` that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).
- Constraints
    - The number of nodes in the tree is in the range `[2, 105]`.
    - $-10^9 <= Node.val <= 10^9$
    - All Node.val are unique.
    - `p != q`
    - `p` and `q` will exist in the BST
- Examples
    - Example 1
        - Input: `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 8`
        - Output: `6`
    - Example 2
        - Input: `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 4`
        - Output: `2`
    - Example 3
        - Input: `root = [2,1]`, `p = 2`, `q = 1`
        - Output: `2`

## Solutions

Common code

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Build an ancestry list

- build an ancestry list for each node
- iterate over the ancestries until a mismatch is found

```python
def lca(
    root: TreeNode, 
    p: TreeNode, 
    q: TreeNode
) -> TreeNode:
    def find_ancestors(root: TreeNode, node: TreeNode) -> List[int]:
        ancestors = []
        curr = root
        while curr:
            ancestors.append(curr.val)
            if curr.val > node.val:
                curr = curr.left
            elif curr.val < node.val:
                curr = curr.right
            else:
                break
        return ancestors
        
    # build ancestry lists
    ancestors_p = find_ancestors(root, p)
    ancestors_q = find_ancestors(root, q)
    
    # traverse ancestries until a mismatch is found
    l = min(len(ancestors_p), len(ancestors_q))
    for i in range(l):
        if ancestors_p[i] == ancestors_q[i]:
            ancestor = ancestors_p[i]
        else:
            break
            
    return TreeNode(ancestor)
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Take advantage of the BST structure

- take advantage of the BST structure
- if p < q, then the LCA must be in the LHS of the current node.
- otherwise it must be on the RHS.

```python
def lca(
    root: TreeNode, 
    p: TreeNode, 
    q: TreeNode
) -> TreeNode:
    node = root
    while node:
        if p.val < node.val > q.val:
            node = node.left
        elif p.val > node.val < q.val:
            node = node.right
        else:
            return node
```

Time complexity: $O(n)$
Space complexity: $O(1)$
