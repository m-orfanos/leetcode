import unittest
from typing import Optional

from shared.linked_list import ListNode, to_list_node, list_node_to_list


def middle_linked_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

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


def middle_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class TestMiddleLinkedList(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 3, 4, 5], [3, 4, 5]],
            [[1, 2, 3, 4, 5, 6], [4, 5, 6]],
        ]
        return data

    def test_middle_linked_list_recursive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = to_list_node(tc[0])
            expected = tc[1]

            actual = list_node_to_list(middle_linked_list_recursive(xs))

            self.assertEqual(actual, expected)

    def test_middle_linked_list(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = to_list_node(tc[0])
            expected = tc[1]

            actual = list_node_to_list(middle_linked_list(xs))

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
