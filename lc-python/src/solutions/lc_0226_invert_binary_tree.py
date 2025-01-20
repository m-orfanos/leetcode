import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree, tree_to_list


def invert_tree0(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    # traverse the tree using depth-first traversal
    # when visiting a node, swap its leaves
    def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if node is None:
            return None

        # swap tree nodes
        temp = node.left
        node.left = node.right
        node.right = temp

        # traverse
        dfs(node.left)
        dfs(node.right)

        return node

    return dfs(root)


def invert_tree1(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = [root]
    while s:
        n = s.pop()

        # base case
        if n is None:
            continue

        # swap
        tmp = n.left
        n.left = n.right
        n.right = tmp

        # traverse
        s.append(n.left)
        s.append(n.right)

    return root


def invert_tree2(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    q = [root]
    while q:
        n = q.pop(0)

        # base case
        if n is None:
            continue

        # swap
        tmp = n.left
        n.left = n.right
        n.right = tmp

        # traverse
        q.append(n.left)
        q.append(n.right)

    return root


class TestInvertBinaryTree(unittest.TestCase):

    @staticmethod
    def parse_input():
        data = [
            [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
            [[2, 1, 3], [2, 3, 1]],
            [[], []],
        ]
        return data

    def test_invert_binary_tree0(self):
        data = self.parse_input()

        for tc in data:
            h = tree_to_list(invert_tree0(list_tree_to_tree(tc[0])))
            self.assertEqual(h, tc[1])

    def test_invert_binary_tree1(self):
        data = self.parse_input()

        for tc in data:
            h = tree_to_list(invert_tree1(list_tree_to_tree(tc[0])))
            self.assertEqual(h, tc[1])

    def test_invert_binary_tree2(self):
        data = self.parse_input()

        for tc in data:
            h = tree_to_list(invert_tree2(list_tree_to_tree(tc[0])))
            self.assertEqual(h, tc[1])


if __name__ == "__main__":
    unittest.main()
