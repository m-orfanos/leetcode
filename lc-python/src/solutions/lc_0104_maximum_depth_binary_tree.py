import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree


def maximum_depth_binary_tree_recursive(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def depth(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        ld = depth(node.left)
        rd = depth(node.right)
        return 1 + max(ld, rd)

    return depth(root)


def maximum_depth_binary_tree_dfs(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    max_depth = 0
    stack = [(root, 1)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if node.left:
            stack.append((node.left, depth + 1))
        if node.right:
            stack.append((node.right, depth + 1))
        max_depth = max(depth, max_depth)
    return max_depth


def maximum_depth_binary_tree_bfs(root: Optional[TreeNode]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # bfs, one-level at a time
    max_depth = 0
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
        max_depth += 1
    return max_depth


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
