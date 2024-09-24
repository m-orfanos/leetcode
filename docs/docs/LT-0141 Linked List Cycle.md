---
tags:
- difficulty/easy
- topics/hash-table
- topics/linked-list
- topics/two-pointers
---

# 0141 Linked List Cycle

<https://leetcode.com/problems/linked-list-cycle>

## Description

- Problem statement
    - Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
    - There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. Note that `pos` is not passed as a parameter.
    - Return `true` if there is a cycle in the linked list. Otherwise, return `false`.
- Constraints
    - The number of the nodes in the list is in the range $[0, 10^4]$.
    - $-10^5 <= Node.val <= 10^5$
    - `pos` is `-1` or a valid index in the linked-list.
- Examples
    - Example 1
        - Input: `head = [3,2,0,-4]`, `pos = 1`
        - Output: `true`
    - Example 2
        - Input: `head = [1,2]`, `pos = 0`
        - Output: `true`
    - Example 3
        - Input: `head = [1]`, `pos = -1`
        - Output: `false`
- Follow up
    - Can you solve it using $O(1)$ (i.e. constant) memory?

## Solutions

### Floyd's Tortoise and hare

Traverse the linked list with 1 "slow" pointer and 1 "fast" pointer. They will either reach the end of the list or eventually the "fast" pointer will intersect with "slow".

<https://en.wikipedia.org/wiki/Cycle_detection#Floyd>'s_tortoise_and_hare>

slow = traverse 1 node at a time
fast = traverse 2 nodes at a time

```python
def has_cycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow and fast and slow is not fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return slow is fast
```

Time complexity: $O(n)$
Space complexity: $O(1)$

### Store visited nodes

Traverse the linked list, storing each node (reference) into a set. When visiting a node, check if node is already present in the set.

Time complexity: $O(n)$
Space complexity: $O(n)$

### Add a flag to visited nodes

Traverse the linked list mutating the node each time adding a "visited" flag. Either the end of the list will be reached or a node with "visited" will be found. Some care needs to be taken when choosing a flag.

Time complexity: $O(n)$
Space complexity: $O(n)$
