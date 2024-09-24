---
tags:
- difficulty/easy
- topics/linked-list
- topics/recursion
---

# 0021 Merge Two Sorted Lists

<https://leetcode.com/problems/merge-two-sorted-lists>

## Description

- Problem statement
    - You are given the heads of two sorted linked lists `list1` and `list2`.
    - Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    - Return the `head` of the merged linked list.
- Constraints
    - The number of nodes in both lists is in the range `[0, 50]`.
    - $-100 <= Node.val <= 100$
    - Both `list1` and `list2` are sorted in non-decreasing order.
- Examples
    - Example 1
        - Input: $list1 = [1,2,4]$, $list2 = [1,3,4]$
        - Output: $[1,1,2,3,4,4]$
    - Example 2
        - Input: $list1 = []$, $list2 = []$
        - Output: $[]$
    - Example 3
        - Input: $list1 = []$, $list2 = [0]$
        - Output: $[0]$

## Solutions

common code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Solution 1: Traverse linked lists

- traverse the lists simultaneously
- requires a whole lot of linked list pointer bookkeeping…

```python
def merge_two_lists(
        list1: Optional[ListNode], 
        list2: Optional[ListNode]
) -> Optional[ListNode]:
    # create pointers for merged list
    h = None
    p = None
    
    # create 2 pointers, one for each list
    p1 = list1
    p2 = list2
    
    # append list1/list2 values
    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            if h is None:
                p = ListNode(p1.val)
                h = p
            else:
                p.next = ListNode(p1.val)
                p = p.next
            p1 = p1.next
        else:
            if h is None:
                p = ListNode(p2.val)
                h = p
            else:
                p.next = ListNode(p2.val)
                p = p.next
            p2 = p2.next
            
    # list2 is exhausted/empty, append remaining list1 values
    while p1 is not None:
        if h is None:
            p = ListNode(p1.val)
            h = p
        else:
            p.next = ListNode(p1.val)
            p = p.next
        p1 = p1.next
        
    # list1 is exhausted/empty, append remaining list2 values
    while p2 is not None:
        if h is None:
            p = ListNode(p2.val)
            h = p
        else:
            p.next = ListNode(p2.val)
            p = p.next
        p2 = p2.next
        
    return h
```

Time complexity: $O(m+n)$
Space complexity: $O(m+n)$
