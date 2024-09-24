---
tags:
- difficulty/easy
- topics/linked-list
- topics/two-pointers
---

# 0876 Middle of the Linked List

<https://leetcode.com/problems/middle-of-the-linked-list>

## Description

- Problem statement
    - Given the `head` of a singly linked list, return the middle node of the linked list.
    - If there are two middle nodes, return the second middle node.
- Constraints
    - The number of nodes in the list is in the range `[1, 100]`.
    - $1 <= Node.val <= 100$
- Examples
    - Example 1
        - Input: `head = [1,2,3,4,5]`
        - Output: `[3,4,5]`
    - Example 2
        - Input: `head = [1,2,3,4,5,6]`
        - Output: `[4,5,6]`

## Solutions

### Recursive 2 pass approach - compute length and return middle

```python
def middle_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    def length(node: Optional[ListNode], curr=0) -> int:
        if not node:
            return curr
        return length(node.next, curr + 1)
        
    def get(node: Optional[ListNode], idx) -> Optional[ListNode]:
        if not node or idx < 0:
            return None
        if idx == 0:
            return node
        return get(node.next, idx - 1)
        
    return get(head, length(head) // 2)
```

Time complexity: $O(n)$
Space complexity: $O(n)$

### Tortoise and hare approach

traverse list with 1 slow and 1 fast
when fast is done, return slow

example: 1 -> 2 -> 3 -> 4 -> 5

|  i  |  1  |  2  |  3  |  4  |  5  |
| :-: | :-: | :-: | :-: | :-: | :-: |
|  0  |  S  |  F  |     |     |     |
|  1  |     |  S  |     |  F  |     |
|  2  |     |     |  S  |     |     |

S: 3 -> 4 -> 5

example: 1 -> 2 -> 3 -> 4 -> 5 -> 6

|  i  |  1  |  2  |  3  |  4  |  5  |  6  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|  0  |  S  |  F  |     |     |     |     |
|  1  |     |  S  |     |  F  |     |     |
|  2  |     |     |  S  |     |     |  F  |
|  3  |     |     |     |  S  |     |     |

S: 4 -> 5 -> 6

```python
def middle_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

Time complexity: $O(n)$
Space complexity: $O(1)$
