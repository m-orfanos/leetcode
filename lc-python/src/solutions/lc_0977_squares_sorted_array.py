import unittest
from typing import List


def sorted_squares0(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n log n)
    """
    return sorted(map(lambda x: x**2, nums))


def sorted_squares1(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n log n)
    """

    def merge_sorted_lists(xs: List[int], ys: List[int]) -> List[int]:
        ans = [0] * (len(xs) + len(ys))

        i = 0
        j = 0
        k = 0

        while i < len(xs) and j < len(ys):
            if xs[i] < ys[j]:
                ans[k] = xs[i]
                k += 1
                i += 1
            else:
                ans[k] = ys[j]
                j += 1
                k += 1

        while i < len(xs):
            ans[k] = xs[i]
            i += 1
            k += 1

        while j < len(ys):
            ans[k] = ys[j]
            j += 1
            k += 1

        return ans

    def merge(xs: List[int]) -> List[int]:
        if len(xs) <= 1:
            return [x**2 for x in xs]
        left = merge(xs[: len(xs) // 2])
        right = merge(xs[len(xs) // 2 :])
        return merge_sorted_lists(left, right)

    return merge(nums)


def sorted_squares2(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    left = 0
    right = len(nums) - 1

    ans = [0] * len(nums)

    i = len(nums) - 1
    while left <= right:
        lhs = nums[left] ** 2
        rhs = nums[right] ** 2
        if lhs > rhs:
            ans[i] = lhs
            left += 1
        else:
            ans[i] = rhs
            right -= 1
        i -= 1

    return ans


class TestSortedSquares(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]],
            [[-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]],
        ]
        return data

    def test_sorted_squares0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = sorted_squares0(a)

            self.assertEqual(actual, expected)

    def test_sorted_squares1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = sorted_squares1(a)

            self.assertEqual(actual, expected)

    def test_sorted_squares2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            actual = sorted_squares2(a)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
