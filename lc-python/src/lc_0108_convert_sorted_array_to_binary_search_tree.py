import unittest
from typing import List, Optional

from shared.tree import TreeNode, tree_to_list, list_tree_to_tree


def sorted_array_to_binary_search_tree0(nums: List[int]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    # 1,2,3
    # 1,2,3,4
    def dfs(nums, low, high) -> Optional[TreeNode]:
        if low > high:
            return None
        mid = low + (high - low) // 2
        left = dfs(nums, low, mid - 1)
        right = dfs(nums, mid + 1, high)
        return TreeNode(nums[mid], left, right)

    return dfs(nums, 0, len(nums) - 1)


def sorted_array_to_binary_search_tree1(nums: List[int]) -> Optional[TreeNode]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    if len(nums) == 0:
        return None

    low = 0
    high = len(nums) - 1
    mid = low + (high - low) // 2

    root = TreeNode(nums[mid])

    q = [(root, low, mid, high)]
    while q:
        curr, lhs, mid, rhs = q.pop(0)
        if curr is None:
            continue

        # lhs
        if lhs <= mid - 1:
            lmid = lhs + (mid - 1 - lhs) // 2
            curr.left = TreeNode(nums[lmid])
            q.append((curr.left, lhs, lmid, mid - 1))

        # rhs
        if mid + 1 <= rhs:
            rmid = mid + 1 + (rhs - (mid + 1)) // 2
            curr.right = TreeNode(nums[rmid])
            q.append((curr.right, mid + 1, rmid, rhs))

    return root


class Test(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [
                [-10, -3, 0, 5, 9],
                [0, -10, 5, None, -3, None, 9, None, None, None, None],
            ],
            [[1, 3], [1, None, 3, None, None]],
        ]
        return data

    def test_convert_sorted_array_to_binary_search_tree0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            head = tc[0]
            expected = tc[1]

            ans = sorted_array_to_binary_search_tree0(head)
            actual = self.convert(ans)

            self.assertEqual(actual, expected)

    def test_convert_sorted_array_to_binary_search_tree1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            head = tc[0]
            expected = tc[1]

            ans = sorted_array_to_binary_search_tree1(head)
            actual = self.convert(ans)

            self.assertEqual(actual, expected)

    def convert(self, root):
        xs = [root.val]
        q = [root.left, root.right]
        while q:
            n = q.pop(0)
            if n is None:
                xs.append(None)
                continue
            xs.append(n.val)
            q.append(n.left)
            q.append(n.right)
        return xs


if __name__ == "__main__":
    unittest.main()
