import unittest

from lib import list_node_to_list, read_lines, chunks, to_list_int, to_list_node
from lc_0021_merge_two_sorted_lists import merge_two_lists


def parse_input():
    lines = read_lines("lc_0021_merge_two_sorted_lists.dat")
    lines_chunks = chunks(lines, 3)
    ans = []
    for chunk in lines_chunks:
        lst1 = to_list_node(to_list_int(chunk[0]))
        lst2 = to_list_node(to_list_int(chunk[1]))
        lst3 = to_list_node(to_list_int(chunk[2]))
        ans.append([lst1, lst2, lst3])
    return ans


class TestMergeTwoSortedLists(unittest.TestCase):
    def test_merge_two_sorted_lists(self):
        test_cases = parse_input()
        for tc in test_cases:
            actual = list_node_to_list(merge_two_lists(tc[0], tc[1]))
            expected = list_node_to_list(tc[2])
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
