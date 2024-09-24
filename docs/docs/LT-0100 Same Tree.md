---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-search
- topics/breadth-first-search
- topics/binary-tree
---

# 0100 Same Tree

<https://leetcode.com/problems/same-tree>

## Description

- Problem statement
    - Given the roots of two binary trees `p` and `q`, write a function to check if they are the same or not.
    - Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
- Constraints
    - The number of nodes in both trees is in the range `[0, 100]`.
    - $-10^4 <= Node.val <= 10^4$
- Examples
    - Example `1`
        - Input: `p = [1,2,3]`, `q = [1,2,3]`
        - Output: `true`
    - Example 2
        - Input: `p = [1,2]`, `q = [1,null,2]`
        - Output: `false`
    - Example 3
        - Input: `p = [1,2,1]`, `q = [1,1,2]`
        - Output: `false`

## Solutions

### Recursive modified DFS

```python
def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    elif p is None or q is None or p.val != q.val:
        return False
    else:
        lhs = same_tree(p.left, q.left)
        rhs = same_tree(p.right, q.right)
        return lhs and rhs
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Stack-based DFS approach

```python
def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # given two trees with elements...
    stk = [p, q]
    
    while len(stk) > 0:
        pn = stk.pop()
        qn = stk.pop()
        
        if pn is None and qn is None:
            continue
            
        if pn is None or qn is None or pn.val != qn.val:
            return False
            
        # the insertion order is important
        stk.append(pn.left)
        stk.append(qn.left)
        stk.append(pn.right)
        stk.append(qn.right)
        
    return True
```

Time complexity: $O(n)$
Space complexity: $O(n)$
