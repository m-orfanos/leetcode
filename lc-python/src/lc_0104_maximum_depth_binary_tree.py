import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree


def maximum_depth_binary_tree_recursive(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def depth(node: Optional[TreeNode], d=0) -> int:
        if not node:
            return d
        lhs = depth(node.left, d)
        rhs = depth(node.right, d)
        return 1 + max(lhs, rhs)

    return depth(root)


def maximum_depth_binary_tree_dfs(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # dfs = go deep, retreat, repeat
    depth = 0
    stack = [(root, 1)]
    while len(stack) > 0:
        node, d = stack.pop()
        if node.left:
            stack.append((node.left, d + 1))
        if node.right:
            stack.append((node.right, d + 1))
        depth = max(d, depth)
    return depth


def maximum_depth_binary_tree_bfs(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # bfs = one-level at a time
    depth = 0
    queue = [root]
    while len(queue) > 0:
        size = len(queue)
        while size > 0:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            size -= 1
        depth += 1
    return depth


class TestMaximumDepthBinaryTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[3, 9, 20, None, None, 15, 7], 3],
            [[1, None, 2], 2],
        ]
        return data

    def test_maximum_depth_binary_tree_recursive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = maximum_depth_binary_tree_recursive(xs)

            self.assertEqual(actual, expected)

    def test_maximum_depth_binary_tree_dfs(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = maximum_depth_binary_tree_dfs(xs)

            self.assertEqual(actual, expected)

    def test_maximum_depth_binary_tree_bfs(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = maximum_depth_binary_tree_bfs(xs)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
