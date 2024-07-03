import unittest
from typing import List
from functools import cmp_to_key
from heapq import heappop, heappush, heappushpop


def k_closest0(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Brute-force-ish approach

    Time complexity: O(n log n)
    Space complexity: O(n)
    """

    def compare(a: List[int], b: List[int]) -> int:
        return a[0] * a[0] + a[1] * a[1] - b[0] * b[0] - b[1] * b[1]

    points.sort(key=cmp_to_key(compare))

    return points[:k]


def k_closest1(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Max-heap approach

    Time complexity: O(n log k)
      headpush, heappop, heappushpop are all O(log k),
      where k is the number of elements in the heap

    Space complexity: O(k)
    """
    q = []

    for i in range(k):
        [x, y] = points[i]
        heappush(q, [-(x * x + y * y), [x, y]])

    for [x, y] in points[k:]:
        heappushpop(q, [-(x * x + y * y), [x, y]])

    return [heappop(q)[1] for _ in range(k)]


def k_closest2(points: List[List[int]], k: int) -> List[List[int]]:
    """
    A modified quick-sort approach (aka quickselect) shared by another LeetCode user.

    https://en.wikipedia.org/wiki/Quicksort
    https://en.wikipedia.org/wiki/Quickselect

    Time complexity: O(n) (average), O(n^2) (worst)
    Space complexity: O(1)
    """

    def mid(low: int, high: int) -> int:
        return high - (high - low) // 2

    def euclid(p: List[int]) -> int:
        return p[0] * p[0] + p[1] * p[1]

    def swap(a: int, b: int):
        tmp = points[a]
        points[a] = points[b]
        points[b] = tmp

    # alternative to `hoare_partition`
    # def lomuto_partition(lo: int, hi: int) -> int:
    #     pivot = points[mid(lo, hi)]
    #
    #     i = lo
    #     for j in range(lo, hi):
    #         if euclid(points[j]) - euclid(pivot) < 0:
    #             swap(i, j)
    #             i += 1
    #
    #     swap(i, hi)
    #
    #     return i

    def hoare_partition(lo: int, hi) -> int:
        pivot = points[mid(lo, hi)]

        l = lo
        r = hi
        while True:
            while euclid(points[l]) - euclid(pivot) < 0:
                l += 1
            while euclid(points[r]) - euclid(pivot) > 0:
                r -= 1
            if l >= r:
                break
            swap(l, r)

        return r

    partition = hoare_partition

    l = 0
    r = len(points) - 1
    while l <= r:
        p = partition(l, r)
        if p == k:
            break
        elif p < k:
            l = p + 1
        else:
            r = p - 1

    return points[:k]


class TestKClosest(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[[1, 3], [-2, 2]], 1, [[-2, 2]]],
            [[[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]],
            [
                [[9, -1], [3, 3], [5, -1], [5, 5], [-2, 4]],
                4,
                [[-2, 4], [3, 3], [5, -1], [5, 5]],
            ],
        ]
        return data

    def test_k_closest0(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = sorted(tc[2])

            actual = sorted(k_closest0(a, b))

            self.assertEqual(actual, expected, f"k_closest1 {a} {b} {expected}")

    def test_k_closest1(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = sorted(tc[2])

            actual = sorted(k_closest1(a, b))

            self.assertEqual(actual, expected, f"k_closest0 {a} {b} {expected}")

    def test_k_closest2(self):
        test_cases = self.parse_input()
        for tc in test_cases:
            a = tc[0]
            b = tc[1]
            expected = sorted(tc[2])

            actual = sorted(k_closest2(a, b))

            self.assertEqual(actual, expected, f"k_closest0 {a} {b} {expected}")


if __name__ == "__main__":
    unittest.main()
