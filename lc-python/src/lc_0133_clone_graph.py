import unittest
from typing import Optional

from shared.graph import Node, graph_to_list_graph, list_graph_to_graph


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    if not node:
        return None

    if not node.neighbors:
        return Node(node.val)

    visited = set()
    copy = {}
    stack = [node]
    while stack:
        n = stack.pop()

        if n.val in visited:
            continue
        visited.add(n.val)

        if n.val not in copy:
            copy[n.val] = Node(n.val)

        for neighbor in n.neighbors:
            stack.append(neighbor)
            if neighbor.val not in copy:
                copy[neighbor.val] = Node(neighbor.val)
            copy[n.val].neighbors.append(copy[neighbor.val])

    return copy[node.val]


class TestCloneGraph(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[[2, 4], [1, 3], [2, 4], [1, 3]], [[2, 4], [1, 3], [2, 4], [1, 3]]],
            [[[]], [[]]],
            [[], []],
        ]
        return data

    def test_clone_graph(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = list_graph_to_graph(tc[0])

            expected = tc[1]
            actual = graph_to_list_graph(clone_graph(a))

            self.assertEqual(actual, expected, f"{a} {expected}")


if __name__ == "__main__":
    unittest.main()
