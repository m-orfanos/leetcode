import unittest
from typing import List, Optional

from src.shared.tree import TreeNode, list_tree_to_tree


def is_balanced(root: Optional[TreeNode]) -> bool:
    def bfs(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        dl = bfs(node.left)
        dr = bfs(node.right)
        if dl == -1 or dr == -1 or abs(dl - dr) > 1:
            return -1
        return 1 + max(dl, dr)

    return bfs(root) != -1


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
