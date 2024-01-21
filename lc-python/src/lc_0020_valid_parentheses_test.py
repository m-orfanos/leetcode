import unittest

from lib import read_lines, chunks
from lc_0020_valid_parentheses import isValid


def parse_input():
    lines = read_lines("lc_0020_valid_parentheses.dat")
    lines_chunks = chunks(lines, 2)
    ans = []
    for chunk in lines_chunks:
        s = chunk[0]
        exp = chunk[1] == "true"
        ans.append([s, exp])
    return ans


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        test_cases = parse_input()
        for tc in test_cases:
            actual = isValid(tc[0])
            expected = tc[1]
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
