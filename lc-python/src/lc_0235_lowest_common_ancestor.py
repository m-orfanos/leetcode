import unittest
from typing import List

from shared.tree import TreeNode, list_tree_to_tree


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # take advantage of the BST's structure
    # if p < q, then the LCA must be in the LHS of the current node.
    # otherwise it must be on the RHS.
    node = root
    while node:
        if p.val < node.val > q.val:
            node = node.left
        elif p.val > node.val < q.val:
            node = node.right
        else:
            return node


def lowest_common_ancestor0(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # build an ancestry list for each node
    # iterate over the ancestries until a mismatch is found

    def find_ancestors(root: TreeNode, node: TreeNode) -> List[int]:
        ancestors = []
        curr = root
        while curr:
            ancestors.append(curr.val)
            if curr.val > node.val:
                curr = curr.left
            elif curr.val < node.val:
                curr = curr.right
            else:
                break
        return ancestors

    # build ancestry lists
    ancestors_p = find_ancestors(root, p)
    ancestors_q = find_ancestors(root, q)

    # traverse ancestries until a mismatch is found
    l = min(len(ancestors_p), len(ancestors_q))
    for i in range(l):
        if ancestors_p[i] == ancestors_q[i]:
            ancestor = ancestors_p[i]
        else:
            break

    return TreeNode(ancestor)


class TestLowestCommonAncestor(unittest.TestCase):
    test_cases = [
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 8, 6],
        [[6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], 2, 4, 2],
        [[2, 1], 2, 1, 2],
    ]

    def to_tree_node(self, tc):
        t = list_tree_to_tree(tc[0])
        p = TreeNode(tc[1])
        q = TreeNode(tc[2])
        return (t, p, q)

    def test_lowest_common_ancestor0(self):
        for tc in self.test_cases:
            (t, p, q) = self.to_tree_node(tc)
            actual = lowest_common_ancestor0(t, p, q)
            expected = tc[3]
            self.assertEqual(actual.val, expected)

    def test_lowest_common_ancestor(self):
        for tc in self.test_cases:
            (t, p, q) = self.to_tree_node(tc)
            actual = lowest_common_ancestor(t, p, q)
            expected = tc[3]
            self.assertEqual(actual.val, expected)


if __name__ == "__main__":
    unittest.main()
