import unittest

from lib import read_lines, chunks
from lc_0125_valid_palindrome import isPalindrome


def parse_input():
    lines = read_lines("lc_0125_valid_palindrome.dat")
    lines_chunks = chunks(lines, 2)
    ans = []
    for chunk in lines_chunks:
        l = chunk[0]
        n = chunk[1] == "true"
        ans.append((l, n))
    return ans


class TestTwoSum(unittest.TestCase):
    def test_is_palindrome(self):
        test_cases = parse_input()
        for tc in test_cases:
            self.assertEqual(isPalindrome(tc[0]), tc[1])


if __name__ == "__main__":
    unittest.main()
