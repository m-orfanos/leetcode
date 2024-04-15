import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree


def is_balanced(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def dfs(node: Optional[TreeNode]) -> int:
        # base case
        if node is None:
            return 0

        # depth-first traversal
        dl = dfs(node.left)
        dr = dfs(node.right)

        # short-circuit
        if dl == -1 or dr == -1 or abs(dl - dr) > 1:
            return -1

        # accumulator
        return 1 + max(dl, dr)

    return dfs(root) != -1


class TestBalancedBinaryTree(unittest.TestCase):

    def test_balanced_binary_tree(self):
        test_cases = [
            [[3, 9, 20, None, None, 15, 7], True],
            [[1, 2, 2, 3, 3, None, None, 4, 4], False],
            [[], True],
        ]
        for i, tc in enumerate(test_cases):
            t = list_tree_to_tree(tc[0])
            actual = is_balanced(t)
            expected = tc[1]
            self.assertEqual(actual, expected, f"{i} {tc}")


if __name__ == "__main__":
    unittest.main()
