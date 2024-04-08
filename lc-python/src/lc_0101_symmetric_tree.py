import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree


def is_symmetric0(root: Optional[TreeNode]) -> bool:

    def traverse(n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if n1 is None and n2 is None:
            return True
        if n1 is None or n2 is None or n1.val != n2.val:
            return False
        return traverse(n1.left, n2.right) and traverse(n1.right, n2.left)

    return traverse(root.left, root.right)


def is_symmetric1(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    q = [root.left, root.right]

    while q:
        n1 = q.pop(0)
        n2 = q.pop(0)
        if n1 is None and n2 is None:
            continue
        if n1 is None or n2 is None or n1.val != n2.val:
            return False
        q.append(n1.left)
        q.append(n2.right)
        q.append(n1.right)
        q.append(n2.left)

    return True


class TestSymmetricTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1], True],
            [[1, 2, 2, 3, 4, 4, 3], True],
            [[1, 2, 2, None, 3, None, 3], False],
        ]
        return data

    def test_symmetric_tree0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = is_symmetric0(a)

            self.assertEqual(actual, expected)

    def test_symmetric_tree1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = is_symmetric1(a)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
