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
        mid = (low + high) // 2
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        test_cases = [[[-1, 0, 3, 5, 9, 12], 9, 4], [[-1, 0, 3, 5, 9, 12], 2, -1]]
        for i, tc in enumerate(test_cases):
            actual = binary_search(tc[0], tc[1])
            expected = tc[2]
            self.assertEqual(actual, expected, f"{i} {tc}")


if __name__ == "__main__":
    unittest.main()
