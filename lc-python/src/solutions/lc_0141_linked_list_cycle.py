import unittest
from typing import Optional

from shared.linked_list import ListNode


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
    if head is None:
        return False
    slow = head
    fast = head.next
    while slow and fast and slow is not fast:
        slow = slow.next
        fast = fast.next.next if fast.next else None
    return slow is fast


class TestLinkedListCycle(unittest.TestCase):
    @staticmethod
    def parse_input():
        a = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
        a.next.next.next.next = a

        b = ListNode(1, ListNode(2))
        b.next.next = b

        return [[a, True], [b, True], [ListNode(1), False]]

    def test_linked_list_cycle(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            head = tc[0]
            expected = tc[1]

            actual = has_cycle(head)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
