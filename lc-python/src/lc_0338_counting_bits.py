import unittest
from typing import List


def count_bits0(n: int) -> List[int]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """

    def nb_bits(x: int) -> int:
        cnt = 0
        while x > 0:
            cnt += x % 2
            x //= 2
        return cnt

    return list(map(nb_bits, range(n + 1)))


def count_bits(n: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # dynamic programming approach
    #
    # | n   | bits | count | Note      |
    # | --- | ---- | ----- | --------- |
    # | 0   | 0000 | 0     | base case |
    # |     |      |       |           |
    # | 1   | 0001 | 1     | 1 up + 1  |
    # |     |      |       |           |
    # | 2   | 0010 | 1     | 2 up + 1  |
    # | 3   | 0011 | 2     | 2 up + 1  |
    # |     |      |       |           |
    # | 4   | 0100 | 1     | 4 up + 1  |
    # | 5   | 0101 | 2     | 4 up + 1  |
    # | 6   | 0110 | 2     | 4 up + 1  |
    # | 7   | 0111 | 3     | 4 up + 1  |
    # |     |      |       |           |
    # | 8   | 1000 | 1     | 8 up + 1  |
    # | 9   | 1001 | 2     | 8 up + 1  |
    # | 10  | 1010 | 2     | 8 up + 1  |
    # | 11  | 1011 | 3     | 8 up + 1  |
    # | 12  | 1100 | 2     | 8 up + 1  |
    # | 13  | 1101 | 3     | 8 up + 1  |
    # | 14  | 1110 | 3     | 8 up + 1  |
    # | 15  | 1111 | 4     | 8 up + 1  |
    #
    # etc...

    # base case
    if n == 0:
        return [0]

    ans = [0]

    offset = 1
    for i in range(1, n + 1):
        if i == offset * 2:
            offset *= 2
        ans.append(1 + ans[i - offset])

    return ans


class TestCountingBits(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [0, [0]],
            [1, [0, 1]],
            [2, [0, 1, 1]],
            [3, [0, 1, 1, 2]],
            [4, [0, 1, 1, 2, 1]],
            [5, [0, 1, 1, 2, 1, 2]],
            [6, [0, 1, 1, 2, 1, 2, 2]],
            [7, [0, 1, 1, 2, 1, 2, 2, 3]],
            [8, [0, 1, 1, 2, 1, 2, 2, 3, 1]],
        ]
        return data

    def test_count_bits0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = count_bits0(n)

            self.assertEqual(actual, expected)

    def test_count_bits(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            expected = tc[1]

            actual = count_bits(n)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
