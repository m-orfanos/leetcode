import unittest
from typing import List


def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Time complexity: O(n log n)
    Space complexity: O(log n)
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i - 1] == nums[i]:
            return True
    return False


def contains_duplicate_map(nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = {}
    for x in nums:
        if x in seen:
            return True
        seen[x] = True
    return False


def contains_duplicate_set1(nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = set()
    for x in nums:
        if x in s:
            return True
        s.add(x)
    return False


def contains_duplicate_set2(nums: List[int]) -> bool:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    return len(nums) != len(set(nums))


class TestContainsDuplicate(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 3, 1], True],
            [[1, 2, 3, 4], False],
            [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True],
        ]
        return data

    def test_contains_duplicate_sort(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = contains_duplicate_sort(xs)

            self.assertEqual(actual, expected)

    def test_contains_duplicate_map(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = contains_duplicate_map(xs)

            self.assertEqual(actual, expected)

    def test_contains_duplicate_set1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = contains_duplicate_set1(xs)

            self.assertEqual(actual, expected)

    def test_contains_duplicate_set2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            xs = tc[0]
            expected = tc[1]

            actual = contains_duplicate_set2(xs)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
