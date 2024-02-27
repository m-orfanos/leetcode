import unittest

from lib import read_lines, chunks, to_list_int
from lc_0226_invert_binary_tree import list_tree_to_tree, tree_to_list, invert_tree


def parse_input():
    lines = read_lines("lc_0226_invert_binary_tree.dat")
    lines_chunks = chunks(lines, 2)
    ans = []
    for chunk in lines_chunks:
        l = to_list_int(chunk[0])
        n = to_list_int(chunk[1])
        ans.append((l, n))
    return ans


class TestInvertBinaryTree(unittest.TestCase):
    def test_invert_binary_tree(self):
        test_cases = parse_input()
        for tc in test_cases:
            h = tree_to_list(invert_tree(list_tree_to_tree(tc[0])))
            self.assertEqual(h, tc[1])


if __name__ == "__main__":
    unittest.main()
