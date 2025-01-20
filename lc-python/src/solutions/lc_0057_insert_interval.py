import unittest
from typing import List


def insert0(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Time complexity: O(n log n)
    Space complexity: O(n)
    """
    # add `newInterval` to the list and sort
    intervals.append(newInterval)
    intervals.sort(key=lambda x: x[0])

    # create a new list to hold the response
    # either append OR merge the ith element into the response
    ans = [intervals[0]]
    for [si, ei] in intervals[1:]:
        [sp, ep] = ans[-1]
        if sp <= si <= ep or sp <= ei <= ep:
            st = min(sp, si)
            et = max(ep, ei)
            ans[-1] = [st, et]
        else:
            ans.append([si, ei])

    return ans


def insert1(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """

    ans = []

    # add intervals until overlap occurs
    i = 0
    while i < len(intervals):
        [si, ei] = intervals[i]
        if ei >= newInterval[0]:
            break
        ans.append([si, ei])
        i += 1

    # merge overlapping intervals
    merged = newInterval
    while i < len(intervals):
        [si, ei] = intervals[i]
        [sm, em] = merged
        if si > em:
            break
        merged = [min(sm, si), max(em, ei)]
        i += 1

    # add merged interval
    ans.append(merged)

    # add remaining intervals
    for interval in intervals[i:]:
        ans.append(interval)

    return ans


class TestInsertInterval(unittest.TestCase):
    @staticmethod
    def parse_input():
        data = [
            [[[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]],
            [
                [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
                [4, 8],
                [[1, 2], [3, 10], [12, 16]],
            ],
            [[[1, 5]], [6, 8], [[1, 5], [6, 8]]],
        ]
        return data

    def test_insert_interval0(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            intervals = tc[0]
            newInterval = tc[1]
            expected = tc[2]

            actual = insert0(intervals, newInterval)

            self.assertEqual(actual, expected, f"Solution `insert0`, test case #{i}")

    def test_insert_interval1(self):
        test_cases = self.parse_input()
        for i, tc in enumerate(test_cases):
            intervals = tc[0]
            newInterval = tc[1]
            expected = tc[2]

            actual = insert1(intervals, newInterval)

            self.assertEqual(actual, expected, f"Solution `insert1`, test case #{i}")


if __name__ == "__main__":
    unittest.main()
