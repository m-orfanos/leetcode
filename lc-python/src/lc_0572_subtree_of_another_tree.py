import unittest
from typing import Optional, List

from shared.tree import TreeNode, list_tree_to_tree


def is_subtree0(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n*m)
    Space complexity: O(n)
    """

    def is_same(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        if h1 is None and h2 is None:
            return True
        elif (h1 is None) or (h2 is None):
            return False
        elif h1.val != h2.val:
            return False
        else:
            return is_same(h1.left, h2.left) and is_same(h1.right, h2.right)

    def dfs(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        if h1 is None:
            return False
        if is_same(h1, h2):
            return True
        return dfs(h1.left, h2) or dfs(h1.right, h2)

    return dfs(root, subRoot)


def is_subtree1(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n*m)
    Space complexity: O(n)
    """

    def is_same(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        # bfs again
        q = [(h1, h2)]
        while q:
            n1, n2 = q.pop(0)
            if n1 is None and n2 is None:
                continue
            if (n1 is None) or (n2 is None):
                return False
            if n1.val != n2.val:
                return False
            q.append((n1.left, n2.left))
            q.append((n1.right, n2.right))
        return True

    def bfs(h1: Optional[TreeNode], h2: Optional[TreeNode]) -> bool:
        q = [h1]
        while q:
            n = q.pop(0)
            if n is None:
                continue
            if is_same(n, h2):
                return True
            q.append(n.left)
            q.append(n.right)
        return False

    return bfs(root, subRoot)


def is_subtree2(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Time complexity: O(n+m)
    Space complexity: O(max(n,m))
    """

    def dfs(h: Optional[TreeNode]) -> List[int]:
        s = []
        q = [h]
        while q:
            n = q.pop()
            if n is None:
                s.append(None)
                continue
            s.append(n.val)
            q.append(n.left)
            q.append(n.right)
        return s

    def kmp_search(pat: List[int], txt: List[int]) -> bool:
        def compute_lps(pat: List[int]) -> None:
            lps = [0] * len(pat)

            l = 0
            i = 1

            while i < len(pat):
                if pat[i] == pat[l]:
                    l += 1
                    lps[i] = l
                    i += 1
                else:
                    if l != 0:
                        l = lps[l - 1]
                    else:
                        lps[i] = 0
                        i += 1

            return lps

        # longest prefix suffix
        lps = compute_lps(pat)

        plen = len(pat)
        tlen = len(txt)

        i = 0
        j = 0

        while (tlen - i) >= (plen - j):
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == plen:
                return True

            if i < tlen and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    return kmp_search(dfs(subRoot), dfs(root))


class TestSubtreeofAnotherTree(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[3, 4, 5, 1, 2], [4, 1, 2], True],
            [[3, 4, 5, 1, 2, None, None, None, None, 0], [4, 1, 2], False],
            [
                [
                    4,
                    -9,
                    5,
                    None,
                    -1,
                    None,
                    8,
                    -6,
                    0,
                    7,
                    None,
                    None,
                    -2,
                    None,
                    None,
                    None,
                    None,
                    -3,
                ],
                [5],
                False,
            ],
        ]
        return data

    def test_is_subtree0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h1 = list_tree_to_tree(tc[0])
            h2 = list_tree_to_tree(tc[1])
            expected = tc[2]

            actual = is_subtree0(h1, h2)

            self.assertEqual(actual, expected)

    def test_is_subtree1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h1 = list_tree_to_tree(tc[0])
            h2 = list_tree_to_tree(tc[1])
            expected = tc[2]

            actual = is_subtree1(h1, h2)

            self.assertEqual(actual, expected)

    def test_is_subtree2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            h1 = list_tree_to_tree(tc[0])
            h2 = list_tree_to_tree(tc[1])
            expected = tc[2]

            actual = is_subtree2(h1, h2)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
