---
tags:
- difficulty/easy
- topics/array
- topics/divide-and-conquer
- topics/tree
- topics/binary-search-tree
- topics/binary-tree
---

# 0108 Convert Sorted Array to Binary Search

<https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree>

## Description

- Problem statement
    - Given an integer array `nums` where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    - A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
- Constraints:
    - $1 <= nums.length <= 10^4$
    - $-10^4 <= nums[i] <= 10^4$
    - $nums$ is sorted in a strictly increasing order.
- Examples
    - Example 1
        - Input: `nums = [-10,-3,0,5,9]`
        - Output: `[0,-3,9,-10,null,5]`
    - Example 2
        - Input: `nums = [1,3]`
        - Output: `[3,1]`

## Solutions

### Modified binary search approach with recursion

```python
def sorted_array_to_binary_search_tree(nums: List[int]) -> Optional[TreeNode]:
    # 1,2,3
    # 1,2,3,4
    def traverse(nums, low, high) -> Optional[TreeNode]:
        if low > high:
            return None
        mid = low + (high - low) // 2
        left = traverse(nums, low, mid - 1)
        right = traverse(nums, mid + 1, high)
        return TreeNode(nums[mid], left, right)
        
    return traverse(nums, 0, len(nums) - 1)
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Queue-based approach

This is essentially the same approach as above but it uses a queue instead.

```python
def sorted_array_to_binary_search_tree(nums: List[int]) -> Optional[TreeNode]:
    if len(nums) == 0:
        return None
        
    low = 0
    high = len(nums) - 1
    mid = low + (high - low) // 2
    
    root = TreeNode(nums[mid])
    
    q = [(root, low, mid, high)]
    while q:
        curr, lhs, mid, rhs = q.pop(0)
        if curr is None:
            continue
            
        # lhs
        if lhs <= mid - 1:
            lmid = lhs + (mid - 1 - lhs) // 2
            curr.left = TreeNode(nums[lmid])
            q.append((curr.left, lhs, lmid, mid - 1))
            
        # rhs
        if mid + 1 <= rhs:
            rmid = mid + 1 + (rhs - (mid + 1)) // 2
            curr.right = TreeNode(nums[rmid])
            q.append((curr.right, mid + 1, rmid, rhs))
            
    return root
```

Time complexity: $O(n)$
Space complexity: $O(n)$
