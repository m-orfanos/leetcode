import unittest
from typing import List, Optional
from collections import deque

from shared.tree import TreeNode, list_tree_to_tree


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if not root:
        return []

    q = deque()
    q.append((root, 0))

    ans = []
    tmp = []
    curr = 0
    while q:
        n, level = q.popleft()

        if curr != level:
            ans.append(tmp)
            tmp = []
            curr += 1

        tmp.append(n.val)

        if n.left:
            q.append((n.left, level + 1))
        if n.right:
            q.append((n.right, level + 1))

    if len(tmp) > 0:
        ans.append(tmp)

    return ans


class TestBinaryTreeLevelOrderTraversal(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]],
            [[1], [[1]]],
            [[], []],
            [[1, 2], [[1], [2]]],
            [[1, 2, None, 3, None, 4, None, 5], [[1], [2], [3], [4], [5]]],
        ]
        return data

    def test_binary_tree_level_order_traversal(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = level_order(a)

            self.assertEqual(actual, expected, f"{a} {expected}")


if __name__ == "__main__":
    unittest.main()
