import unittest
from typing import List, Optional

from src.shared.tree import TreeNode, list_tree_to_tree, tree_to_list
from shared.linked_list import ListNode, to_list_node, list_node_to_list

def problem(tree: Optional[TreeNode], 
            xs: Optional[ListNode], 
            nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return False


class Test(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = []
        return data

    def test_(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = tc[2]

            actual = problem(a, b)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
