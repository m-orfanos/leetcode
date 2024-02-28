import unittest

from src.shared.tree import invert_tree, list_tree_to_tree, tree_to_list


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        test_cases = [
            [[4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]],
            [[2, 1, 3], [2, 3, 1]],
            [[], []],
        ]

        for tc in test_cases:
            h = tree_to_list(invert_tree(list_tree_to_tree(tc[0])))
            self.assertEqual(h, tc[1])


if __name__ == "__main__":
    unittest.main()
