import unittest
from typing import List, Optional

from shared.linked_list import ListNode, list_to_list_node, list_node_to_list
from shared.tree import TreeNode, list_tree_to_tree, tree_to_list
from shared.graph import Node, graph_to_list_graph, list_graph_to_graph


def problem3(x: List[int]) -> bool:
    tmp: Optional[Node] = list_graph_to_graph(x)
    copy: List[int] = graph_to_list_graph(tmp)
    return x == copy


def problem2(x: List[int]) -> bool:
    tmp: Optional[TreeNode] = list_tree_to_tree(x)
    copy: List[int] = tree_to_list(tmp)
    return x == copy


def problem1(x: List[int]) -> bool:
    tmp: Optional[ListNode] = list_to_list_node(x)
    copy: List[int] = list_node_to_list(tmp)
    return x == copy


def problem0(x: List[int]) -> bool:
    """
    Time complexity: O(?)
    Space complexity: O(?)
    """
    return False


class Test(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = []
        return data

    def test_(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = tc[1]

            actual = problem0(a)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
