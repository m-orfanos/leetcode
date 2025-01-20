import unittest
from typing import List


def product_except_self0(nums: List[int]) -> List[int]:
    """
    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    ans = []
    for i in range(len(nums)):
        tmp = 1
        for j in range(len(nums)):
            if i == j:
                continue
            tmp *= nums[j]
        ans.append(tmp)
    return ans


def product_except_self1(nums: List[int]) -> List[int]:
    """
    Create two arrays holding the pair-wise product of elements as follows
        forward[i] = a[0]*a[1]*...*a[i]
        backward[i] = a[i]*a[i+1]*...*a[n]

    then for a given i,
        forward[i-1] * backward[i+1] skips a[i]
    e.g.
        (a[0]*a[1]*...*a[i-1]) * (a[i+1]*a[i+2]*...*a[n])

    Time complexity: O(n)
    Space complexity: O(n)
    """
    n = len(nums)

    forward = [1] * n
    forward[0] = nums[0]

    backward = [1] * n
    backward[n - 1] = nums[n - 1]

    for i in range(1, n):
        forward[i] = forward[i - 1] * nums[i]
        backward[n - 1 - i] = backward[n - 1 - i + 1] * nums[n - 1 - i]

    ans = [0] * n
    ans[0] = backward[1]
    ans[n - 1] = forward[n - 1 - 1]
    for i in range(1, n - 1):
        ans[i] = forward[i - 1] * backward[i + 1]

    return ans


class TestProductofArrayExceptSelf(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[1, 2, 3, 4], [24, 12, 8, 6]],
            [[-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]],
        ]
        return data

    def test_product_of_array_except_self0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = tc[1]

            actual = product_except_self0(a)

            self.assertEqual(actual, expected, f"test case {i} failed")

    def test_product_of_array_except_self1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            a = tc[0]
            expected = tc[1]

            actual = product_except_self1(a)

            self.assertEqual(actual, expected, f"test case {i} failed")


if __name__ == "__main__":
    unittest.main()
