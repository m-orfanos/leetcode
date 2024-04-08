import unittest
from typing import List


def missing_number(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)

    NOTE: 1 + 2 + ... + n = n*(n+1)/2

    | n | nums  |n_sum| missing |
    |---|-------|-----|---------|
    | 1 |   [0] |  1  | 1-0 = 1 |
    | 1 |   [1] |  1  | 1-1 = 0 |
    | 2 | [0,1] |  3  | 3-1 = 2 |
    | 2 | [0,2] |  3  | 3-2 = 1 |
    |...|  ...  | ... |   ...   |
    """
    n = len(nums)
    n_sum = (n * (n + 1)) // 2
    return n_sum - sum(nums)


class Test(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[3, 0, 1], 2],
            [[0, 1], 2],
            [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
            [[1], 0],
            [[0], 1],
        ]
        return data

    def test_(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = missing_number(a)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
