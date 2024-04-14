import unittest
from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    low = 0
    high = len(nums) - 1
    while low <= high:
        # avoids upcasting (or int overflow in other languages)
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


class TestBinarySearch(unittest.TestCase):

    @staticmethod
    def parse_input():
        data = [
            [[-1, 0, 3, 5, 9, 12], 9, 4],
            [[-1, 0, 3, 5, 9, 12], 2, -1],
        ]
        return data

    def test_binary_search(self):
        data = self.parse_input()
        for i, tc in enumerate(data):
            actual = binary_search(tc[0], tc[1])
            expected = tc[2]
            self.assertEqual(actual, expected, f"{i} {tc}")


if __name__ == "__main__":
    unittest.main()
