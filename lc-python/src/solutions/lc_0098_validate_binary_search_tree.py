import unittest
from typing import List, Optional

from shared.tree import TreeNode, list_tree_to_tree


def is_valid_bst0(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    LHS = 0
    RHS = 1

    def dfs(node: Optional[TreeNode], ancestry: List[int]) -> bool:
        if not node:
            return True

        for cmp, ancestor in ancestry:
            if cmp == LHS and node.val >= ancestor:
                return False
            if cmp == RHS and node.val <= ancestor:
                return False

        l = ancestry[:]
        l.append((LHS, node.val))

        r = ancestry[:]
        r.append((RHS, node.val))

        return dfs(node.left, l) and dfs(node.right, r)

    return dfs(root, [])


def is_valid_bst1(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def dfs(node: Optional[TreeNode], lhs: List[int], rhs: List[int]) -> bool:
        if not node:
            return True

        for l in lhs:
            if node.val >= l:
                return False
        for r in rhs:
            if node.val <= r:
                return False

        clhs = lhs[:]
        clhs.append(node.val)

        crhs = rhs[:]
        crhs.append(node.val)

        return dfs(node.left, clhs, rhs) and dfs(node.right, lhs, crhs)

    return dfs(root, [], [])


def is_valid_bst2(root: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    def dfs(node: Optional[TreeNode], cmin: int, cmax: int) -> bool:
        if not node:
            return True
        if cmin <= node.val or node.val <= cmax:
            return False
        return dfs(node.left, node.val, cmax) and dfs(node.right, cmin, node.val)

    return dfs(root, 2**63 - 1, -(2**63) + 1)


class TestValidateBinarySearchTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[2, 1, 3], True],
            [[5, 1, 4, None, None, 3, 6], False],
            [[2, 2, 2], False],
            [[5, 4, 6, None, None, 3, 7], False],
            [[3, 1, 5, 0, 2, 4, 6], True],
            [[32, 26, 47, 19, None, None, 56, None, 27], False],
            [[3, None, 30, 10, None, None, 15, None, 45], False],
        ]
        return data

    def test_validate_binary_search_tree0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = is_valid_bst0(a)

            self.assertEqual(actual, expected, f"is_valid_bst0 t#{i} - {tc[0]} failed")

    def test_validate_binary_search_tree1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = is_valid_bst1(a)

            self.assertEqual(actual, expected, f"is_valid_bst1 t#{i} - {tc[0]} failed")

    def test_validate_binary_search_tree2(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = list_tree_to_tree(tc[0])
            expected = tc[1]

            actual = is_valid_bst2(a)

            self.assertEqual(actual, expected, f"is_valid_bst2 t#{i} - {tc[0]} failed")


if __name__ == "__main__":
    unittest.main()
