import unittest
from typing import Optional

from shared.linked_list import ListNode, to_list_node


def is_palindrome0(head: Optional[ListNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def equals(n1: Optional[ListNode], n2: Optional[ListNode]) -> bool:
        if n1 is None and n2 is None:
            return True
        return n1.val == n2.val and equals(n1.next, n2.next)

    def reverse(
        n1: Optional[ListNode], n2: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        # does NOT mutate the original list
        # object creation in python is REALLY REALLY REALLY slow...
        # the statement `ListNode(n1.val, n2)` takes relatively forever...
        if n1 is None:
            return n2
        return reverse(n1.next, ListNode(n1.val, n2))

    reversed = reverse(head)

    return equals(head, reversed)


def is_palindrome1(head: Optional[ListNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    stack = []
    p = head
    while p:
        stack.append(p.val)
        p = p.next

    cnt = len(stack)
    curr = head
    while stack and cnt >= 0:
        n1 = curr.val
        n2 = stack.pop()
        if n1 != n2:
            return False

        curr = curr.next
        cnt -= 2

    return True


def is_palindrome2(head: Optional[ListNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    # []
    if head is None:
        return False

    # [1]
    if head.next is None:
        return True

    # [1, 2, 3, ...]
    slow = head
    fast = head
    rev = None
    while slow and fast:
        if fast.next is None:
            # list has odd-length, skips middle element
            slow = slow.next
            break
        fast = fast.next.next

        # NOTE: mutates the original list
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


class TestPalindromeLinkedList(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 2, 1], True],
            [[1, 2, 3, 2, 1], True],
            [[1, 2], False],
            [[1], True],
        ]
        return data

    def test_palindrome_linked_list0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h = to_list_node(tc[0])
            expected = tc[1]

            actual = is_palindrome0(h)

            self.assertEqual(actual, expected)

    def test_palindrome_linked_list1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h = to_list_node(tc[0])
            expected = tc[1]

            actual = is_palindrome1(h)

            self.assertEqual(actual, expected)

    def test_palindrome_linked_list2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h = to_list_node(tc[0])
            expected = tc[1]

            actual = is_palindrome2(h)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
