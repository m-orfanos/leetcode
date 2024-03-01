import unittest
from typing import Optional

from src.shared.linked_list import ListNode, to_list_node, list_node_to_list


def merge_two_lists(
        list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Create 2 pointers, one for each list. Traverse both lists at the same time building
    the merged list. There are various edge cases to consider since the lists can be
    empty and/or different lengths.

    The approach below purposefully does NOT short-circuit for lists of different
    lengths to avoid sharing memory references.

    Time complexity: O(m+n)
    Space complexity: O(m+n)
    """
    h = None
    p = None

    p1 = list1
    p2 = list2

    # append list1/list2 values
    while p1 is not None and p2 is not None:
        if h is None:
            if p1.val < p2.val:
                h = ListNode(p1.val)
                p1 = p1.next
            else:
                h = ListNode(p2.val)
                p2 = p2.next
            p = h
        else:
            if p1.val < p2.val:
                p.next = ListNode(p1.val)
                p1 = p1.next
            else:
                p.next = ListNode(p2.val)
                p2 = p2.next
            p = p.next

    # list2 is exhausted/empty, append remaining list1 values
    while p1 is not None:
        if h is None:
            h = ListNode(p1.val)
            p = h
        else:
            p.next = ListNode(p1.val)
            p = p.next
        p1 = p1.next

    # list1 is exhausted/empty, append remaining list2 values
    while p2 is not None:
        if h is None:
            h = ListNode(p2.val)
            p = h
        else:
            p.next = ListNode(p2.val)
            p = p.next
        p2 = p2.next

    return h


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        input_data = [
            [[1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]],
            [[], [], []],
            [[], [0], [0]],
            [[5], [1, 2, 4], [1, 2, 4, 5]],
            [[1, 2, 4], [5], [1, 2, 4, 5]],
        ]

        test_cases = []
        for data in input_data:
            lst1 = to_list_node(data[0])
            lst2 = to_list_node(data[1])
            lst3 = to_list_node(data[2])
            test_cases.append([lst1, lst2, lst3])

        for tc in test_cases:
            actual = list_node_to_list(merge_two_lists(tc[0], tc[1]))
            expected = list_node_to_list(tc[2])
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()