import unittest
import sys

from functools import cmp_to_key
from typing import List


def move_zeroes(nums: List[int]) -> None:
    """
    Time complexity: O(n log n)
    Space complexity: O(n log n)
    """

    def zeros_are_massive(a: int, b: int) -> int:
        if a == 0:
            return sys.maxsize - b
        if b == 0:
            return a - sys.maxsize
        else:
            return 0

    nums.sort(key=cmp_to_key(zeros_are_massive))


def move_zeroes1(xs: List[int]) -> None:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    tmp = []
    for i in range(len(xs)):
        if xs[i] != 0:
            tmp.append(xs[i])

    for i in range(len(tmp)):
        xs[i] = tmp[i]

    for i in range(len(xs) - len(tmp)):
        xs[len(xs) - 1 - i] = 0


def move_zeroes2(xs: List[int]) -> None:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    # nice solution on leetcode
    snowball_size = 0
    for i in range(len(xs)):
        if xs[i] == 0:
            snowball_size += 1
        elif snowball_size > 0:
            tmp = xs[i]
            xs[i] = 0
            xs[i - snowball_size] = tmp


def move_zeroes3(xs: List[int]) -> None:
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    non_zero_cnt = 0
    for i in range(len(xs)):
        if xs[i] != 0:
            xs[non_zero_cnt] = xs[i]
            non_zero_cnt += 1

    for i in range(non_zero_cnt, len(xs)):
        xs[i] = 0


class Test(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[0, 1, 0, 3, 12], [1, 3, 12, 0, 0]],
            [[0], [0]],
            [[2, 1], [2, 1]],
        ]
        return data

    def test_move_zeroes(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            move_zeroes(a)

            actual = a

            self.assertEqual(actual, expected)

    def test_move_zeroes1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            move_zeroes1(a)

            actual = a

            self.assertEqual(actual, expected)

    def test_move_zeroes2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            move_zeroes2(a)

            actual = a

            self.assertEqual(actual, expected)

    def test_move_zeroes3(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            expected = tc[1]

            move_zeroes3(a)

            actual = a

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()