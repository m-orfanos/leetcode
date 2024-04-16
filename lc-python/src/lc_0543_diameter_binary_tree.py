import unittest
from typing import Optional, Tuple

from shared.tree import TreeNode, list_tree_to_tree


def diameter_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    # NOTE: The height of a node is the number of edges present in the longest path
    # connecting that node to a leaf node.
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        if not node:
            return (0, 0)

        lh, ld = dfs(node.left)
        rh, rd = dfs(node.right)

        height = 1 + max(lh, rh)
        diameter = max(lh + rh, ld, rd)

        return (height, diameter)

    return dfs(root)[1]


class TestDiameterBinaryTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 3, 4, 5], 3],
            [[1, 2], 1],
            [
                [
                    4,
                    -7,
                    -3,
                    None,
                    None,
                    -9,
                    -3,
                    9,
                    -7,
                    -4,
                    None,
                    6,
                    None,
                    -6,
                    -6,
                    None,
                    None,
                    0,
                    6,
                    5,
                    None,
                    9,
                    None,
                    None,
                    -1,
                    -4,
                    None,
                    None,
                    None,
                    -2,
                ],
                8,
            ],
        ]
        return data

    def test_diameter_binary_tree(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = diameter_binary_tree(xs)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
