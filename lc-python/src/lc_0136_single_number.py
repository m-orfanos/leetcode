import unittest
from typing import List


def single_number0(xs: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    hist = {}
    for x in xs:
        hist[x] = 1 + hist.get(x, 0)

    for k, cnt in hist.items():
        if cnt == 1:
            return k

    raise ValueError("List is empty")


def single_number1(xs: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # takes advantage of the following
    # 1101 ^ 1101 = 0000
    # 1010 ^ 0000 = 1010
    #
    # alternative
    # from functools import reduce
    # reduce(lambda a, b: a ^ b, xs)
    ans = 0
    for x in xs:
        ans ^= x
    return ans


class TestSingleProblem(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[2, 2, 1], 1],
            [[4, 1, 2, 1, 2], 4],
            [[1], 1],
        ]
        return data

    def test_single_number0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = single_number0(xs)

            self.assertEqual(actual, expected)

    def test_single_number1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = single_number1(xs)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
