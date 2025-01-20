import unittest
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    # use a dictionary/map as a temporary cache
    nums_dict = {n: i for (i, n) in enumerate(nums)}
    for i, n in enumerate(nums):
        m = target - n
        if m in nums_dict and nums_dict[m] != i:
            return [i, nums_dict[m]]
    return []


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Time complexity: O(n^2)
    Space complexity: O(1)
    """
    # generate 2-length combinations of an array
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


class TestTwoSum(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[2, 7, 11, 15], 9, [0, 1]],
            [[3, 2, 4], 6, [1, 2]],
            [[3, 3], 6, [0, 1]],
        ]
        return data

    def test_two_sum(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            nums = tc[0]
            target = tc[1]
            expected = tc[2]

            actual = two_sum(nums, target)

            self.assertEqual(actual, expected)

    def test_two_sum_brute_force(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            nums = tc[0]
            target = tc[1]
            expected = tc[2]

            actual = two_sum_brute_force(nums, target)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
