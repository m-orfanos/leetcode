---
tags:
- difficulty/easy
- topics/linked-list
- topics/recursion
---

# 0206 Reverse Linked List

<https://leetcode.com/problems/reverse-linked-list>

## Description

- Problem statement
    - Given the `head` of a singly linked list, reverse the list, and return the reversed list.
- Constraints
    - The number of nodes in the list is the range `[0, 5000]`.
    - $-5000 <= Node.val <= 5000$
- Examples
    - Example 1
        - Input: `head = [1,2,3,4,5]`
        - Output: `[5,4,3,2,1]`
    - Example 2
        - Input: `head = [1,2]`
        - Output: `[2,1]`
    - Example 3
        - Input: `head = []`
        - Output: `[]`
- Follow up
    - A linked list can be reversed either iteratively or recursively. Could you implement both?

## Solutions

### Iterative approach

mostly pointer bookkeeping

- traverse the list
- when visit a node
    - store node's tail into variable
    - make node point to the new head of the new list
    - update head new list
    - update head old list
    - continue traverse

```text
l1  1 -> 2 -> 3 -> 4 -> 5
l2  x

l1  2 -> 3 -> 4 -> 5
l2  1

l1  3 -> 4 -> 5
l2  2 -> 1

l1  4 -> 5
l2  3 -> 2 -> 1

l1  5
l2  4 -> 3 -> 2 -> 1

l1  x
l2  5 -> 4 -> 3 -> 2 -> 1

DONE!
```

code

```typescript
function reverse_linked_list(head: ListNode | null): ListNode | null {
    let l1: ListNode | null = head;
    let l2: ListNode | null = null;
    
    while (l1 != null) {
        const l1_tail = l1.next;
        l1.next = l2;
        l2 = l1;
        l1 = l1_tail;
    }
    
    return l2;
}
```

Time complexity: $O(n)$
Space complexity: $O(1)$

### Recursive approach

same as above but use functions instead (with worse space complexity)

```typescript
function reverse_linked_list(head: ListNode | null): ListNode | null {
    function reverse(l1: ListNode | null, l2: ListNode | null) {
        if (l1 == null) {
            return l2;
        }
        const l1_tail = l1.next;
        l1.next = l2;
        l2 = l1;
        return reverse(l1_tail, l2);
    }
    return reverse(head, null);
}
```

Time complexity: $O(n)$
Space complexity: $O(n)$
