---
tags:
- difficulty/easy
- topics/linked-list
- topics/two-pointers
- topics/stack
- topics/recursion
---

# 0234 Palindrome Linked List

<https://leetcode.com/problems/palindrome-linked-list>

## Description

- Problem statement
    - Given the `head` of a singly linked list, return `true` if it is a palindrome or `false` otherwise.
    - A palindrome is a sequence that reads the same forward and backward.
- Constraints
    - The number of nodes in the list is in the range $[1, 10^5]$.
    - $0 <= Node.val <= 9$
- Examples
    - Example 1
        - Input: `head = [1,2,2,1]`
        - Output: `true`
    - Example 2
        - Input: `head = [1,2]`
        - Output: `false`
- Follow up
    - Could you do it in $O(n)$ time and $O(1)$ space?

## Solutions

### Straight-forward reverse and compare

```python
def is_palindrome(head: Optional[ListNode]) -> bool:
    def equals(
        n1: Optional[ListNode], 
        n2: Optional[ListNode],
    ) -> bool:
        if n1 is None and n2 is None:
            return True
        return n1.val == n2.val and equals(n1.next, n2.next)
        
    def reverse(
        n1: Optional[ListNode], 
        n2: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        if n1 is None:
            return n2
        return reverse(n1.next, ListNode(n1.val, n2))
        
    return equals(head, reverse(head))
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Stack-based reverse and compare

build reverse until midpoint using fast & slow approach
reverse is stored as a stack
compare node by node

```python
def is_palindrome(head: Optional[ListNode]) -> bool:
    stack = []
    slow = head
    fast = head
    while slow and fast:
        if fast.next is None:
            # list has odd-length, skips middle element
            slow = slow.next
            break
        fast = fast.next.next

        stack.append(slow.val)
        slow = slow.next

    while slow:
        n1 = slow.val
        n2 = stack.pop()
        if n1 != n2:
            return False
        slow = slow.next

    return True
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Two pointer fast and slow approach

build reverse until midpoint using fast & slow approach
reverse is a linked list built from the original list

```python
def is_palindrome(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    rev = None
    while slow and fast:
        if fast.next is None:
            # list has odd-length, skips middle element
            slow = slow.next
            break
        fast = fast.next.next
        
        # head will point to the tail once done
        # append to rev
        tmp = slow.next
        slow.next = rev
        rev = slow
        slow = tmp
        
    while rev:
        if slow.val != rev.val:
            return False
        slow = slow.next
        rev = rev.next
        
    return True
```

Time complexity: $O(n)$
Space complexity: $O(1)$
