import unittest
from typing import Optional

from shared.tree import TreeNode, list_tree_to_tree


def same_tree_recursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if p is None and q is None:
        return True
    elif p is None or q is None or p.val != q.val:
        return False
    else:
        lhs = same_tree_recursive(p.left, q.left)
        rhs = same_tree_recursive(p.right, q.right)
        return lhs and rhs


def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # stack-based DFS approach

    # given two trees with elements...
    stk = [p, q]

    while len(stk) > 0:
        pn = stk.pop()
        qn = stk.pop()

        if pn is None and qn is None:
            continue

        if pn is None or qn is None or pn.val != qn.val:
            return False

        # the insertion order is important
        stk.append(pn.left)
        stk.append(qn.left)
        stk.append(pn.right)
        stk.append(qn.right)

    return True


class TestSameTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 3], [1, 2, 3], True],
            [[1, 2], [1, None, 2], False],
            [[1, 2, 1], [1, 1, 2], False],
        ]
        return data

    def test_same_tree_recursive(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            p = list_tree_to_tree(tc[0])
            q = list_tree_to_tree(tc[1])
            expected = tc[2]

            actual = same_tree_recursive(p, q)

            self.assertEqual(actual, expected)

    def test_same_tree(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            p = list_tree_to_tree(tc[0])
            q = list_tree_to_tree(tc[1])
            expected = tc[2]

            actual = same_tree(p, q)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
