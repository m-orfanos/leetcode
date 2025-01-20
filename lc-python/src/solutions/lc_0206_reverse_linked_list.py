import unittest
from typing import List, Optional

from shared.linked_list import ListNode, list_to_list_node, list_node_to_list


def reverse_linked_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def reverse(
        curr: Optional[ListNode], acc: Optional[ListNode]
    ) -> Optional[ListNode]:
        if curr is None:
            return acc
        acc = ListNode(curr.val, acc)
        return reverse(curr.next, acc)

    return reverse(head, None)


def reverse_linked_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    pt = None
    curr = head
    while curr:
        # cache reference
        t = curr.next

        # point current to previous
        curr.next = pt

        # step forward
        pt = curr
        curr = t

    return pt


class TestReverseLinkedList(unittest.TestCase):
    @staticmethod
    def parse_input() -> List[List[List[int]]]:
        data = [
            [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]],
            [[1, 2], [2, 1]],
            [[], []],
        ]
        return data

    def test_reverse_linked_list_recursive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_to_list_node(tc[0])
            expected = tc[1]

            actual = list_node_to_list(reverse_linked_list_recursive(xs))

            self.assertEqual(actual, expected)

    def test_reverse_linked_list_iterative(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_to_list_node(tc[0])
            expected = tc[1]

            t = reverse_linked_list_iterative(xs)
            actual = list_node_to_list(t)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
