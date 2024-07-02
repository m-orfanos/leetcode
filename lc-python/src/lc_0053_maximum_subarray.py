import unittest
from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """

    best = -(2**31)
    curr = 0
    for n in nums:
        curr = max(n, curr + n)
        best = max(curr, best)

    return best


class TestMaxSubArray(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
            [[1], 1],
            [[5, 4, -1, 7, 8], 23],
        ]
        return data

    def test_max_sub_array(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            nums = tc[0]
            expected = tc[1]

            actual = max_sub_array(nums)

            self.assertEqual(actual, expected, f"{nums} {expected}")


if __name__ == "__main__":
    unittest.main()
