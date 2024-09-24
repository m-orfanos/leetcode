---
tags:
- difficulty/easy
- topics/tree
- topics/depth-first-search
- topics/breadth-first-search
- topics/binary-tree
---

# 0104 Maximum Depth of Binary Tree

<https://leetcode.com/problems/maximum-depth-of-binary-tree>

## Description

- Problem statement
    - Given the root of a binary tree, return its maximum depth.
    - A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
- Constraints
    - The number of nodes in the tree is in the range $[0, 10^4]$.
    - $-100 <= Node.val <= 100$
- Examples
    - Example 1
        - Input: `root = [3,9,20,null,null,15,7]`
        - Output: `3`
    - Example 2
        - Input: `root = [1,null,2]`
        - Output: `2`

## Solutions

### Recursive DFS approach

```python
def depth(root: Optional[TreeNode]) -> int:
    def depth0(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        ld = depth0(node.left)
        rd = depth0(node.right)
        return 1 + max(ld, rd)

    return depth0(root)
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Stack-based iterative DFS approach

```python
def depth(root: Optional[TreeNode]) -> int:
    max_depth = 0
    stack = [(root, 1)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
        max_depth = max(depth, max_depth)
    return max_depth
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Queue-based iterative BFS approach

- Instead of keeping a running `depth`, go level-by-level.

```python
def maximum_depth_binary_tree_bfs(root: Optional[TreeNode]) -> int:
    max_depth = 0
    queue = [root]
    while len(queue) > 0:
        size = len(queue)
        while size > 0:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            size -= 1
        max_depth += 1
    return max_depth
```

Time complexity: $O(n)$
Space complexity: $O(n)$
