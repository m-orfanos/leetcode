from typing import Callable
import unittest


def first_bad_version(n: int, isBadVersion: Callable[[int], bool]) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    low = 1
    high = n
    while low <= high:
        mid = low + (high - low) // 2
        if isBadVersion(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


class TestFirstBadVersion(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [5, 4, 4],
            [1, 1, 1],
            [3, 2, 2],
        ]
        return data

    def test_first_bad_version(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            n = tc[0]
            version = tc[1]
            expected = tc[2]

            actual = first_bad_version(n, lambda x: x == version)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
