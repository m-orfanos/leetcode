import unittest

from lib import read_lines, chunks, to_list_int
from lc_0001_two_sum import two_sum, two_sum_brute_force


def parse_input():
    lines = read_lines("lc_0001_two_sum.dat")
    lines_chunks = chunks(lines, 3)
    ans = []
    for chunk in lines_chunks:
        nums = to_list_int(chunk[0])
        target = int(chunk[1])
        expected = to_list_int(chunk[2])
        ans.append([nums, target, expected])
    return ans


class TestTwoSum(unittest.TestCase):
    def test_two_sum(self):
        test_cases = parse_input()
        for tc in test_cases:
            nums = tc[0]
            target = tc[1]
            expected = tc[2]

            actual = two_sum(nums, target)

            self.assertEqual(actual, expected)

    def test_two_sum_brute_force(self):
        test_cases = parse_input()
        for tc in test_cases:
            nums = tc[0]
            target = tc[1]
            expected = tc[2]

            actual = two_sum_brute_force(nums, target)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
